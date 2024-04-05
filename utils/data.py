crop_idx = {
    1: 'rice',
    2: 'maize',
    3: 'chickpea',
    4: 'kidneybeans',
    5: 'pigeonpeas',
    6: 'mothbeans',
    7: 'mungbean',
    8: 'blackgram',
    9: 'lentil',
    10: 'pomegranate',
    11: 'banana',
    12: 'mango',
    13: 'grapes',
    14: 'watermelon',
    15: 'muskmelon',
    16: 'apple',
    17: 'orange',
    18: 'papaya',
    19: 'coconut',
    20: 'cotton',
    21: 'jute',
    22: 'coffee'
}


crop_url = {
    'rice' : 'https://images.cnbctv18.com/wp-content/uploads/2023/07/Rice-2.jpg',
    'maize' : 'https://seed2plant.in/cdn/shop/products/maizeseeds.jpg?v=1604034397',
    'chickpea' : 'https://media.post.rvohealth.io/wp-content/uploads/2021/10/chickpeas-732x549-thumbnail-732x549.jpg',
    'kidneybeans' : 'https://media.istockphoto.com/id/1863013813/photo/dried-raw-red-beans-in-a-bowl.webp?b=1&s=170667a&w=0&k=20&c=TY4zeXBm8iK415Rk-IlXTGxNeV7vGQ0laPPPQa8a8uQ=',
    'pigeonpeas' : 'https://5.imimg.com/data5/SELLER/Default/2021/11/HW/CP/XB/10888193/pigeon-pea-seeds.jpg',
    'mothbeans' : 'https://www.poshtik.in/cdn/shop/products/Moth_Dal_Poshtik_grande.jpg?v=1565272395',
    'mungbean' : 'https://www.cookingwithcamilla.com/wp-content/uploads/2022/11/whole-green-mung-beans-1x1-2369.jpg',
    'blackgram' : 'https://www.shutterstock.com/image-photo/fresh-black-gram-udad-clay-600nw-2077914544.jpg',
    'lentil' : 'https://www.keepingthepeas.com/wp-content/uploads/2022/11/red-lentils-in-wood-bowl.jpg',
    'pomegranate' : 'https://insanelygoodrecipes.com/wp-content/uploads/2023/02/Cut-Opened-Ripe-Pomegranate-on-Wood-Plate.jpg',
    'banana' : 'https://www.forbesindia.com/media/images/2022/Sep/img_193773_banana.jpg',
    'mango' : 'https://img.etimg.com/thumb/width-640,height-480,imgsize-105444,resizemode-75,msid-91803294/small-biz/trade/exports/insights/a-heat-waves-lamented-victim-the-mango-indias-king-of-fruits/mango-stock.jpg',
    'grapes' : 'https://images.pexels.com/photos/9556561/pexels-photo-9556561.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1',
    'watermelon' : 'https://hips.hearstapps.com/hmg-prod/images/fresh-ripe-watermelon-slices-on-wooden-table-royalty-free-image-1684966820.jpg',
    'muskmelon' : 'https://www.healthshots.com/wp-content/uploads/2020/04/muskmelon.jpg',
    'apple' : 'https://images.everydayhealth.com/images/diet-nutrition/apples-101-about-1440x810.jpg',
    'orange' : 'https://www.heythattastesgood.com/wp-content/uploads/2022/06/orange-fruits.jpg',
    'papaya' : 'https://draxe.com/wp-content/uploads/2018/11/DrAxePapayaBenefitsHeader.jpg',
    'coconut' : 'https://cdn11.bigcommerce.com/s-i52r9dz4cm/products/1780/images/1382/CO-635_Coconut_Oil__47403.1581876884.500.750.jpg?c=2',
    'cotton' : 'https://imgix-prod.sgs.com/-/media/sgscorp/images/natural-resources/cotton-plant.cdn.en-IN.1.jpg?fit=crop&crop=edges&auto=format&w=1200&h=630',
    'jute' : 'https://researchoutreach.org/wp-content/uploads/2021/05/shutterstock_1340391350.jpg',
    'coffee' : 'https://5.imimg.com/data5/SELLER/Default/2021/8/AP/WL/GJ/5504430/roasted-coffee-beans-500x500.jpg'
}


