"""
Disease Information Database
Contains detailed information about all 38 plant disease classes
including descriptions, symptoms, treatments, and prevention measures.
"""

DISEASE_INFO = {
    'Apple___Apple_scab': {
        'plant': 'Apple',
        'disease': 'Apple Scab',
        'description': 'Apple scab is caused by the fungus Venturia inaequalis. It is one of the most common and serious diseases affecting apple trees worldwide.',
        'symptoms': 'Dark, olive-green to brown velvety spots on leaves. Infected leaves may curl, become distorted, and fall prematurely. Fruit develops dark, scabby lesions that crack as the fruit grows.',
        'treatment': '1. Apply fungicides (captan, myclobutanil) during spring.\n2. Remove and destroy fallen infected leaves.\n3. Prune trees to improve air circulation.\n4. Use copper-based sprays during dormant season.',
        'prevention': '1. Plant scab-resistant apple varieties.\n2. Maintain good sanitation by raking fallen leaves.\n3. Apply preventive fungicide sprays before infection periods.\n4. Ensure proper spacing between trees for air flow.'
    },
    'Apple___Black_rot': {
        'plant': 'Apple',
        'disease': 'Black Rot',
        'description': 'Black rot is caused by the fungus Botryosphaeria obtusa. It affects leaves, fruit, and bark of apple trees, and can cause significant economic losses.',
        'symptoms': 'Purple spots on upper leaf surfaces that enlarge and develop brown centers ("frog-eye" pattern). Fruit rot starts as small brown spots that enlarge into firm, black, rotting areas. Cankers form on branches and trunks.',
        'treatment': '1. Prune out all cankers and dead wood.\n2. Remove mummified fruit from trees and ground.\n3. Apply fungicide sprays (captan, thiophanate-methyl).\n4. Maintain tree vigor through proper fertilization.',
        'prevention': '1. Remove all dead wood and mummified fruits during winter.\n2. Avoid wounding trees during cultivation.\n3. Apply protective fungicides from bud break through harvest.\n4. Practice good orchard sanitation.'
    },
    'Apple___Cedar_apple_rust': {
        'plant': 'Apple',
        'disease': 'Cedar Apple Rust',
        'description': 'Cedar apple rust is caused by the fungus Gymnosporangium juniperi-virginianae. It requires two hosts to complete its life cycle: apple trees and eastern red cedar (juniper).',
        'symptoms': 'Bright yellow-orange spots on upper leaf surfaces in late spring. Spots enlarge and develop tiny black dots (spermogonia). Tube-like structures (aecia) form on the undersides of leaves.',
        'treatment': '1. Apply fungicide (myclobutanil, triadimefon) at bud break.\n2. Continue fungicide applications through early summer.\n3. Remove galls from nearby cedar trees during winter.\n4. Remove heavily infected leaves.',
        'prevention': '1. Plant rust-resistant apple varieties.\n2. Remove nearby cedar or juniper trees (within 2-3 miles if possible).\n3. Apply preventive fungicide sprays starting at bud break.\n4. Monitor trees regularly for early symptoms.'
    },
    'Apple___healthy': {
        'plant': 'Apple',
        'disease': 'Healthy',
        'description': 'This apple leaf is healthy with no signs of disease. The plant shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy leaves are uniformly green with no spots, discoloration, or deformities.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Maintain regular watering and fertilization schedule.\n2. Prune trees annually for good air circulation.\n3. Monitor regularly for early signs of disease.\n4. Apply preventive fungicide sprays as needed.'
    },
    'Blueberry___healthy': {
        'plant': 'Blueberry',
        'disease': 'Healthy',
        'description': 'This blueberry leaf is healthy with no signs of disease. The plant shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy leaves show vibrant green color with no spots or discoloration.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Maintain acidic soil pH (4.5-5.5).\n2. Provide adequate mulching.\n3. Ensure proper drainage.\n4. Monitor for pests and diseases regularly.'
    },
    'Cherry_(including_sour)___Powdery_mildew': {
        'plant': 'Cherry',
        'disease': 'Powdery Mildew',
        'description': 'Powdery mildew on cherry is caused by the fungus Podosphaera clandestina. It commonly affects sweet and sour cherry trees, especially young developing tissues.',
        'symptoms': 'White powdery coating on leaf surfaces, shoots, and sometimes fruit. Infected leaves may curl upward and become distorted. Severely affected leaves may turn yellow and drop prematurely.',
        'treatment': '1. Apply sulfur-based fungicides or potassium bicarbonate.\n2. Use systemic fungicides (myclobutanil, trifloxystrobin).\n3. Remove and destroy heavily infected shoots.\n4. Improve air circulation through pruning.',
        'prevention': '1. Plant resistant cherry varieties.\n2. Ensure proper spacing for air circulation.\n3. Avoid excessive nitrogen fertilization.\n4. Apply preventive fungicide sprays before symptoms appear.'
    },
    'Cherry_(including_sour)___healthy': {
        'plant': 'Cherry',
        'disease': 'Healthy',
        'description': 'This cherry leaf is healthy with no signs of disease. The plant shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy cherry leaves are smooth, glossy green without any spots or powdery residue.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Maintain proper irrigation.\n2. Prune regularly for good air circulation.\n3. Apply balanced fertilization.\n4. Monitor for early signs of disease.'
    },
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot': {
        'plant': 'Corn (Maize)',
        'disease': 'Cercospora Leaf Spot / Gray Leaf Spot',
        'description': 'Gray leaf spot is caused by the fungus Cercospora zeae-maydis. It is one of the most significant foliar diseases of corn, particularly in warm, humid environments.',
        'symptoms': 'Small, rectangular, tan to gray lesions that develop between leaf veins. Lesions are parallel-sided and can be 2-3 inches long. Severely infected leaves may appear entirely gray or brown.',
        'treatment': '1. Apply foliar fungicides (strobilurin, triazole-based).\n2. Time applications at tasseling or when disease first appears.\n3. Ensure adequate plant nutrition.\n4. Scout fields regularly for early detection.',
        'prevention': '1. Plant resistant corn hybrids.\n2. Practice crop rotation (avoid corn-on-corn).\n3. Reduce surface residue through tillage.\n4. Ensure proper plant spacing for air flow.'
    },
    'Corn_(maize)___Common_rust_': {
        'plant': 'Corn (Maize)',
        'disease': 'Common Rust',
        'description': 'Common rust is caused by the fungus Puccinia sorghi. It is a widespread foliar disease of corn that thrives in cool, humid conditions.',
        'symptoms': 'Small, elongated, reddish-brown to cinnamon-brown pustules on both leaf surfaces. Pustules are scattered across the leaf and may be circular to elongated. Severely infected leaves may yellow and die prematurely.',
        'treatment': '1. Apply fungicides (strobilurin, triazole) at early disease onset.\n2. Time fungicide applications at tasseling.\n3. Monitor weather conditions for disease-favorable periods.\n4. Ensure balanced plant nutrition.',
        'prevention': '1. Plant rust-resistant corn hybrids.\n2. Plant early to avoid peak rust infection periods.\n3. Destroy volunteer corn plants.\n4. Maintain adequate plant spacing.'
    },
    'Corn_(maize)___Northern_Leaf_Blight': {
        'plant': 'Corn (Maize)',
        'disease': 'Northern Leaf Blight',
        'description': 'Northern leaf blight (NLB) is caused by the fungus Exserohilum turcicum (formerly Helminthosporium turcicum). It is a common and potentially devastating foliar disease of corn.',
        'symptoms': 'Long, elliptical, grayish-green to tan lesions (1-6 inches) on leaves. Lesions typically appear first on lower leaves. In severe cases, entire leaves may be killed, reducing plant photosynthesis.',
        'treatment': '1. Apply foliar fungicides (propiconazole, azoxystrobin) at disease onset.\n2. Scout fields starting at V8 growth stage.\n3. Consider fungicide application if disease develops before tasseling.\n4. Maintain adequate plant nutrition.',
        'prevention': '1. Plant resistant hybrids with Ht genes.\n2. Practice crop rotation.\n3. Reduce corn residue through tillage.\n4. Ensure proper plant spacing and nutrition.'
    },
    'Corn_(maize)___healthy': {
        'plant': 'Corn (Maize)',
        'disease': 'Healthy',
        'description': 'This corn leaf is healthy with no signs of disease. The plant shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy corn leaves are uniformly green, upright, and free from spots or lesions.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Use quality seeds with disease resistance.\n2. Practice crop rotation.\n3. Maintain balanced soil fertility.\n4. Monitor fields regularly for pest and disease pressure.'
    },
    'Grape___Black_rot': {
        'plant': 'Grape',
        'disease': 'Black Rot',
        'description': 'Black rot is caused by the fungus Guignardia bidwellii. It is one of the most serious diseases of grapes in warm, humid climates.',
        'symptoms': 'Small, tan to brown circular spots on leaves with dark borders. Infected berries turn brown, then shrivel into hard, black, wrinkled mummies. Shoot lesions appear as dark, sunken cankers.',
        'treatment': '1. Apply fungicides (myclobutanil, mancozeb, captan) from bud break.\n2. Continue applications until berries begin to ripen.\n3. Remove and destroy all mummified fruit.\n4. Prune out infected canes during dormancy.',
        'prevention': '1. Remove mummified berries and infected debris.\n2. Prune vines to improve air circulation.\n3. Maintain a regular fungicide spray schedule.\n4. Plant in well-drained locations with good sun exposure.'
    },
    'Grape___Esca_(Black_Measles)': {
        'plant': 'Grape',
        'disease': 'Esca (Black Measles)',
        'description': 'Esca (Black Measles) is a complex wood disease caused by multiple fungi including Phaeomoniella chlamydospora and Phaeoacremonium spp. It affects the trunk and vascular system of grapevines.',
        'symptoms': 'Interveinal striping or "tiger stripe" pattern on leaves. Dark spots on berries resembling measles. Internal wood decay with dark streaks. In acute form, sudden vine wilting ("apoplexy") can occur.',
        'treatment': '1. Remove and destroy severely affected vines.\n2. Trunk renewal (retraining from suckers) for less severe cases.\n3. Protect pruning wounds with fungicide paste.\n4. Apply sodium arsenite (where legally permitted) or biocontrol agents.',
        'prevention': '1. Protect pruning wounds immediately after cutting.\n2. Prune during dry weather to reduce infection risk.\n3. Avoid large pruning wounds.\n4. Use certified disease-free planting material.'
    },
    'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)': {
        'plant': 'Grape',
        'disease': 'Leaf Blight (Isariopsis Leaf Spot)',
        'description': 'Grape leaf blight is caused by the fungus Pseudocercospora vitis (formerly Isariopsis clavispora). It primarily affects grape leaves, leading to premature defoliation.',
        'symptoms': 'Dark brown to reddish-brown irregular spots on leaves. Spots may coalesce and cover large areas. Severely infected leaves turn yellow and fall prematurely.',
        'treatment': '1. Apply fungicides (mancozeb, copper-based products).\n2. Remove and destroy infected leaves.\n3. Improve canopy management through pruning.\n4. Ensure adequate vine nutrition.',
        'prevention': '1. Practice good canopy management for air circulation.\n2. Avoid overhead irrigation.\n3. Apply preventive fungicide spray schedule.\n4. Remove fallen leaves and debris from vineyard floor.'
    },
    'Grape___healthy': {
        'plant': 'Grape',
        'disease': 'Healthy',
        'description': 'This grape leaf is healthy with no signs of disease. The vine shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy grape leaves are broad, lobed, and bright green with no spots or discoloration.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Maintain regular pruning and canopy management.\n2. Ensure proper irrigation and nutrition.\n3. Monitor for pests and diseases regularly.\n4. Practice good vineyard sanitation.'
    },
    'Orange___Haunglongbing_(Citrus_greening)': {
        'plant': 'Orange',
        'disease': 'Huanglongbing (Citrus Greening)',
        'description': 'Huanglongbing (HLB), also known as citrus greening, is caused by the bacterium Candidatus Liberibacter spp. It is spread by the Asian citrus psyllid and is considered the most devastating citrus disease worldwide.',
        'symptoms': 'Asymmetric blotchy yellowing of leaves (unlike uniform nutrient deficiency). Small, lopsided, bitter-tasting fruit with aborted seeds. Tree shows thinning canopy, dieback, and eventual decline.',
        'treatment': '1. No cure currently exists for HLB.\n2. Remove and destroy infected trees promptly.\n3. Control Asian citrus psyllid vector with insecticides.\n4. Apply enhanced nutrition programs to slow disease progression.',
        'prevention': '1. Use certified disease-free nursery stock.\n2. Implement psyllid management programs.\n3. Remove infected trees immediately.\n4. Report suspected cases to agricultural authorities.'
    },
    'Peach___Bacterial_spot': {
        'plant': 'Peach',
        'disease': 'Bacterial Spot',
        'description': 'Bacterial spot is caused by Xanthomonas arboricola pv. pruni. It affects leaves, fruit, and twigs of peach and other stone fruits.',
        'symptoms': 'Small, water-soaked spots on leaves that turn angular and brown. Severely affected leaves turn yellow and drop. Fruit develops sunken, dark spots that may crack. Twig cankers and defoliation.',
        'treatment': '1. Apply copper-based bactericides during dormant season.\n2. Use oxytetracycline sprays during the growing season.\n3. Remove severely infected branches.\n4. Maintain tree vigor through proper nutrition.',
        'prevention': '1. Plant resistant peach varieties.\n2. Avoid overhead irrigation.\n3. Ensure proper tree spacing for air circulation.\n4. Apply preventive copper sprays before bud break.'
    },
    'Peach___healthy': {
        'plant': 'Peach',
        'disease': 'Healthy',
        'description': 'This peach leaf is healthy with no signs of disease. The plant shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy peach leaves are elongated, dark green, and smooth without spots or holes.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Maintain regular pruning schedule.\n2. Apply balanced fertilization.\n3. Monitor for pests and diseases regularly.\n4. Ensure adequate drainage and irrigation.'
    },
    'Pepper,_bell___Bacterial_spot': {
        'plant': 'Bell Pepper',
        'disease': 'Bacterial Spot',
        'description': 'Bacterial spot of pepper is caused by several species of Xanthomonas. It is a major disease of pepper in warm, humid environments.',
        'symptoms': 'Small, water-soaked spots on leaves that become raised and brown. Leaves may yellow and drop. Fruit develops raised, blister-like spots that become rough and scabby.',
        'treatment': '1. Apply copper-based bactericides combined with mancozeb.\n2. Remove infected plant debris.\n3. Avoid working with plants when wet.\n4. Use disease-free transplants.',
        'prevention': '1. Use certified disease-free seeds and transplants.\n2. Practice crop rotation (3-year cycle).\n3. Avoid overhead irrigation.\n4. Maintain adequate plant spacing for air circulation.'
    },
    'Pepper,_bell___healthy': {
        'plant': 'Bell Pepper',
        'disease': 'Healthy',
        'description': 'This bell pepper leaf is healthy with no signs of disease. The plant shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy pepper leaves are broad, smooth, and vibrant green.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Maintain consistent watering.\n2. Apply balanced fertilization.\n3. Monitor for pests and diseases regularly.\n4. Practice crop rotation.'
    },
    'Potato___Early_blight': {
        'plant': 'Potato',
        'disease': 'Early Blight',
        'description': 'Early blight is caused by the fungus Alternaria solani. It is one of the most common diseases of potato and tomato, occurring worldwide.',
        'symptoms': 'Dark brown to black spots with concentric rings (target-like or "bull\'s-eye" pattern) on older leaves first. Spots may coalesce and cause leaf yellowing and drop. Tubers may develop dark, sunken lesions.',
        'treatment': '1. Apply fungicides (chlorothalonil, mancozeb, azoxystrobin).\n2. Begin applications when conditions favor disease.\n3. Remove infected plant material.\n4. Ensure adequate plant nutrition (especially potassium).',
        'prevention': '1. Practice crop rotation (3+ years).\n2. Plant resistant potato varieties.\n3. Avoid overhead irrigation.\n4. Space plants adequately for air circulation.'
    },
    'Potato___Late_blight': {
        'plant': 'Potato',
        'disease': 'Late Blight',
        'description': 'Late blight is caused by the oomycete Phytophthora infestans. This was the disease responsible for the Irish Potato Famine of the 1840s. It remains one of the most destructive plant diseases worldwide.',
        'symptoms': 'Water-soaked, dark green to brown irregular lesions on leaves, often starting at leaf tips or edges. White fuzzy mold growth on leaf undersides in humid conditions. Rapid plant death. Tubers develop firm, dark rotting areas.',
        'treatment': '1. Apply fungicides immediately (metalaxyl, chlorothalonil, mancozeb).\n2. Destroy infected plants to prevent spread.\n3. Harvest tubers promptly in dry conditions.\n4. Monitor weather for disease-favorable conditions.',
        'prevention': '1. Plant certified disease-free seed potatoes.\n2. Plant resistant varieties.\n3. Destroy volunteer potatoes and cull piles.\n4. Ensure good drainage and air circulation.\n5. Avoid overhead irrigation, especially in the evening.'
    },
    'Potato___healthy': {
        'plant': 'Potato',
        'disease': 'Healthy',
        'description': 'This potato leaf is healthy with no signs of disease. The plant shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy potato leaves are compound, dark green, and free from spots or lesions.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Use certified seed potatoes.\n2. Practice crop rotation.\n3. Maintain adequate soil moisture.\n4. Apply balanced fertilization and monitor for pests.'
    },
    'Raspberry___healthy': {
        'plant': 'Raspberry',
        'disease': 'Healthy',
        'description': 'This raspberry leaf is healthy with no signs of disease. The plant shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy raspberry leaves are compound with serrated edges, bright green on top and lighter underneath.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Maintain proper cane management and pruning.\n2. Ensure good air circulation.\n3. Water at the base, avoiding wetting foliage.\n4. Remove spent canes after harvest.'
    },
    'Soybean___healthy': {
        'plant': 'Soybean',
        'disease': 'Healthy',
        'description': 'This soybean leaf is healthy with no signs of disease. The plant shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy soybean leaves are trifoliate, bright green, and free from spots or discoloration.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Practice crop rotation.\n2. Use quality certified seeds.\n3. Maintain proper soil fertility.\n4. Monitor fields regularly for pests and diseases.'
    },
    'Squash___Powdery_mildew': {
        'plant': 'Squash',
        'disease': 'Powdery Mildew',
        'description': 'Powdery mildew on squash is caused by fungi Podosphaera xanthii or Erysiphe cichoracearum. It is one of the most common and widespread diseases of cucurbits.',
        'symptoms': 'White to grayish powdery fungal growth on upper leaf surfaces, stems, and petioles. Infected leaves may become yellow, curl, and die. Severely affected plants may have reduced fruit quality and yield.',
        'treatment': '1. Apply fungicides (sulfur, potassium bicarbonate, neem oil).\n2. Use systemic fungicides for severe infections.\n3. Remove heavily infected leaves.\n4. Apply biological control agents (Bacillus subtilis).',
        'prevention': '1. Plant resistant squash varieties.\n2. Ensure adequate plant spacing for air circulation.\n3. Avoid excessive nitrogen fertilization.\n4. Water at the base of plants, not overhead.'
    },
    'Strawberry___Leaf_scorch': {
        'plant': 'Strawberry',
        'disease': 'Leaf Scorch',
        'description': 'Leaf scorch of strawberry is caused by the fungus Diplocarpon earlianum. It is a common foliar disease that can weaken plants and reduce fruit yield.',
        'symptoms': 'Small, dark purple spots on upper leaf surfaces that enlarge and develop brown centers. Spots may merge, causing leaves to appear scorched. Infected leaves may dry out and curl upward.',
        'treatment': '1. Apply fungicides (captan, myclobutanil) during growing season.\n2. Remove and destroy infected leaves.\n3. Renovate strawberry beds after harvest.\n4. Maintain plant vigor through proper fertilization.',
        'prevention': '1. Plant resistant strawberry varieties.\n2. Ensure proper spacing between plants.\n3. Avoid overhead irrigation.\n4. Remove old, infected foliage during bed renovation.'
    },
    'Strawberry___healthy': {
        'plant': 'Strawberry',
        'disease': 'Healthy',
        'description': 'This strawberry leaf is healthy with no signs of disease. The plant shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy strawberry leaves are trifoliate with serrated edges, bright green, and glossy.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Maintain proper plant spacing.\n2. Apply balanced fertilization.\n3. Water at the base of plants.\n4. Renovate beds annually after harvest.'
    },
    'Tomato___Bacterial_spot': {
        'plant': 'Tomato',
        'disease': 'Bacterial Spot',
        'description': 'Bacterial spot of tomato is caused by several Xanthomonas species. It is a widespread disease in warm, humid environments that can cause significant yield losses.',
        'symptoms': 'Small, water-soaked, circular spots on leaves that become angular and dark brown. Spots may have a yellow halo. Fruit develops small, raised, scab-like spots. Severe infection causes defoliation.',
        'treatment': '1. Apply copper-based bactericides.\n2. Use copper + mancozeb combinations.\n3. Remove infected plant material.\n4. Avoid working with wet plants.',
        'prevention': '1. Use certified disease-free seeds and transplants.\n2. Practice crop rotation (2-3 years).\n3. Avoid overhead irrigation.\n4. Sanitize tools and equipment.'
    },
    'Tomato___Early_blight': {
        'plant': 'Tomato',
        'disease': 'Early Blight',
        'description': 'Early blight is caused by the fungus Alternaria solani. It is one of the most common tomato diseases, occurring in most regions where tomatoes are grown.',
        'symptoms': 'Dark brown to black spots with concentric rings (target-like pattern) on lower leaves first. Spots enlarge and may cause leaves to yellow and drop. Stem lesions appear as dark, sunken areas.',
        'treatment': '1. Apply fungicides (chlorothalonil, mancozeb, copper).\n2. Remove infected lower leaves.\n3. Maintain adequate plant nutrition.\n4. Stake or cage plants to improve air circulation.',
        'prevention': '1. Practice crop rotation (avoid planting tomatoes/potatoes in same area).\n2. Mulch around plants to prevent soil splash.\n3. Water at the base of plants.\n4. Plant resistant varieties when available.'
    },
    'Tomato___Late_blight': {
        'plant': 'Tomato',
        'disease': 'Late Blight',
        'description': 'Late blight is caused by the oomycete Phytophthora infestans. It can rapidly destroy tomato plants under cool, wet conditions.',
        'symptoms': 'Large, water-soaked, grayish-green areas on leaves that turn brown and papery. White fuzzy mold on leaf undersides. Dark brown firm spots on fruit. Plants can be killed within days.',
        'treatment': '1. Apply fungicides immediately (chlorothalonil, mancozeb, metalaxyl).\n2. Destroy infected plants completely (burn or bag).\n3. Harvest any unaffected fruit.\n4. Do not compost infected material.',
        'prevention': '1. Plant resistant varieties.\n2. Ensure good air circulation.\n3. Avoid overhead watering.\n4. Destroy volunteer tomato and potato plants.\n5. Monitor weather forecasts for disease-favorable conditions.'
    },
    'Tomato___Leaf_Mold': {
        'plant': 'Tomato',
        'disease': 'Leaf Mold',
        'description': 'Leaf mold is caused by the fungus Passalora fulva (formerly Cladosporium fulvum). It primarily affects tomatoes grown in greenhouses or high-tunnel conditions.',
        'symptoms': 'Pale green to yellowish spots on upper leaf surfaces. Olive-green to grayish-brown velvety mold on leaf undersides. Infected leaves may curl, wilt, and drop. Fruit infection is rare but possible.',
        'treatment': '1. Improve greenhouse ventilation.\n2. Apply fungicides (chlorothalonil, mancozeb).\n3. Reduce humidity through proper watering practices.\n4. Remove and destroy infected leaves.',
        'prevention': '1. Plant resistant tomato varieties.\n2. Maintain greenhouse humidity below 85%.\n3. Ensure proper plant spacing and air circulation.\n4. Avoid wetting foliage during watering.'
    },
    'Tomato___Septoria_leaf_spot': {
        'plant': 'Tomato',
        'disease': 'Septoria Leaf Spot',
        'description': 'Septoria leaf spot is caused by the fungus Septoria lycopersici. It is one of the most destructive foliar diseases of tomatoes worldwide.',
        'symptoms': 'Small, circular spots (1/16 to 1/8 inch) with dark brown borders and gray centers on lower leaves first. Tiny black dots (pycnidia) visible in spot centers. Severe infection leads to extensive defoliation.',
        'treatment': '1. Apply fungicides (chlorothalonil, mancozeb, copper).\n2. Remove infected lower leaves promptly.\n3. Apply fungicides at 7-10 day intervals during wet weather.\n4. Destroy infected plant debris at end of season.',
        'prevention': '1. Practice crop rotation (at least 3 years).\n2. Mulch around plants.\n3. Water at the base of plants.\n4. Stake plants for better air circulation.\n5. Avoid overhead irrigation.'
    },
    'Tomato___Spider_mites Two-spotted_spider_mite': {
        'plant': 'Tomato',
        'disease': 'Spider Mites (Two-Spotted Spider Mite)',
        'description': 'Two-spotted spider mites (Tetranychus urticae) are tiny arachnids that feed on plant sap. They thrive in hot, dry conditions and can reproduce rapidly.',
        'symptoms': 'Fine stippling (tiny white/yellow dots) on upper leaf surfaces. Leaves may become bronzed, dry, brittle. Fine webbing on leaf undersides and between leaves. Severe infestations cause leaf drop and plant decline.',
        'treatment': '1. Spray plants with strong jets of water to dislodge mites.\n2. Apply miticides (abamectin, spiromesifen).\n3. Use horticultural oils or insecticidal soap.\n4. Release predatory mites (Phytoseiulus persimilis) as biological control.',
        'prevention': '1. Maintain adequate plant hydration.\n2. Avoid dusty conditions around plants.\n3. Avoid broad-spectrum insecticides that kill natural predators.\n4. Inspect plants regularly, especially during hot, dry weather.'
    },
    'Tomato___Target_Spot': {
        'plant': 'Tomato',
        'disease': 'Target Spot',
        'description': 'Target spot is caused by the fungus Corynespora cassiicola. It affects leaves, stems, and fruit of tomato plants, particularly in warm, humid conditions.',
        'symptoms': 'Small, round, brown spots with concentric rings (target-like appearance) on leaves. Spots may enlarge and merge, causing significant leaf blight. Fruit develops sunken, dark spots near the stem.',
        'treatment': '1. Apply fungicides (chlorothalonil, mancozeb, azoxystrobin).\n2. Remove infected plant material.\n3. Improve air circulation through pruning.\n4. Apply fungicides at 7-14 day intervals during favorable conditions.',
        'prevention': '1. Practice crop rotation.\n2. Use resistant varieties when available.\n3. Maintain proper plant spacing.\n4. Avoid overhead irrigation.\n5. Remove plant debris from previous crops.'
    },
    'Tomato___Tomato_Yellow_Leaf_Curl_Virus': {
        'plant': 'Tomato',
        'disease': 'Tomato Yellow Leaf Curl Virus (TYLCV)',
        'description': 'TYLCV is a devastating viral disease transmitted by whiteflies (Bemisia tabaci). It is one of the most destructive tomato diseases in tropical and subtropical regions.',
        'symptoms': 'Upward curling and cupping of leaves. Yellowing of leaf margins. Stunted plant growth. Flower drop and significantly reduced fruit production. Plants infected early may be completely unproductive.',
        'treatment': '1. No cure exists for virus-infected plants.\n2. Remove and destroy infected plants immediately.\n3. Control whitefly vector with insecticides (imidacloprid, pyriproxyfen).\n4. Use yellow sticky traps to monitor whitefly populations.',
        'prevention': '1. Plant resistant tomato varieties.\n2. Use reflective mulches to repel whiteflies.\n3. Install fine-mesh insect screens in greenhouses.\n4. Implement whitefly management programs.\n5. Remove weeds that may harbor the virus.'
    },
    'Tomato___Tomato_mosaic_virus': {
        'plant': 'Tomato',
        'disease': 'Tomato Mosaic Virus (ToMV)',
        'description': 'Tomato mosaic virus is a highly stable and persistent virus that can survive on surfaces and in soil for extended periods. It spreads through mechanical transmission (contaminated hands, tools).',
        'symptoms': 'Mosaic pattern of light and dark green areas on leaves. Leaf distortion, curling, and reduced leaf size. Stunted plant growth. Fruit may show uneven ripening, internal browning, or yellow rings.',
        'treatment': '1. No cure exists for virus-infected plants.\n2. Remove and destroy infected plants.\n3. Disinfect all tools and hands with milk solution or 10% bleach.\n4. Do not compost infected plant material.',
        'prevention': '1. Plant resistant tomato varieties (with Tm-2 gene).\n2. Use certified virus-free seeds.\n3. Wash hands thoroughly before handling plants.\n4. Disinfect tools regularly.\n5. Avoid tobacco use near tomato plants (TMV can be in tobacco).'
    },
    'Tomato___healthy': {
        'plant': 'Tomato',
        'disease': 'Healthy',
        'description': 'This tomato leaf is healthy with no signs of disease. The plant shows normal growth characteristics.',
        'symptoms': 'No disease symptoms. Healthy tomato leaves are compound, bright green, and may have a slight fuzzy texture with a characteristic tomato smell.',
        'treatment': 'No treatment required. Continue regular care and maintenance.',
        'prevention': '1. Practice crop rotation.\n2. Maintain consistent watering (avoid over/under watering).\n3. Stake or cage plants for support.\n4. Monitor for early signs of pests and diseases.\n5. Apply balanced fertilization.'
    }
}


