# ============================================================
# VITAFUEL
# AI CALORIE & FITNESS ASSISTANT
# ============================================================

import json
from pathlib import Path

import streamlit as st


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="VitaFuel | AI Calorie & Fitness",
    page_icon="🥗",
    layout="wide"
)


# ============================================================
# FILE STORAGE
# ============================================================

DATA_FILE = Path("vitafuel_data.json")


# ============================================================
# DEFAULT DATA
# ============================================================

DEFAULT_DATA = {
    "profile": {
        "age": 30,
        "gender": "Female",
        "height": 165.0,
        "weight": 65.0,
        "activity": 1.55,
        "goal": 0
    },

    "foods": [],

    "exercises": []
}


# ============================================================
# LOAD DATA
# ============================================================

def load_data():

    if not DATA_FILE.exists():

        return DEFAULT_DATA.copy()

    try:

        with open(DATA_FILE, "r", encoding="utf-8") as file:

            data = json.load(file)

        return data

    except Exception:

        return DEFAULT_DATA.copy()


# ============================================================
# SAVE DATA
# ============================================================

def save_data(data):

    with open(DATA_FILE, "w", encoding="utf-8") as file:

        json.dump(
            data,
            file,
            indent=4
        )


# ============================================================
# INITIALIZE SESSION
# ============================================================

if "data" not in st.session_state:

    st.session_state.data = load_data()


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_profile():

    return st.session_state.data["profile"]


def get_foods():

    return st.session_state.data["foods"]


def get_exercises():

    return st.session_state.data["exercises"]


def format_number(value):

    return f"{value:,.0f}"


# ============================================================
# CALORIE CALCULATION
# ============================================================

def calculate_calories(profile):

    age = profile["age"]

    gender = profile["gender"]

    height = profile["height"]

    weight = profile["weight"]

    activity = profile["activity"]

    goal = profile["goal"]


    # Mifflin-St Jeor equation

    if gender == "Male":

        bmr = (
            (10 * weight)
            + (6.25 * height)
            - (5 * age)
            + 5
        )

    else:

        bmr = (
            (10 * weight)
            + (6.25 * height)
            - (5 * age)
            - 161
        )


    tdee = bmr * activity

    target = max(
        1200,
        tdee + goal
    )


    bmi = weight / ((height / 100) ** 2)


    return bmr, tdee, target, bmi


# ============================================================
# FOOD DATA
# ============================================================

FOODS = {

    # name: calories, protein, carbs, fat

    "🍚 Rice": (130, 3, 28, 0.3),

    "🫓 Roti": (120, 3.5, 18, 4),

    "🫓 Paratha": (180, 4, 30, 5),

    "🥞 Dosa": (210, 4, 32, 7),

    "🥞 Idli": (160, 4, 30, 3),

    "🥣 Poha": (190, 5, 30, 6),

    "🥣 Upma": (220, 6, 35, 7),

    "🫘 Chole": (250, 8, 30, 10),

    "🫘 Rajma": (230, 9, 28, 8),

    "🍛 Dal": (210, 7, 30, 7),

    "🥔 Aloo Sabzi": (190, 5, 25, 8),

    "🍛 Paneer Curry": (170, 5, 18, 9),

    "🥚 Egg": (72, 6.3, 0.4, 4.8),

    "🍗 Chicken": (165, 31, 0, 3.6),

    "🐟 Fish": (208, 22, 0, 13),

    "🧀 Paneer": (120, 22, 0, 7),

    "🥛 Milk": (140, 6, 9, 5),

    "🍌 Banana": (105, 1.3, 27, 0.4),

    "🍎 Apple": (95, 0.5, 25, 0.3),

    "🍊 Orange": (62, 0.8, 15, 0.2),

    "🍉 Watermelon": (60, 0.6, 15, 0.2),

    "🥭 Mango": (69, 0.7, 18, 0.2),

    "🍇 Grapes": (68, 0.7, 18, 0.3),

    "🍓 Strawberry": (50, 0.4, 13, 0.2),

    "🍍 Pineapple": (100, 1.1, 26, 0.3),

    "🥣 Oats": (150, 5, 27, 3),

    "🍞 Bread": (80, 2, 15, 1),

    "🥣 Cornflakes": (120, 4, 22, 2),

    "🥪 Sandwich": (180, 6, 25, 7),

    "🥜 Peanuts": (160, 6, 14, 10),

    "🌰 Almonds": (170, 6, 6, 15),

    "🍿 Popcorn": (90, 3, 15, 2),

    "🍪 Biscuits": (150, 2, 20, 7),

    "🍟 French Fries": (210, 3, 25, 11),

    "🧃 Orange Juice": (90, 1, 22, 0),

    "☕ Milk Tea": (120, 4, 20, 3),

    "☕ Coffee": (100, 3, 15, 3)
}