fertilizer_data = {
    'NHigh': """<h3>The N value of soil is <span>high</span> and might give rise to weeds.</h3>
            <h5>Please consider the following suggestions:</h5>
            <ul>
                <li><i> Manure </i> – adding manure is one of the simplest ways to amend your soil with nitrogen. Be careful
                as there are various types of manures with varying degrees of nitrogen.</li>
                
                <li><i>Coffee grinds </i> – use your morning addiction to feed your gardening habit! Coffee grinds are considered
                a green compost material which is rich in nitrogen. Once the grounds break down, your soil will be fed with delicious,
                delicious nitrogen. An added benefit to including coffee grounds to your soil is while it will compost, it will also
                help provide increased drainage to your soil.</li>
                
                <li><i>Plant nitrogen fixing plants</i> – planting vegetables that are in Fabaceae family like peas, beans and
                soybeans have the ability to increase nitrogen in your soil.</li>
                
                <li>Plant ‘green manure’ crops like cabbage, corn and brocolli.</li>
                
                <li><i>Use mulch (wet grass) while growing crops</i> - Mulch can also include sawdust and scrap soft woods.</li>
            </ul>""",

    'Nlow': """<h3>The N value of your soil is <Span>low</Span>.</h3>
            <h5>Please consider the following suggestions:</h5>
            <ul>
                <li><i>Add sawdust or fine woodchips to your soil</i> – the carbon in the
                sawdust/woodchips love nitrogen and will help absorb and soak up and excess nitrogen.</li>

                <li><i>Plant heavy nitrogen feeding plants</i> – tomatoes, corn, broccoli, cabbage and spinach
                are examples of plants that thrive off nitrogen and will suck the nitrogen dry.</li>

                <li><i>Water</i> – soaking your soil with water will help leach the nitrogen deeper into your
                soil, effectively leaving less for your plants to use.</li>

                <li><i>Sugar</i> – In limited studies, it was shown that adding sugar to your soil can help
                potentially reduce the amount of nitrogen is your soil. Sugar is partially composed of 
                carbon, an element which attracts and soaks up the nitrogen in the soil. This is similar 
                concept to adding sawdust/woodchips which are high in carbon content.</li>

                <li>Add composted manure to the soil.</li>

                <li>Plant Nitrogen fixing plants like peas or beans.</li>

                <li><i>Use NPK fertilizers with high N value.</li>

                <li><i>Do nothing</i> – It may seem counter-intuitive, but if you already have plants that are producing 
                lots of foliage, it may be best to let them continue to absorb all the nitrogen to amend the soil for
                your next crops.</li>
            </ul>""",

    'PHigh': """<h3>The P value of your soil is <span>high</span>.</h3>
            <h5>Please consider the following suggestions:</h5>
            <ul>
                <li><i>Avoid adding manure</i> – manure contains many key nutrients for your soil but typically including
                high levels of phosphorous. Limiting the addition of manure will help reduce phosphorus being added.</li>
                
                <li><i>Use only phosphorus-free fertilizer</i> – if you can limit the amount of phosphorous added to your soil, you
                can let the plants use the existing phosphorus while still providing other key nutrients such as Nitrogen and Potassium.
                Find a fertilizer with numbers such as 10-0-10, where the zero represents no phosphorous.</li>
                
                <li><i>Water your soil</i> – soaking your soil liberally will aid in driving phosphorous out of the soil. This is
                recommended as a last ditch effort.</li>
                
                <li>Plant nitrogen fixing vegetables to increase nitrogen without increasing phosphorous (like beans and peas).</li>
                    
                <li>Use crop rotations to decrease high phosphorous levels.</li>
            </ul>""",

    'Plow': """<h3>The P value of your soil is <span>low</span>.</h3>
            <h5>Please consider the following suggestions:</h5>
            <ul>
                <li><i>Bone meal</i> – a fast acting source that is made from ground animal bones which is rich in
                phosphorous.</li>
                
                <li><i>Rock phosphate</i> – a slower acting source where the soil needs to convert the rock phosphate into
                phosphorous that the plants can use.</li>
                
                <li><i>Phosphorus Fertilizers</i> – applying a fertilizer with a high phosphorous content in the NPK ratio
                (example: 10-20-10, 20 being phosphorous percentage).</li>
                
                <li><i>Organic compost</i> – adding quality organic compost to your soil will help increase phosphorous content.</li>
                
                <li><i>Manure</i> – as with compost, manure can be an excellent source of phosphorous for your plants.</li>
                
                <li><i>Clay soil</i> – introducing clay particles into your soil can help retain & fix phosphorus deficiencies.</li>
                
                <li><i>Ensure proper soil pH</i> – having a pH in the 6.0 to 7.0 range has been scientifically proven to have the
                optimal phosphorus uptake in plants.</li>
                
                <li>If soil pH is low, add lime or potassium carbonate to the soil as fertilizers. Pure calcium carbonate is very
                effective in increasing the pH value of the soil.</li>
                
                <li>If pH is high, addition of appreciable amount of organic matter will help acidify the soil. Application of
                acidifying fertilizers, such as ammonium sulfate, can help lower soil pH.</li>
            </ul>""",

    'KHigh': """<h3>The K value of your soil is <span>high</span>.</h3>
            <h5>Please consider the following suggestions:</h5>
            <ul>
                <li><i>Loosen the soil</i> deeply with a shovel, and water thoroughly to dissolve water-soluble potassium.
                Allow the soil to fully dry, and repeat digging and watering the soil two or three more times.
                
                <li><i>Sift through the soil</i>, and remove as many rocks as possible, using a soil sifter. Minerals occurring in
                rocks such as mica and feldspar slowly release potassium into the soil slowly through weathering.
                
                <li>Stop applying potassium-rich commercial fertilizer. Apply only commercial fertilizer that has a '0' in the
                final number field. Commercial fertilizers use a three number system for measuring levels of nitrogen, phosphorous and
                potassium. The last number stands for potassium. Another option is to stop using commercial fertilizers all together and
                to begin using only organic matter to enrich the soil.
                
                <li>Mix crushed eggshells, crushed seashells, wood ash or soft rock phosphate to the soil to add calcium. Mix in up
                to 10 percent of organic compost to help amend and balance the soil.
                
                <li>Use NPK fertilizers with low K levels and organic fertilizers since they have low NPK values.
                
                <li>Grow a cover crop of legumes that will fix nitrogen in the soil. This practice will meet the soil’s needs for
                nitrogen without increasing phosphorus or potassium.
            </ul>""",

    'Klow': """<h3>The K value of your soil is <span>low</span>.</h3>
                    <h5>Please consider the following suggestions:</h5>
                    <ul>
                        <li>Mix in muricate of potash or sulphate of potash.</li>
                        <li>Try kelp meal or seaweed.</li>
                        <li>Try Sul-Po-Mag.</li>
                        <li>Bury banana peels an inch below the soils surface.</li>
                        <li>Use Potash fertilizers since they contain high values potassium.</li>
                    </ul>"""
}