def get_disease_info(class_name):
    """Get disease information for a given class name."""
    return DISEASE_INFO.get(class_name, None)


def get_disease_name(class_name):
    """Get a human-readable disease name from the class name."""
    info = DISEASE_INFO.get(class_name)
    if info:
        return f"{info['plant']} - {info['disease']}"
    return class_name.replace('___', ' - ').replace('_', ' ')


# ═══════════════════════════════════════════════════════════════════════
# SEVERITY LEVEL ANALYSIS
# ═══════════════════════════════════════════════════════════════════════

SEVERITY_LEVELS = {
    'Mild': {
        'range': (0, 15),
        'color': '#4caf50',       # Green
        'icon': '[MILD]',
        'urgency': 'Low',
        'description': 'Early stage infection with minimal spread. The disease affects less than 15% of the visible leaf area.',
        'action': 'Monitor the plant closely over the next few days. Apply preventive measures and light treatment.',
        'treatment_approach': [
            '1. Remove only the most visibly affected leaves.',
            '2. Apply organic/mild fungicide or bactericide as a first measure.',
            '3. Improve air circulation around the plant.',
            '4. Adjust watering practices — avoid wetting foliage.',
            '5. Re-inspect after 5-7 days to check if the disease has progressed.'
        ]
    },
    'Moderate': {
        'range': (15, 35),
        'color': '#ff9800',       # Orange
        'icon': '[MOD]',
        'urgency': 'Medium',
        'description': 'The disease has spread noticeably, affecting 15-35% of the leaf area. Prompt action is recommended.',
        'action': 'Begin targeted treatment immediately. The disease is progressing and needs intervention.',
        'treatment_approach': [
            '1. Remove and destroy all visibly infected leaves and plant parts.',
            '2. Apply appropriate chemical fungicide/bactericide at recommended dosage.',
            '3. Treat surrounding healthy plants preventively.',
            '4. Improve growing conditions (spacing, ventilation, drainage).',
            '5. Apply treatment every 7-10 days until symptoms subside.',
            '6. Consider soil treatment if the pathogen is soil-borne.'
        ]
    },
    'Severe': {
        'range': (35, 60),
        'color': '#f44336',       # Red
        'icon': '[SEV]',
        'urgency': 'High',
        'description': 'Significant disease spread covering 35-60% of the leaf area. Aggressive treatment is required to save the plant.',
        'action': 'Urgent treatment needed. The disease is at an advanced stage and threatens plant survival.',
        'treatment_approach': [
            '1. Remove and destroy ALL infected leaves, branches, and plant debris immediately.',
            '2. Apply systemic fungicide/bactericide at maximum recommended dosage.',
            '3. Treat the entire plant, not just affected areas.',
            '4. Isolate the affected plant from healthy plants if possible.',
            '5. Apply treatment every 5-7 days aggressively.',
            '6. Consider soil drenching with appropriate fungicide.',
            '7. Boost plant immunity with potassium-rich fertilizer.',
            '8. If no improvement in 2 weeks, consider removing the plant to protect others.'
        ]
    },
    'Critical': {
        'range': (60, 100),
        'color': '#b71c1c',       # Dark Red
        'icon': '[CRIT]',
        'urgency': 'Very High',
        'description': 'The disease has spread extensively, covering more than 60% of the leaf area. The plant is at high risk of death.',
        'action': 'Emergency intervention required. Consider whether the plant can be saved or should be removed.',
        'treatment_approach': [
            '1. EVALUATE: Assess whether the plant can realistically be saved.',
            '2. If salvageable: Apply the strongest available systemic treatment immediately.',
            '3. Remove and BURN (do not compost) all infected material.',
            '4. Isolate the plant completely from all other plants.',
            '5. Apply intensive treatment every 3-5 days.',
            '6. If NOT salvageable: Remove and destroy the entire plant to prevent spread.',
            '7. Treat the soil where the plant was located.',
            '8. Monitor all nearby plants for signs of infection for the next 30 days.',
            '9. Do NOT replant the same species in that location for at least one season.'
        ]
    }
}


