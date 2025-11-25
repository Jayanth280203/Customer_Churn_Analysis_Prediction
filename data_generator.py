import pandas as pd
import numpy as np
import random

def generate_churn_data(num_samples=2000):
    np.random.seed(42)
    random.seed(42)

    data = {
        'CustomerID': [f'CUST_{i+1:04d}' for i in range(num_samples)],
        'Age': np.random.randint(18, 70, num_samples),
        'Gender': np.random.choice(['Male', 'Female'], num_samples),
        'Tenure': np.random.randint(1, 60, num_samples),  # Months
        'Usage Frequency': np.random.randint(1, 30, num_samples),  # Times per month
        'Support Calls': np.random.randint(0, 10, num_samples),
        'Payment Delay': np.random.randint(0, 30, num_samples),  # Days delayed on average
        'Subscription Type': np.random.choice(['Basic', 'Standard', 'Premium'], num_samples),
        'Total Spend': np.random.uniform(100, 5000, num_samples).round(2),
        'Last Purchase Days Ago': np.random.randint(1, 365, num_samples)
    }

    df = pd.DataFrame(data)

    # Logic to simulate Churn (Target Variable)
    # Higher support calls, payment delay, and low usage -> Higher chance of churn
    # Lower tenure -> Higher chance of churn
    
    churn_prob = np.zeros(num_samples)
    
    churn_prob += (df['Support Calls'] * 0.1)
    churn_prob += (df['Payment Delay'] * 0.05)
    churn_prob += np.where(df['Usage Frequency'] < 5, 0.3, 0)
    churn_prob += np.where(df['Tenure'] < 6, 0.2, 0)
    churn_prob -= (df['Total Spend'] / 10000) # High spenders less likely to churn
    
    # Normalize and add randomness
    churn_prob = (churn_prob - churn_prob.min()) / (churn_prob.max() - churn_prob.min())
    churn_prob += np.random.normal(0, 0.1, num_samples)
    
    # Threshold for churn
    df['Churn'] = (churn_prob > 0.55).astype(int)
    
    return df

if __name__ == "__main__":
    print("Generating synthetic data...")
    df = generate_churn_data()
    output_file = 'customer_churn_data.csv'
    df.to_csv(output_file, index=False)
    print(f"Data generated and saved to {output_file}")
    print(df.head())
    print("\nClass Distribution:")
    print(df['Churn'].value_counts(normalize=True))
