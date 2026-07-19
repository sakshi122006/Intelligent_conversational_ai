"""
Simple ML training scaffold for crime prediction using XGBoost.
This is a starting point — replace feature engineering with real features.
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import classification_report


def train_model(csv_path='data/crime_features.csv'):
    df = pd.read_csv(csv_path)
    X = df.drop(columns=['target'])
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
    model.fit(X_train, y_train)

    preds = model.predict(X_test)
    print(classification_report(y_test, preds))
    model.save_model('ml/trained_models/xgb_crime.model')

if __name__ == '__main__':
    train_model()