def analyze_severity(image):
    """
    Analyze disease severity from a leaf image using color-based segmentation.

    This function estimates the percentage of the leaf area that appears
    diseased by analyzing color deviations from healthy green tissue.

    Algorithm:
    1. Convert image to HSV color space
    2. Create a mask for "healthy green" leaf pixels
    3. Create a mask for the entire leaf (non-background)
    4. Calculate the ratio of non-green (diseased) to total leaf area
    5. Map the ratio to a severity level

    Args:
        image: PIL Image object

    Returns:
        dict with keys: level, percentage, color, icon, severity_info
    """
    import numpy as np

    # Resize for consistent analysis
    img = image.convert("RGB").resize((256, 256))
    img_array = np.array(img, dtype=np.float32)

    # Convert RGB to HSV manually (to avoid OpenCV dependency)
    r, g, b = img_array[:,:,0]/255.0, img_array[:,:,1]/255.0, img_array[:,:,2]/255.0

    cmax = np.maximum(np.maximum(r, g), b)
    cmin = np.minimum(np.minimum(r, g), b)
    diff = cmax - cmin

    # Hue calculation
    h = np.zeros_like(cmax)
    mask_r = (cmax == r) & (diff != 0)
    mask_g = (cmax == g) & (diff != 0)
    mask_b = (cmax == b) & (diff != 0)
    h[mask_r] = (60 * ((g[mask_r] - b[mask_r]) / diff[mask_r]) + 360) % 360
    h[mask_g] = (60 * ((b[mask_g] - r[mask_g]) / diff[mask_g]) + 120) % 360
    h[mask_b] = (60 * ((r[mask_b] - g[mask_b]) / diff[mask_b]) + 240) % 360

    # Saturation
    s = np.where(cmax == 0, 0, diff / cmax)

    # Value
    v = cmax

    # Leaf mask: exclude very dark (background) and very bright white (background)
    leaf_mask = (v > 0.15) & (v < 0.95) & (s > 0.08)

    # Healthy green mask: hue in green range (60-170 degrees), decent saturation
    healthy_mask = leaf_mask & (h >= 55) & (h <= 170) & (s > 0.15) & (v > 0.2)

    total_leaf_pixels = np.sum(leaf_mask)

    if total_leaf_pixels == 0:
        # If can't detect leaf, return mild by default
        affected_pct = 5.0
    else:
        healthy_pixels = np.sum(healthy_mask)
        affected_pct = max(0, (1 - healthy_pixels / total_leaf_pixels) * 100)

        # Clamp to reasonable range
        affected_pct = min(affected_pct, 95.0)

    # Determine severity level
    severity_level = 'Mild'
    for level, info in SEVERITY_LEVELS.items():
        low, high = info['range']
        if low <= affected_pct < high:
            severity_level = level
            break
    else:
        if affected_pct >= 60:
            severity_level = 'Critical'

    severity_info = SEVERITY_LEVELS[severity_level]

    return {
        'level': severity_level,
        'percentage': round(affected_pct, 1),
        'color': severity_info['color'],
        'icon': severity_info['icon'],
        'urgency': severity_info['urgency'],
        'description': severity_info['description'],
        'action': severity_info['action'],
        'treatment_approach': severity_info['treatment_approach']
    }
