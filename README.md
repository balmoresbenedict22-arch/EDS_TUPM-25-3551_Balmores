ENV-01: Thermal Inversion & CO Trapping (Search: "Global Air Pollution")  
Author: Benedict Balmores  
Topic: Air Quality Index Prediction using Machine Learning  

---

Overview  
This repository contains a full Python machine learning pipeline that analyzes air pollution data and predicts Air Quality Index (AQI) categories using features such as CO, Ozone, NO2, and PM2.5 levels. The project includes data cleaning, visualization, model training, evaluation, prediction, and automatic saving of outputs.

---

Structure  
main.py: Core pipeline (data loading, cleaning, visualization, training, evaluation, prediction)  
src/: Modular Python scripts for ML workflow  
data/: Raw and cleaned datasets  
outputs/: Generated graphs, animations, reports, and trained model  
README.md: Project documentation  
requirements.txt: Required Python libraries  

---

Run Instructions  
1. Clone the repository  
2. Install dependencies:  
   pip install -r requirements.txt  
3. Place dataset in:  
   data/raw/global air pollution dataset.csv  
4. Run the project:  
   python main.py  
5. Outputs will be saved automatically in the outputs/ folder  

---

Features  
- Loads and cleans air pollution dataset  
- Saves cleaned dataset automatically  
- Generates static and animated graphs  
- Trains machine learning model for AQI prediction  
- Evaluates model accuracy  
- Predicts AQI category from new input data  
- Saves trained model and reports automatically  

---

Outputs  
- data/processed/dataset_cleaned.csv  
- outputs/graphs/histogram.png  
- outputs/graphs/co_aqi_animation.gif  
- outputs/graphs/pm25_animation.gif  
- outputs/models/air_pollution_model.pkl  
- outputs/reports/report.txt  

---

Sample Input  
CO AQI Value: 25  
Ozone AQI Value: 30  
NO2 AQI Value: 15  
PM2.5 AQI Value: 40  

Prediction Output  
AQI Category: Moderate  

---

Requirements  
- Python 3.8+  
- pandas  
- numpy  
- matplotlib  
- scikit-learn  
- joblib  
- pillow  

---

License  
This project is for educational purposes only.
