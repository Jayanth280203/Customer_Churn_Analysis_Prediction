import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.preprocessing import StandardScaler

def run_analysis():
    print("Loading data...")
    df = pd.read_csv('customer_churn_data.csv')
    
    # 1. Preprocessing
    print("Preprocessing data...")
    # Drop CustomerID for modeling
    X = df.drop(['CustomerID', 'Churn'], axis=1)
    y = df['Churn']
    
    # Encode categorical variables
    X = pd.get_dummies(X, drop_first=True)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # 2. Modeling
    print("Training Random Forest Model...")
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train_scaled, y_train)
    
    # 3. Evaluation
    print("Evaluating model...")
    y_pred = rf.predict(X_test_scaled)
    print("\nAccuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    
    # 4. Feature Importance
    feature_importances = pd.DataFrame(rf.feature_importances_,
                                       index = X.columns,
                                       columns=['importance']).sort_values('importance', ascending=False)
    print("\nTop 5 Important Features:\n", feature_importances.head())
    
    # Save Feature Importance Plot
    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_importances.importance, y=feature_importances.index)
    plt.title('Feature Importance')
    plt.tight_layout()
    plt.savefig('feature_importance.png')
    print("Feature importance plot saved to feature_importance.png")

    # 5. Export for Dashboard
    print("Generating export for dashboard...")
    # We want to export the full dataset with predictions
    # First, prepare the full dataset for prediction
    X_full = pd.get_dummies(df.drop(['CustomerID', 'Churn'], axis=1), drop_first=True)
    # Align columns with training data (in case some categories were missing in split, though unlikely with this data)
    X_full = X_full.reindex(columns=X.columns, fill_value=0)
    X_full_scaled = scaler.transform(X_full)
    
    # Predict probabilities
    probs = rf.predict_proba(X_full_scaled)[:, 1]
    
    # Add to original dataframe
    export_df = df.copy()
    export_df['Churn_Probability'] = probs.round(4)
    export_df['Predicted_Churn'] = (probs > 0.5).astype(int)
    
    # Define Risk Levels
    conditions = [
        (export_df['Churn_Probability'] < 0.3),
        (export_df['Churn_Probability'] >= 0.3) & (export_df['Churn_Probability'] < 0.7),
        (export_df['Churn_Probability'] >= 0.7)
    ]
    choices = ['Low Risk', 'Medium Risk', 'High Risk']
    export_df['Risk_Level'] = np.select(conditions, choices, default='Unknown')
    
    export_df.to_csv('churn_dashboard_data.csv', index=False)
    print("Dashboard data exported to churn_dashboard_data.csv")

if __name__ == "__main__":
    run_analysis()
