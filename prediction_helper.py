import pandas as pd
import joblib

# Load serialized models and scalers
young_model = joblib.load("artifacts/model_young.joblib")
adult_model = joblib.load("artifacts/model_rest.joblib")
young_scaler = joblib.load("artifacts/scaler_young.joblib")
adult_scaler = joblib.load("artifacts/scaler_rest.joblib")

def get_medical_risk_score(history_str):
    """Assign a normalized risk score based on medical history string."""
    risk_map = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }
    # Split history string and compute risk
    conditions = history_str.lower().split(" & ")
    total_score = sum(risk_map.get(cond, 0) for cond in conditions)
    # Maximum possible score: heart disease (8) + diabetes/high BP (6)
    max_possible = 14
    normalized_score = total_score / max_possible
    return normalized_score

def prepare_features(user_input):
    """Convert user input dictionary into model-ready DataFrame."""
    # All expected feature columns
    columns = [
        'age', 'number_of_dependants', 'income_lakhs', 'insurance_plan', 'genetical_risk', 'normalized_risk_score',
        'gender_Male', 'region_Northwest', 'region_Southeast', 'region_Southwest', 'marital_status_Unmarried',
        'bmi_category_Obesity', 'bmi_category_Overweight', 'bmi_category_Underweight', 'smoking_status_Occasional',
        'smoking_status_Regular', 'employment_status_Salaried', 'employment_status_Self-Employed'
    ]
    plan_code = {'Bronze': 1, 'Silver': 2, 'Gold': 3}
    features = pd.DataFrame(0, columns=columns, index=[0])

    # Map dictionary values to DataFrame columns
    for key, val in user_input.items():
        if key == 'Gender' and val == 'Male':
            features['gender_Male'] = 1
        elif key == 'Region':
            if val in ['Northwest', 'Southeast', 'Southwest']:
                features[f'region_{val}'] = 1
        elif key == 'Marital Status' and val == 'Unmarried':
            features['marital_status_Unmarried'] = 1
        elif key == 'BMI Category':
            if val in ['Obesity', 'Overweight', 'Underweight']:
                features[f'bmi_category_{val}'] = 1
        elif key == 'Smoking Status':
            if val in ['Occasional', 'Regular']:
                features[f'smoking_status_{val}'] = 1
        elif key == 'Employment Status':
            if val in ['Salaried', 'Self-Employed']:
                features[f'employment_status_{val}'] = 1
        elif key == 'Insurance Plan':
            features['insurance_plan'] = plan_code.get(val, 1)
        elif key == 'Age':
            features['age'] = val
        elif key == 'Number of Dependants':
            features['number_of_dependants'] = val
        elif key == 'Income in Lakhs':
            features['income_lakhs'] = val
        elif key == 'Genetical Risk':
            features['genetical_risk'] = val

    # Calculate normalized risk score from medical history
    features['normalized_risk_score'] = get_medical_risk_score(user_input['Medical History'])

    # Apply scaling to numerical features
    features = scale_features(user_input['Age'], features)
    return features

def scale_features(age_value, df):
    """Scale age and income features according to age group."""
    scaler_bundle = young_scaler if age_value <= 25 else adult_scaler
    scale_columns = scaler_bundle['cols_to_scale']
    scaler = scaler_bundle['scaler']
    # Add dummy column if required by scaler
    df['income_level'] = 0
    df[scale_columns] = scaler.transform(df[scale_columns])
    df.drop('income_level', axis=1, inplace=True)
    return df

def make_prediction(user_input):
    """Generate prediction using appropriate model based on age."""
    feature_df = prepare_features(user_input)
    if user_input['Age'] <= 25:
        result = young_model.predict(feature_df)
    else:
        result = adult_model.predict(feature_df)
    return int(result[0])
