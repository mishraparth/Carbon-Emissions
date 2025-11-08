# Carbon Emissions Predictor
4-weeks Shell-Edunet Skills4Future Internship (Oct 2025 - Nov 2025)

---
##  Project Status: 30% Completed

The Carbon Emissions Predictor is currently in its early development phase. So far, the following milestones have been achieved:

### Completed Tasks
- **Data Ingestion**: Loaded and explored a 10,000-row dataset on global energy consumption
- **Feature Engineering**: Dropped non-predictive columns (`Country`, `Year`) and selected key predictors
- **Data Cleaning**: Verified no missing values across selected features
- **Scaling**: Applied `StandardScaler` to normalize input features
- **Target Isolation**: Defined `Carbon Emissions (Million Tons)` as the prediction target

### Current Focus
- Designing the input-output flow for model prediction
- Preparing training-ready datasets
- Exploring regression models for baseline performance

### What this Model Will Do
"To build and train a high-accuracy Gradient Boosting model (R² 0.65) to predict a country's 'Carbon Intensity' (CO₂ per TWh) by engineering advanced features from its national energy profile."

---
##  Project Status: 60% Completed

The Carbon Emissions Predictor is now in its advanced development phase. Core modeling is complete, with smart feature engineering, simulated population and GDP, and a shift to predicting carbon intensity for better accuracy. Gradient Boosting has been implemented and evaluated, and a reusable prediction function is working. Visualizations for model performance and feature importance are also done.

###  Completed
- Feature engineering + simulated features
- Carbon intensity as target (log-transformed)
- Gradient Boosting model trained and evaluated
- Prediction function + visualizations

### In Progress
- Streamlit app for interactive input and live predictions

---

