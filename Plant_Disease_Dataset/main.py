import json
import os
from datetime import datetime

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
import tensorflow as tf
from PIL import Image

from disease_info import analyze_severity, get_disease_info, get_disease_name


st.set_page_config(
    page_title="Plant Disease Recognition System",
    page_icon="leaf",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
<style>
.stApp {
    background:
        radial-gradient(circle at top left, rgba(116, 198, 157, 0.12), transparent 28%),
        radial-gradient(circle at top right, rgba(241, 196, 15, 0.08), transparent 22%),
        linear-gradient(180deg, #081c15 0%, #0b221b 50%, #102a24 100%);
    color: #e9f5ee;
}
.main-header {
    background: linear-gradient(135deg, #11241c 0%, #1b4332 42%, #2d6a4f 100%);
    padding: 2.2rem;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 1.4rem;
    box-shadow: 0 18px 44px rgba(0, 0, 0, 0.32);
}
.metric-card {
    background: linear-gradient(145deg, #10241d 0%, #1b4332 100%);
    padding: 1rem;
    border-radius: 14px;
    text-align: center;
    color: white;
}
.disease-card {
    background: rgba(13, 33, 27, 0.88);
    backdrop-filter: blur(10px);
    padding: 1rem;
    border-radius: 14px;
    margin-bottom: 0.9rem;
    border-left: 4px solid #52b788;
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.22);
    color: #e9f5ee;
}
.severity-card {
    background: rgba(14, 36, 29, 0.9);
    padding: 1rem;
    border-radius: 14px;
    border: 1px solid #2d6a4f;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.2);
    color: #e9f5ee;
}
.hero-grid {
    display: grid;
    grid-template-columns: 1.35fr 1fr;
    gap: 1rem;
    margin-bottom: 1rem;
}
.hero-panel {
    background: linear-gradient(145deg, rgba(12, 31, 25, 0.95), rgba(19, 44, 36, 0.95));
    border: 1px solid rgba(116, 198, 157, 0.18);
    border-radius: 18px;
    padding: 1.3rem;
    box-shadow: 0 14px 34px rgba(0, 0, 0, 0.24);
    color: #e9f5ee;
}
.hero-panel h3, .hero-panel h4 {
    margin-top: 0;
}
.hero-chip {
    display: inline-block;
    padding: 0.35rem 0.75rem;
    border-radius: 999px;
    background: #16372c;
    color: #d8f3dc;
    font-size: 0.85rem;
    margin: 0.2rem 0.35rem 0.2rem 0;
    border: 1px solid #2d6a4f;
}
.section-title {
    font-size: 1.2rem;
    font-weight: 700;
    color: #d8f3dc;
    margin: 0.7rem 0 0.9rem 0;
}
.soft-panel {
    background: rgba(14, 36, 29, 0.9);
    border-radius: 16px;
    padding: 1rem;
    border: 1px solid rgba(116, 198, 157, 0.12);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.18);
    color: #e9f5ee;
}
.stMarkdown, .stText, p, label, div {
    color: #e9f5ee;
}
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0b1e18 0%, #102922 100%);
}
[data-baseweb="tab-list"] {
    gap: 0.35rem;
}
button[kind="secondary"], button[kind="primary"] {
    border-radius: 12px !important;
}
</style>
""",
    unsafe_allow_html=True,
)

CLASS_NAMES = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
    'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy',
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
    'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy',
    'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold',
    'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot',
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy'
]

if "prediction_history" not in st.session_state:
    st.session_state.prediction_history = []
if "latest_prediction" not in st.session_state:
    st.session_state.latest_prediction = None
if "latest_pathogen_prediction" not in st.session_state:
    st.session_state.latest_pathogen_prediction = None


@st.cache_resource
def load_model():
    return tf.keras.models.load_model("trained_plant_disease_model.keras")


def model_prediction(uploaded_file):
    model = load_model()
    image = Image.open(uploaded_file).convert("RGB").resize((128, 128))
    input_arr = tf.keras.preprocessing.image.img_to_array(image)
    input_arr = np.expand_dims(input_arr, axis=0)
    predictions = model.predict(input_arr, verbose=0)
    return predictions[0]


def get_top_predictions(predictions, top_k=5):
    top_indices = np.argsort(predictions)[-top_k:][::-1]
    results = []
    for idx in top_indices:
        results.append(
            {
                "class": CLASS_NAMES[idx],
                "name": get_disease_name(CLASS_NAMES[idx]),
                "confidence": float(predictions[idx]) * 100,
            }
        )
    return results


def infer_pathogen_profile(class_name):
    class_name = class_name.lower()
    if "bacterial" in class_name:
        return "Bacterial", ["Water splash", "Tool contact", "Leaf surface moisture"]
    if "virus" in class_name or "greening" in class_name:
        return "Viral", ["Vector movement", "Nearby host transfer", "Plant-to-plant exposure"]
    if "mite" in class_name:
        return "Mite-linked", ["Leaf contact", "Dry canopy movement", "Localized spread"]
    return "Fungal", ["Wind-borne spores", "Leaf wetness", "Dense canopy exposure"]


def generate_pathogen_prediction(class_name, severity_result, humidity, temperature_c,
                                 wind_speed, wind_direction, rainfall_level,
                                 nearby_infected_plants):
    pathogen_type, pathways = infer_pathogen_profile(class_name)
    severity_pct = severity_result["percentage"] if severity_result else 0.0

    pressure_points = 0
    if severity_pct >= 45:
        pressure_points += 2
    elif severity_pct >= 20:
        pressure_points += 1

    if humidity >= 75:
        pressure_points += 2
    elif humidity >= 55:
        pressure_points += 1

    if wind_speed >= 18:
        pressure_points += 2
    elif wind_speed >= 8:
        pressure_points += 1

    if rainfall_level in ("Moderate", "Heavy"):
        pressure_points += 1

    if nearby_infected_plants >= 4:
        pressure_points += 2
    elif nearby_infected_plants >= 2:
        pressure_points += 1

    if pressure_points >= 7:
        pressure_band = "High"
    elif pressure_points >= 4:
        pressure_band = "Medium"
    else:
        pressure_band = "Low"

    if pathogen_type == "Bacterial" and rainfall_level in ("Moderate", "Heavy"):
        movement_note = "Splash-driven movement is more likely than long-distance drift."
        likely_direction = f"{wind_direction} and nearby surrounding plants"
    elif pathogen_type == "Viral":
        movement_note = "Movement is likely to depend more on vectors and host proximity than direct wind drift."
        likely_direction = f"{wind_direction} corridor with nearby host plants"
    elif pathogen_type == "Mite-linked":
        movement_note = "Movement is likely to stay localized unless the canopy is tightly packed."
        likely_direction = "adjacent leaves and nearby rows"
    else:
        movement_note = "Wind and leaf moisture are the strongest movement drivers for this profile."
        likely_direction = f"downwind toward {wind_direction}"

    if temperature_c >= 32:
        temp_note = "Current temperature may accelerate activity for heat-tolerant spread."
    elif temperature_c <= 18:
        temp_note = "Cooler temperature may slow pathogen movement."
    else:
        temp_note = "Current temperature is within a moderate movement range."

    severity_score = min(severity_pct / 60, 1.0) * 100
    humidity_score = min(humidity / 100, 1.0) * 100
    wind_score = min(wind_speed / 35, 1.0) * 100
    rainfall_score = {"Low": 35, "Moderate": 68, "Heavy": 92}[rainfall_level]
    nearby_score = min(nearby_infected_plants / 10, 1.0) * 100
    pressure_score = min((pressure_points / 8) * 100, 100)

    return {
        "pathogen_type": pathogen_type,
        "pressure_band": pressure_band,
        "pressure_score": round(pressure_score, 1),
        "likely_direction": likely_direction,
        "movement_note": movement_note,
        "temp_note": temp_note,
        "pathways": pathways,
        "factor_scores": {
            "Severity": round(severity_score, 1),
            "Humidity": round(humidity_score, 1),
            "Wind": round(wind_score, 1),
            "Rainfall": round(rainfall_score, 1),
            "Nearby": round(nearby_score, 1),
        },
        "input_snapshot": {
            "humidity": humidity,
            "temperature_c": temperature_c,
            "wind_speed": wind_speed,
            "wind_direction": wind_direction,
            "rainfall_level": rainfall_level,
            "nearby_infected_plants": nearby_infected_plants,
        },
    }


def build_factor_radar(factor_scores):
    labels = list(factor_scores.keys())
    values = list(factor_scores.values())
    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=values + [values[0]],
            theta=labels + [labels[0]],
            fill="toself",
            line=dict(color="#1d3557", width=2),
            fillcolor="rgba(69, 123, 157, 0.35)",
        )
    )
    fig.update_layout(
        template="plotly_white",
        height=320,
        margin=dict(l=20, r=20, t=30, b=20),
        polar=dict(radialaxis=dict(visible=True, range=[0, 100])),
        showlegend=False,
    )
    return fig


def build_hotspot_grid(wind_direction, time_hours, pressure_score):
    direction_vectors = {
        "N": (0, -1),
        "NE": (1, -1),
        "E": (1, 0),
        "SE": (1, 1),
        "S": (0, 1),
        "SW": (-1, 1),
        "W": (-1, 0),
        "NW": (-1, -1),
    }
    dx, dy = direction_vectors.get(wind_direction, (1, 0))
    time_multiplier = min(max(time_hours / 24, 0.4), 2.0)

    z = []
    text = []
    for y in range(-2, 3):
        z_row = []
        t_row = []
        for x in range(-2, 3):
            if x == 0 and y == 0:
                z_row.append(100)
                t_row.append("Center: infected source plant")
                continue

            alignment = (x * dx) + (y * dy)
            distance = abs(x) + abs(y)
            base = pressure_score * 0.22 * time_multiplier

            if alignment >= 2:
                score = min(95, base + 46 - (distance * 4))
                zone = "strong drift zone"
            elif alignment >= 1:
                score = min(82, base + 28 - (distance * 3))
                zone = "watch zone"
            else:
                score = min(58, base + 10 - (distance * 2))
                zone = "lower pressure zone"

            score = max(score, 8)
            z_row.append(round(score, 1))
            t_row.append(f"Cell ({x},{y}): {zone} after {time_hours}h")
        z.append(z_row)
        text.append(t_row)

    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            x=["Far West", "West", "Center", "East", "Far East"],
            y=["Far North", "North", "Source", "South", "Far South"],
            text=text,
            hovertemplate="%{text}<extra></extra>",
            colorscale=[[0.0, "#d8f3dc"], [0.55, "#ffd166"], [1.0, "#ef476f"]],
            zmin=0,
            zmax=100,
            showscale=False,
        )
    )
    fig.update_layout(
        template="plotly_white",
        height=320,
        margin=dict(l=20, r=20, t=30, b=20),
        yaxis=dict(autorange="reversed"),
    )
    return fig


def show_model_metrics():
    if not os.path.exists("training_hist.json"):
        st.info("training_hist.json not found.")
        return

    with open("training_hist.json", "r", encoding="utf-8") as f:
        hist = json.load(f)

    epochs = list(range(1, len(hist.get("accuracy", [])) + 1))
    if epochs:
        best_val_acc = max(hist.get("val_accuracy", [0]))
        best_val_loss = min(hist.get("val_loss", [0]))
        final_train_acc = hist.get("accuracy", [0])[-1]
        final_val_acc = hist.get("val_accuracy", [0])[-1]

        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.metric("Epochs", len(epochs))
        with m2:
            st.metric("Best Val Accuracy", f"{best_val_acc * 100:.2f}%")
        with m3:
            st.metric("Final Train Accuracy", f"{final_train_acc * 100:.2f}%")
        with m4:
            st.metric("Best Val Loss", f"{best_val_loss:.4f}")

        st.markdown("<div class='soft-panel'>", unsafe_allow_html=True)
        st.markdown("**Training vs Validation Accuracy**")
        df_acc = pd.DataFrame(
            {
                "Epoch": epochs,
                "Train Accuracy": hist.get("accuracy", []),
                "Validation Accuracy": hist.get("val_accuracy", []),
            }
        )
        fig_acc = px.line(df_acc, x="Epoch", y=["Train Accuracy", "Validation Accuracy"], markers=True)
        fig_acc.update_layout(template="plotly_white", height=360, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_acc, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='soft-panel'>", unsafe_allow_html=True)
        st.markdown("**Training vs Validation Loss**")
        df_loss = pd.DataFrame(
            {
                "Epoch": epochs,
                "Train Loss": hist.get("loss", []),
                "Validation Loss": hist.get("val_loss", []),
            }
        )
        fig_loss = px.line(df_loss, x="Epoch", y=["Train Loss", "Validation Loss"], markers=True)
        fig_loss.update_layout(template="plotly_white", height=360, margin=dict(l=20, r=20, t=30, b=20))
        st.plotly_chart(fig_loss, use_container_width=True)
        st.markdown("</div>", unsafe_allow_html=True)


st.sidebar.markdown("## Dashboard")
st.sidebar.markdown("---")
app_mode = st.sidebar.selectbox("Select Page", ["Home", "About", "Disease Recognition", "Prediction History"])
st.sidebar.markdown("---")
st.sidebar.markdown("### Session Stats")
st.sidebar.metric("Total Predictions", len(st.session_state.prediction_history))
if st.session_state.prediction_history:
    diseases_found = sum(1 for p in st.session_state.prediction_history if "healthy" not in p["class"].lower())
    healthy_count = len(st.session_state.prediction_history) - diseases_found
    st.sidebar.metric("Diseases Detected", diseases_found)
    st.sidebar.metric("Healthy Plants", healthy_count)


if app_mode == "Home":
    st.markdown(
        """
    <div class="main-header">
        <h1>Plant Disease Intelligence Hub</h1>
        <p>Screen leaf images, understand severity, and review pathogen movement cues in one clean workflow.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    hero_left, hero_right = st.columns([1.4, 1])
    with hero_left:
        st.markdown(
            """
            <div class="hero-panel">
                <h3>What this platform does</h3>
                <p>Upload a crop leaf image, run disease classification, inspect severity, and explore a pathogen prediction prototype using field conditions.</p>
                <div>
                    <span class="hero-chip">38 disease classes</span>
                    <span class="hero-chip">Severity analysis</span>
                    <span class="hero-chip">Pathogen preview</span>
                    <span class="hero-chip">Review dashboard</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with hero_right:
        st.markdown(
            """
            <div class="hero-panel">
                <h4>Account Access</h4>
                <p>Use these entry points as placeholders for a future authentication flow.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        cta1, cta2 = st.columns(2)
        with cta1:
            if st.button("Login", use_container_width=True, key="home_login"):
                st.info("Login screen can be connected here later.")
        with cta2:
            if st.button("Sign Up", use_container_width=True, key="home_signup"):
                st.info("Sign-up flow can be connected here later.")

    st.markdown("### Core Modules")
    mod1, mod2, mod3 = st.columns(3)
    with mod1:
        st.markdown(
            """
            <div class="disease-card">
                <h4>Disease Detection</h4>
                <p>Predict the most likely disease class from a single uploaded leaf image using the trained CNN model.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with mod2:
        st.markdown(
            """
            <div class="disease-card">
                <h4>Severity Review</h4>
                <p>Estimate affected leaf area and translate the result into severity-aware treatment guidance.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with mod3:
        st.markdown(
            """
            <div class="disease-card">
                <h4>Pathogen Preview</h4>
                <p>Use humidity, rainfall, wind, and nearby infection cues to explore spread pressure and hotspot visuals.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif app_mode == "About":
    st.markdown(
        """
    <div class="main-header">
        <h1>Model Review Dashboard</h1>
        <p>Training history, validation performance, and review-ready metrics for the disease classifier.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )
    show_model_metrics()

    if os.path.exists("model_metrics.json"):
        st.success("Validation metrics loaded successfully.")
    else:
        st.info("model_metrics.json not found. Run generate_metrics.py to regenerate it.")

elif app_mode == "Disease Recognition":
    st.markdown(
        """
    <div class="main-header">
        <h1>Disease Recognition</h1>
        <p>Upload a leaf image, run the classifier, and review severity, treatments, and pathogen cues in a cleaner workspace.</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    test_image = st.file_uploader(
        "Choose a plant leaf image",
        type=["jpg", "jpeg", "png", "JPG", "JPEG", "PNG"],
    )

    if test_image is not None:
        preview_col, action_col = st.columns([1, 1.3])
        with preview_col:
            st.markdown("### Uploaded Image")
            st.image(test_image, use_column_width=True)

        with action_col:
            st.markdown("#### Analysis")
            if st.button("Predict Disease", use_container_width=True, type="primary"):
                with st.spinner("Analyzing image..."):
                    predictions = model_prediction(test_image)
                    top_predictions = get_top_predictions(predictions, top_k=5)
                    top_result = top_predictions[0]

                    result_class = top_result["class"]
                    result_name = top_result["name"]
                    confidence = top_result["confidence"]
                    is_healthy = "healthy" in result_class.lower()

                    severity_result = None
                    if not is_healthy:
                        leaf_image = Image.open(test_image)
                        test_image.seek(0)
                        severity_result = analyze_severity(leaf_image)

                    history_entry = {
                        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "class": result_class,
                        "name": result_name,
                        "confidence": confidence,
                        "image_name": test_image.name,
                    }
                    if severity_result:
                        history_entry["severity"] = severity_result["level"]
                        history_entry["affected_pct"] = severity_result["percentage"]
                    st.session_state.prediction_history.append(history_entry)
                    st.session_state.latest_prediction = {
                        "class": result_class,
                        "name": result_name,
                        "confidence": confidence,
                        "is_healthy": is_healthy,
                        "severity_result": severity_result,
                        "top_predictions": top_predictions,
                        "image_name": test_image.name,
                    }
                    st.session_state.latest_pathogen_prediction = None

        current_prediction = st.session_state.latest_prediction
        if current_prediction and current_prediction.get("image_name") == test_image.name:
            result_class = current_prediction["class"]
            result_name = current_prediction["name"]
            confidence = current_prediction["confidence"]
            is_healthy = current_prediction["is_healthy"]
            severity_result = current_prediction["severity_result"]
            top_predictions = current_prediction["top_predictions"]

            with action_col:
                if is_healthy:
                    st.success(f"Prediction: {result_name} | Confidence: {confidence:.2f}%")
                else:
                    st.warning(f"Prediction: {result_name} | Confidence: {confidence:.2f}%")

                st.markdown("### Top-5 Prediction Confidence")
                chart_data = {
                    "Disease": [p["name"] for p in top_predictions],
                    "Confidence (%)": [p["confidence"] for p in top_predictions],
                }
                fig = px.bar(
                    chart_data,
                    x="Confidence (%)",
                    y="Disease",
                    orientation="h",
                    color="Confidence (%)",
                    color_continuous_scale=["#ffc107", "#40916c", "#2d6a4f"],
                    text="Confidence (%)",
                )
                fig.update_traces(texttemplate="%{text:.2f}%", textposition="outside")
                fig.update_layout(template="plotly_white", height=340, yaxis=dict(autorange="reversed"), margin=dict(l=10, r=80))
                st.plotly_chart(fig, use_container_width=True)

            st.markdown("### Disease Information and Recommendations")
            info = get_disease_info(result_class)
            if info:
                tab1, tab2, tab3, tab4, tab5 = st.tabs(["Description", "Symptoms", "Severity", "Treatments", "Pathogen"])

                with tab1:
                    st.markdown(
                        f"""
                    <div class="disease-card">
                        <h4>Plant: {info['plant']}</h4>
                        <h4>Disease: {info['disease']}</h4>
                        <p>{info['description']}</p>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )

                with tab2:
                    st.markdown(
                        f"""
                    <div class="disease-card">
                        <h4>Symptoms</h4>
                        <p>{info['symptoms']}</p>
                    </div>
                    """,
                        unsafe_allow_html=True,
                    )
                    st.markdown("##### Prevention")
                    for line in info["prevention"].split("\n"):
                        if line.strip():
                            st.markdown(line.strip())

                with tab3:
                    if severity_result:
                        sev = severity_result
                        st.markdown(
                            f"""
                        <div class="severity-card">
                            <h4>Severity Level: <span style="color:{sev['color']};">{sev['level']}</span></h4>
                            <p>Affected Area: <b>{sev['percentage']}%</b></p>
                            <p>Urgency: <b style="color:{sev['color']};">{sev['urgency']}</b></p>
                            <p>{sev['description']}</p>
                            <p><b style="color:{sev['color']};">{sev['action']}</b></p>
                        </div>
                        """,
                            unsafe_allow_html=True,
                        )
                    else:
                        st.info("Severity analysis is shown only for diseased plants.")

                with tab4:
                    if severity_result:
                        st.markdown("##### Treatments")
                        for step in severity_result["treatment_approach"]:
                            st.markdown(step)
                    else:
                        st.info("Treatment steps are shown only for diseased plants.")

                with tab5:
                    if not is_healthy:
                        left_col, right_col = st.columns(2)
                        with left_col:
                            humidity = st.slider("Humidity (%)", 20, 100, 70, key="pathogen_humidity")
                            temperature_c = st.slider("Temperature (C)", 10, 45, 28, key="pathogen_temp")
                            wind_speed = st.slider("Wind Speed (km/h)", 0, 35, 12, key="pathogen_wind")
                            wind_direction = st.selectbox("Wind Direction", ["N", "NE", "E", "SE", "S", "SW", "W", "NW"], index=2, key="pathogen_direction")
                            rainfall_level = st.selectbox("Rainfall / Leaf Wetness", ["Low", "Moderate", "Heavy"], key="pathogen_rainfall")
                            nearby_infected_plants = st.slider("Nearby Infected Plants", 0, 10, 2, key="pathogen_nearby")

                            if st.button("Predict Pathogen", use_container_width=True, key="predict_pathogen"):
                                st.session_state.latest_pathogen_prediction = generate_pathogen_prediction(
                                    result_class,
                                    severity_result,
                                    humidity,
                                    temperature_c,
                                    wind_speed,
                                    wind_direction,
                                    rainfall_level,
                                    nearby_infected_plants,
                                )

                        with right_col:
                            if st.session_state.latest_pathogen_prediction:
                                pathogen_result = st.session_state.latest_pathogen_prediction
                                pathway_text = ", ".join(pathogen_result["pathways"])
                                st.metric("Spread Score", f"{pathogen_result['pressure_score']}%")
                                st.markdown(
                                    f"""
                                    <div class="disease-card">
                                        <h4>Pathogen Movement Preview</h4>
                                        <p><b>Pathogen profile:</b> {pathogen_result['pathogen_type']}</p>
                                        <p><b>Spread pressure:</b> {pathogen_result['pressure_band']}</p>
                                        <p><b>Likely movement zone:</b> {pathogen_result['likely_direction']}</p>
                                        <p><b>Main movement note:</b> {pathogen_result['movement_note']}</p>
                                        <p><b>Temperature effect:</b> {pathogen_result['temp_note']}</p>
                                        <p><b>Likely pathways:</b> {pathway_text}</p>
                                    </div>
                                    """,
                                    unsafe_allow_html=True,
                                )

                        if st.session_state.latest_pathogen_prediction:
                            pathogen_result = st.session_state.latest_pathogen_prediction
                            graph_left, graph_right = st.columns(2)
                            with graph_left:
                                st.markdown("##### Radar View")
                                st.plotly_chart(build_factor_radar(pathogen_result["factor_scores"]), use_container_width=True)
                            with graph_right:
                                st.markdown("##### Hotspot Grid")
                                st.plotly_chart(
                                    build_hotspot_grid(
                                        pathogen_result["input_snapshot"]["wind_direction"],
                                        st.session_state.get("pathogen_time_selector", 24),
                                        pathogen_result["pressure_score"],
                                    ),
                                    use_container_width=True,
                                )
                                time_hours = st.slider(
                                    "Spread Time Selector (hours)",
                                    6,
                                    72,
                                    24,
                                    step=6,
                                    key="pathogen_time_selector",
                                )
                    else:
                        st.info("Pathogen prediction is available only for diseased plants.")
            else:
                st.info("No detailed disease information found for this class.")
    else:
        st.info("Please upload a plant leaf image to get started.")

elif app_mode == "Prediction History":
    st.markdown(
        """
    <div class="main-header">
        <h1>Prediction History</h1>
        <p>Track predictions made in this session</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    history = st.session_state.prediction_history
    if not history:
        st.info("No predictions made yet.")
    else:
        st.markdown("### Prediction Log")
        for i, pred in enumerate(reversed(history), 1):
            status = "[Healthy]" if "healthy" in pred["class"].lower() else "[Diseased]"
            severity_str = ""
            if "severity" in pred:
                severity_str = f" | Severity: {pred['severity']} ({pred['affected_pct']}%)"
            title = f"{status} #{len(history)-i+1} | {pred['name']} | {pred['confidence']:.2f}%{severity_str} | {pred['timestamp']}"
            with st.expander(title):
                st.markdown(f"**Image:** {pred['image_name']}")
                st.markdown(f"**Prediction:** {pred['name']}")
                st.markdown(f"**Confidence:** {pred['confidence']:.2f}%")
                if "severity" in pred:
                    st.markdown(f"**Severity Level:** {pred['severity']}")
                    st.markdown(f"**Affected Area:** {pred['affected_pct']}%")

        if len(history) > 1:
            st.markdown("### Disease Distribution")
            disease_counts = {}
            for h in history:
                name = h["name"]
                disease_counts[name] = disease_counts.get(name, 0) + 1
            fig = px.pie(values=list(disease_counts.values()), names=list(disease_counts.keys()), hole=0.3)
            fig.update_layout(template="plotly_white", height=380)
            st.plotly_chart(fig, use_container_width=True)
