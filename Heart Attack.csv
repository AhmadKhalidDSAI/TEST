import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('Heart Attack.csv')

le = LabelEncoder()
df['class'] = le.fit_transform(df['class']) 

plt.figure(figsize=(7, 5))
sns.countplot(x='class', data=df, palette='pastel')
plt.title("Target Distribution (0: Negative, 1: Positive)", fontweight='bold')
plt.show()

plt.figure(figsize=(10, 8))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap", fontweight='bold')
plt.show()

X = df.drop('class', axis=1)
y = df['class']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

y_pred = model.predict(X_test_scaled)
print(f"Final Model Accuracy: {accuracy_score(y_test, y_pred)*100:.2f}%")
print("\nClassification Report:\n", classification_report(y_test, y_pred))

print("\n" + "="*40)
print("  PATIENT DIAGNOSIS SYSTEM")
print("="*40)

try:
    v_age      = float(input("Enter Age: "))
    v_gender   = int(input("Enter Gender (1 for Male, 0 for Female): "))
    v_impulse  = float(input("Enter Impulse (Heart Rate): "))
    v_p_high   = float(input("Enter Pressure High (Systolic): "))
    v_p_low    = float(input("Enter Pressure Low (Diastolic): "))
    v_glucose  = float(input("Enter Glucose level: "))
    v_kcm      = float(input("Enter KCM (Creatine Kinase): "))
    v_troponin = float(input("Enter Troponin level: "))

    new_patient = pd.DataFrame([[v_age, v_gender, v_impulse, v_p_high, v_p_low, v_glucose, v_kcm, v_troponin]], 
                               columns=['age', 'gender', 'impluse', 'pressurehight', 'pressurelow', 'glucose', 'kcm', 'troponin'])

    new_patient_scaled = scaler.transform(new_patient)

    result = model.predict(new_patient_scaled)
    prob = model.predict_proba(new_patient_scaled)

    print("\n" + "-"*30)
    if result[0] == 1:
        print(f"DIAGNOSIS: POSITIVE (Heart Attack Risk Detected)")
        print(f"Model Confidence: {prob[0][1]*100:.2f}%")
    else:
        print(f"DIAGNOSIS: NEGATIVE (No Heart Attack Detected)")
        print(f"Model Confidence: {prob[0][0]*100:.2f}%")
    print("-"*30)

except ValueError:
    print("\n[Error] Invalid input. Please enter numbers only.")