# ============================================================
# EXERCISE DATA
# ============================================================

EXERCISES = {

    "🚶 Walking": 3.5,

    "🏃 Running": 9.8,

    "🚴 Cycling": 7.5,

    "🏊 Swimming": 8.0,

    "🪢 Skipping": 11.0,

    "🧘 Yoga": 3.0,

    "🏋️ Strength Training": 5.0,

    "💃 Dancing": 5.5,

    "🔥 HIIT": 8.0
}


# ============================================================
# CALCULATE FOOD TOTALS
# ============================================================

def calculate_food_totals():

    total_calories = 0

    protein = 0

    carbs = 0

    fat = 0


    for food in get_foods():

        total_calories += food["calories"]

        protein += food["protein"]

        carbs += food["carbs"]

        fat += food["fat"]


    return (
        total_calories,
        protein,
        carbs,
        fat
    )


# ============================================================
# CALCULATE EXERCISE TOTALS
# ============================================================

def calculate_exercise_totals():

    total_burned = 0

    total_minutes = 0


    for exercise in get_exercises():

        total_burned += exercise["calories"]

        total_minutes += exercise["duration"]


    return (
        total_burned,
        total_minutes
    )


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 48px;
        font-weight: 900;
        color: #163d5b;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #66788a;
        margin-bottom: 30px;
    }

    .metric-card {
        background-color: white;
        padding: 25px;
        border-radius: 18px;
        border: 1px solid #e1e9ef;
        box-shadow: 0 5px 20px rgba(24,58,82,0.07);
    }

    .metric-title {
        color: #66788a;
        font-size: 14px;
        font-weight: 700;
    }

    .metric-value {
        color: #163d5b;
        font-size: 32px;
        font-weight: 900;
    }

    .section-title {
        color: #163d5b;
        font-size: 30px;
        font-weight: 900;
    }

    .success-box {
        padding: 12px;
        border-radius: 10px;
        background-color: #e9f9d7;
        color: #4e7900;
        font-weight: 700;
    }

    .warning-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #fff5d8;
        color: #664b15;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.markdown(
        "# vita**fuel** ✦"
    )

    st.markdown(
        "### AI Calorie & Fitness Assistant"
    )

    st.divider()

    page = st.radio(
        "Navigate",
        [
            "🏠 Home",
            "👤 Profile",
            "🍎 Nutrition",
            "🏃 Exercise",
            "📊 Dashboard",
            "🤖 AI Prediction",
            "ℹ️ About"
        ]
    )

    st.divider()

    st.caption(
        "Your data is stored locally in "
        "`vitafuel_data.json`."
    )


# ============================================================
# HOME
# ============================================================

