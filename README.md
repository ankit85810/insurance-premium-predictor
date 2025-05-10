## Insurance Premium Predictor

machine learning-powered web application( [link](https://insurance-premium-predictor-by-ankit.streamlit.app/) ) that predicts health insurance premiums based on personal, medical, and lifestyle factors.

## 📋 Overview

This application uses machine learning models to estimate health insurance premiums based on various factors including age, income, medical history, lifestyle choices, and more. The system employs separate models for young adults (≤25 years) and older adults to provide more accurate predictions tailored to different age groups.

## ✨ Features

- **Personalized Premium Prediction**: Get instant estimates based on your profile
- **Comprehensive Input Factors**: Considers 12+ variables including:
  - Demographics (age, gender, region)
  - Health indicators (BMI category, medical history)
  - Lifestyle factors (smoking status)
  - Financial aspects (income, dependents)
  - Genetic risk factors
- **Age-Specific Models**: Specialized prediction models for different age groups
- **User-Friendly Interface**: Clean, intuitive Streamlit interface

## 🛠️ Technical Architecture

The application consists of three main components:

1. **Frontend Interface** (`main.py`): Streamlit-based user interface for data collection
2. **Prediction Engine** (`prediction_helper.py`): Processes inputs and generates predictions
3. **ML Models** (`artifacts/`): Pre-trained regression models and scalers

### Model Details

- **Young Adult Model**: Specialized for users ≤25 years
- **Adult Model**: Optimized for users >25 years
- **Feature Scaling**: Age-specific scalers ensure accurate predictions across age ranges
- **Medical Risk Scoring**: Custom algorithm to quantify health risks based on medical history

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip package manager

### Installation

1. Clone the repository
git clone https://github.com/ankit85810/insurance-premium-predictor.git

```cd insurance-premium-predictor```


2. Install required dependencies
```
pip install -r requirements.txt
```



3. Run the application

```streamlit run main.py```


## 📊 How It Works

1. **Input Collection**: User provides personal, medical, and lifestyle information
2. **Feature Engineering**: Raw inputs are transformed into model-ready features
3. **Risk Calculation**: Medical conditions are converted to normalized risk scores
4. **Age-Based Routing**: User is directed to the appropriate age-specific model
5. **Prediction**: The model estimates the insurance premium
6. **Result Display**: Premium estimate is presented to the user

## 🔍 Input Variables

| Category | Variables |
|----------|-----------|
| Personal | Age, Gender, Marital Status, Dependants Count |
| Financial | Annual Income, Employment Type |
| Health | BMI Category, Medical Background, Genetic Risk Score |
| Lifestyle | Smoking Status |
| Insurance | Plan Type (Bronze/Silver/Gold) |
| Geographic | Region |

## 📁 Project Structure
```
insurance-premium-predictor/
├── main.py # Streamlit interface
├── prediction_helper.py # Prediction logic
├── requirements.txt # Dependencies
├── artifacts/ # Model files
│ ├── model_young.joblib # ML model for young adults
│ ├── model_rest.joblib # ML model for adults
│ ├── scaler_young.joblib # Feature scaler for young adults
│ └── scaler_rest.joblib # Feature scaler for adults
└── README.md # Documentation
```


## 🔧 Customization

To adapt the model for different regions or insurance systems:

1. Retrain models with region-specific data
2. Adjust the risk scoring algorithm in `get_medical_risk_score()`
3. Modify the plan types and their corresponding codes in `prepare_features()`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