if page == "🏠 Home":

    st.markdown(
        '<div class="main-title">'
        'Understand your daily energy.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="main-title">'
        'Build healthier habits.'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="subtitle">
        VitaFuel helps you estimate daily calorie needs,
        track food intake, monitor exercise and understand
        your energy balance through simple data science.
        </div>
        """,
        unsafe_allow_html=True
    )


    profile = get_profile()

    bmr, tdee, target, bmi = calculate_calories(profile)

    food_total, protein, carbs, fat = (
        calculate_food_totals()
    )

    burned, minutes = (
        calculate_exercise_totals()
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Daily Target",
            f"{format_number(target)} kcal"
        )


    with col2:

        st.metric(
            "Food Intake",
            f"{format_number(food_total)} kcal"
        )


    with col3:

        st.metric(
            "Calories Burned",
            f"{format_number(burned)} kcal"
        )


    with col4:

        remaining = max(
            0,
            target - food_total + burned
        )

        st.metric(
            "Remaining",
            f"{format_number(remaining)} kcal"
        )


    st.divider()


    st.markdown(
        '<div class="section-title">'
        'Everything in one place'
        '</div>',
        unsafe_allow_html=True
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.info(
            "### ◌ Personal Target\n"
            "Calculate BMI, BMR, TDEE and "
            "your calorie target."
        )


    with col2:

        st.success(
            "### 🍎 Food Tracker\n"
            "Track multiple foods and macros."
        )


    with col3:

        st.warning(
            "### 🏃 Exercise Burn\n"
            "Add multiple exercises and "
            "calculate total calories burned."
        )


    with col4:

        st.info(
            "### ✦ AI Prediction\n"
            "Use machine-learning models "
            "for calorie prediction."
        )


# ============================================================
# PROFILE
# ============================================================

elif page == "👤 Profile":

    st.markdown(
        '<div class="section-title">'
        '👤 My Profile'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Your profile is automatically saved. "
        "You do not need to create it again "
        "when reopening the app."
    )


    profile = get_profile()


    with st.form("profile_form"):

        col1, col2 = st.columns(2)


        with col1:

            age = st.number_input(
                "Age",
                min_value=10,
                max_value=100,
                value=int(profile["age"])
            )


            gender = st.selectbox(
                "Gender",
                [
                    "Female",
                    "Male"
                ],
                index=(
                    0
                    if profile["gender"] == "Female"
                    else 1
                )
            )


            height = st.number_input(
                "Height (cm)",
                min_value=100.0,
                max_value=250.0,
                value=float(profile["height"])
            )


        with col2:

            weight = st.number_input(
                "Weight (kg)",
                min_value=25.0,
                max_value=300.0,
                value=float(profile["weight"])
            )


            activity_options = {

                "Sedentary": 1.2,

                "Lightly Active": 1.375,

                "Moderately Active": 1.55,

                "Very Active": 1.725,

                "Extremely Active": 1.9
            }


            activity_names = list(
                activity_options.keys()
            )


            current_activity = min(
                activity_names,
                key=lambda name:
                abs(
                    activity_options[name]
                    - profile["activity"]
                )
            )


            activity_name = st.selectbox(
                "Activity Level",
                activity_names,
                index=activity_names.index(
                    current_activity
                )
            )


            goal_options = {

                "Weight Loss": -450,

                "General Fitness": 0,

                "Weight Maintenance": 0,

                "Weight Gain": 300
            }


            goal_name = st.selectbox(
                "Fitness Goal",
                list(goal_options.keys())
            )


        submitted = st.form_submit_button(
            "💾 Save Profile",
            use_container_width=True
        )


    if submitted:

        st.session_state.data["profile"] = {

            "age": int(age),

            "gender": gender,

            "height": float(height),

            "weight": float(weight),

            "activity":
                activity_options[activity_name],

            "goal":
                goal_options[goal_name]
        }


        save_data(
            st.session_state.data
        )


        st.success(
            "✓ Profile saved successfully!"
        )


        st.rerun()


    st.divider()


    bmr, tdee, target, bmi = calculate_calories(
        get_profile()
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "BMI",
            f"{bmi:.1f}"
        )


    with col2:

        st.metric(
            "BMR",
            f"{format_number(bmr)} kcal"
        )


    with col3:

        st.metric(
            "TDEE",
            f"{format_number(tdee)} kcal"
        )


    with col4:

        st.metric(
            "Daily Target",
            f"{format_number(target)} kcal"
        )


    st.divider()


    if st.button(
        "🗑️ Clear Saved Profile",
        type="secondary"
    ):

        st.session_state.data["profile"] = (
            DEFAULT_DATA["profile"].copy()
        )


        save_data(
            st.session_state.data
        )


        st.success(
            "Saved profile has been cleared."
        )


        st.rerun()


# ============================================================
# NUTRITION
# ============================================================

elif page == "🍎 Nutrition":

    st.markdown(
        '<div class="section-title">'
        '🍎 Food & Nutrition'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Add as many foods as you want to "
        "build your daily food log."
    )


    col1, col2, col3 = st.columns(3)


    with col1:

        food_name = st.selectbox(
            "Food",
            list(FOODS.keys())
        )


    with col2:

        quantity = st.number_input(
            "Quantity / Servings",
            min_value=0.1,
            value=1.0,
            step=0.1
        )


    with col3:

        meal = st.selectbox(
            "Meal",
            [
                "Breakfast",
                "Lunch",
                "Dinner",
                "Snack"
            ]
        )


    if st.button(
        "➕ Add Food",
        use_container_width=True
    ):

        calories, protein, carbs, fat = (
            FOODS[food_name]
        )


        new_food = {

            "name": food_name,

            "meal": meal,

            "quantity": quantity,

            "calories":
                calories * quantity,

            "protein":
                protein * quantity,

            "carbs":
                carbs * quantity,

            "fat":
                fat * quantity
        }


        st.session_state.data[
            "foods"
        ].append(new_food)


        save_data(
            st.session_state.data
        )


        st.success(
            f"{food_name} added successfully!"
        )


        st.rerun()


    st.divider()


    foods = get_foods()


    if len(foods) == 0:

        st.info(
            "No foods added yet."
        )

    else:

        st.subheader(
            "Today's Food Log"
        )


        for index, food in enumerate(foods):

            col1, col2, col3 = st.columns(
                [5, 2, 1]
            )


            with col1:

                st.write(
                    f"**{food['name']}**"
                )

                st.caption(
                    f"{food['meal']} • "
                    f"{food['quantity']} serving(s)"
                )


            with col2:

                st.write(
                    f"**{format_number(food['calories'])} kcal**"
                )


            with col3:

                if st.button(
                    "Remove",
                    key=f"remove_food_{index}"
                ):

                    st.session_state.data[
                        "foods"
                    ].pop(index)


                    save_data(
                        st.session_state.data
                    )


                    st.rerun()


    st.divider()


    total_calories, protein, carbs, fat = (
        calculate_food_totals()
    )


    st.subheader(
        "Today's Nutrition"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Calories",
            f"{format_number(total_calories)} kcal"
        )


    with col2:

        st.metric(
            "Protein",
            f"{protein:.0f} g"
        )


    with col3:

        st.metric(
            "Carbohydrates",
            f"{carbs:.0f} g"
        )


    with col4:

        st.metric(
            "Fat",
            f"{fat:.0f} g"
        )


    profile = get_profile()

    bmr, tdee, target, bmi = calculate_calories(
        profile
    )


    percentage = 0


    if target > 0:

        percentage = (
            total_calories /
            target
        ) * 100


    percentage = min(
        100,
        max(0, percentage)
    )


    st.progress(
        percentage / 100
    )


    st.write(
        f"{percentage:.0f}% of your estimated "
        "daily target"
    )


# ============================================================
# EXERCISE
# ============================================================

elif page == "🏃 Exercise":

    st.markdown(
        '<div class="section-title">'
        '🏃 Exercise & Calories Burned'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Add multiple exercises. "
        "All exercises are stored and their "
        "calories are added together."
    )


    profile = get_profile()

    weight = profile["weight"]


    col1, col2 = st.columns(2)


    with col1:

        exercise_name = st.selectbox(
            "Exercise",
            list(EXERCISES.keys())
        )


    with col2:

        duration = st.number_input(
            "Duration (minutes)",
            min_value=1,
            value=30,
            step=1
        )


    if st.button(
        "➕ Add Exercise",
        use_container_width=True
    ):

        met = EXERCISES[
            exercise_name
        ]


        calories = (
            met
            * 3.5
            * weight
            / 200
            * duration
        )


        new_exercise = {

            "name": exercise_name,

            "met": met,

            "duration": duration,

            "calories": calories
        }


        st.session_state.data[
            "exercises"
        ].append(new_exercise)


        save_data(
            st.session_state.data
        )


        st.success(
            f"{exercise_name} added!"
        )


        st.rerun()


    st.divider()


    exercises = get_exercises()


    if len(exercises) == 0:

        st.info(
            "No exercises added yet."
        )

    else:

        st.subheader(
            "Today's Exercise Log"
        )


        for index, exercise in enumerate(
            exercises
        ):

            col1, col2, col3 = st.columns(
                [5, 2, 1]
            )


            with col1:

                st.write(
                    f"**{exercise['name']}**"
                )

                st.caption(
                    f"{exercise['duration']} minutes"
                )


            with col2:

                st.write(
                    f"🔥 **{format_number(exercise['calories'])} kcal**"
                )


            with col3:

                if st.button(
                    "Remove",
                    key=f"remove_exercise_{index}"
                ):

                    st.session_state.data[
                        "exercises"
                    ].pop(index)


                    save_data(
                        st.session_state.data
                    )


                    st.rerun()


    st.divider()


    total_burned, total_minutes = (
        calculate_exercise_totals()
    )


    col1, col2 = st.columns(2)


    with col1:

        st.metric(
            "🔥 Total Calories Burned",
            f"{format_number(total_burned)} kcal"
        )


    with col2:

        st.metric(
            "Total Exercise Time",
            f"{total_minutes} minutes"
        )


    st.info(
        "Calories burned are estimates based "
        "on MET value, body weight and duration."
    )


# ============================================================
# DASHBOARD
# ============================================================

elif page == "📊 Dashboard":

    st.markdown(
        '<div class="section-title">'
        '📊 Today\'s Dashboard'
        '</div>',
        unsafe_allow_html=True
    )


    profile = get_profile()


    bmr, tdee, target, bmi = calculate_calories(
        profile
    )


    food_total, protein, carbs, fat = (
        calculate_food_totals()
    )


    burned, minutes = (
        calculate_exercise_totals()
    )


    remaining = max(
        0,
        target -
        food_total +
        burned
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.metric(
            "Daily Target",
            f"{format_number(target)} kcal"
        )


    with col2:

        st.metric(
            "Food Intake",
            f"{format_number(food_total)} kcal"
        )


    with col3:

        st.metric(
            "Calories Burned",
            f"{format_number(burned)} kcal"
        )


    with col4:

        st.metric(
            "Remaining",
            f"{format_number(remaining)} kcal"
        )


    st.divider()


    st.subheader(
        "Energy Balance"
    )


    balance = (
        target -
        food_total +
        burned
    )


    if balance > 0:

        st.success(
            f"You have approximately "
            f"{format_number(balance)} kcal "
            "remaining."
        )

    else:

        st.warning(
            "Your estimated daily target has "
            "been reached."
        )


    st.divider()


    col1, col2 = st.columns(2)


    with col1:

        st.subheader(
            "Profile Summary"
        )


        st.write(
            f"**Age:** {profile['age']}"
        )

        st.write(
            f"**Gender:** {profile['gender']}"
        )

        st.write(
            f"**Height:** {profile['height']} cm"
        )

        st.write(
            f"**Weight:** {profile['weight']} kg"
        )

        st.write(
            f"**BMI:** {bmi:.1f}"
        )

        st.write(
            f"**BMR:** {format_number(bmr)} kcal"
        )

        st.write(
            f"**TDEE:** {format_number(tdee)} kcal"
        )


    with col2:

        st.subheader(
            "Today's Activity"
        )


        st.write(
            f"🍎 Food: "
            f"**{format_number(food_total)} kcal**"
        )

        st.write(
            f"🔥 Burned: "
            f"**{format_number(burned)} kcal**"
        )

        st.write(
            f"🏃 Exercises: "
            f"**{len(get_exercises())}**"
        )

        st.write(
            f"⏱️ Exercise Time: "
            f"**{minutes} minutes**"
        )

        st.write(
            f"🥚 Protein: "
            f"**{protein:.0f} g**"
        )

        st.write(
            f"🍚 Carbohydrates: "
            f"**{carbs:.0f} g**"
        )

        st.write(
            f"🥑 Fat: "
            f"**{fat:.0f} g**"
        )


# ============================================================
# AI PREDICTION
# ============================================================

elif page == "🤖 AI Prediction":

    st.markdown(
        '<div class="section-title">'
        '🤖 AI Calories Prediction'
        '</div>',
        unsafe_allow_html=True
    )


    st.write(
        "This section is prepared for your "
        "machine-learning calorie prediction model."
    )


    st.info(
        """
        Your final data-science project can use:

        • Linear Regression

        • Random Forest Regression

        • MAE

        • RMSE

        • R² Score
        """
    )


    st.subheader(
        "Prediction Inputs"
    )


    profile = get_profile()


    col1, col2, col3 = st.columns(3)


    with col1:

        prediction_weight = st.number_input(
            "Weight (kg)",
            min_value=25.0,
            max_value=300.0,
            value=float(
                profile["weight"]
            )
        )


    with col2:

        prediction_duration = st.number_input(
            "Exercise Duration (minutes)",
            min_value=1,
            value=30
        )


    with col3:

        prediction_exercise = st.selectbox(
            "Exercise Type",
            list(EXERCISES.keys())
        )


    if st.button(
        "🤖 Predict Calories",
        use_container_width=True
    ):

        met = EXERCISES[
            prediction_exercise
        ]


        prediction = (
            met
            * 3.5
            * prediction_weight
            / 200
            * prediction_duration
        )


        st.success(
            f"Estimated Calories Burned: "
            f"{format_number(prediction)} kcal"
        )


    st.divider()


    st.subheader(
        "Machine Learning Model"
    )


    st.write(
        """
        For the final ML version, train your model
        using your calorie dataset and save it as
        a `.pkl` or `.joblib` file.

        The model can then be loaded using:

        `joblib.load("calorie_model.pkl")`
        """
    )


# ============================================================
# ABOUT
# ============================================================

elif page == "ℹ️ About":

    st.markdown(
        '<div class="section-title">'
        'ℹ️ About VitaFuel'
        '</div>',
        unsafe_allow_html=True
    )


    st.write(
        """
        VitaFuel is a data-science based wellness
        application that combines:

        • Calorie estimation

        • Nutrition tracking

        • Exercise tracking

        • BMI calculation

        • BMR calculation

        • TDEE calculation

        • Machine learning

        • Data analysis
        """
    )


    st.subheader(
        "Technologies"
    )


    col1, col2, col3, col4 = st.columns(4)


    with col1:

        st.info(
            "**Python**"
        )


    with col2:

        st.info(
            "**Streamlit**"
        )


    with col3:

        st.info(
            "**Pandas / NumPy**"
        )


    with col4:

        st.info(
            "**Scikit-learn**"
        )


    st.divider()


    st.warning(
        """
        IMPORTANT DISCLAIMER

        Calorie, BMI, BMR, TDEE, nutrition and
        exercise values shown by this application
        are estimates.

        Food values can vary depending on ingredients,
        preparation method and serving size.

        VitaFuel is intended for educational and
        general wellness purposes and is not a
        substitute for professional medical,
        nutritional or fitness advice.
        """
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "vitaFUEL ✦ | AI Calorie & Fitness Companion | "
    "Data Science & Machine Learning Project"
)