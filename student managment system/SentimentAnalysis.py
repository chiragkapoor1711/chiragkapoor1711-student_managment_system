# Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Import libraries


# Load dataset
data = pd.read_csv('cardekho.csv')

# Separate numeric and categorical columns
numeric_cols = data.select_dtypes(include=['number']).columns
categorical_cols = data.select_dtypes(include=['object']).columns

# Handle missing values
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())
data[categorical_cols] = data[categorical_cols].fillna(data[categorical_cols].mode().iloc[0])

# Verify there are no missing values
print(data.isnull().sum())


# Load dataset
data = pd.read_csv('cardekho.csv')

# Data preprocessing
# Replace missing values
data.fillna(data.median(), inplace=True)

# Feature Engineering
data['car_age'] = 2024 - data['year']
data.drop(['year'], axis=1, inplace=True)

# Separate features and target variable
X = data.drop('price', axis=1)
y = data['price']

# Identify categorical and numerical columns
cat_features = X.select_dtypes(include=['object']).columns
num_features = X.select_dtypes(include=['int64', 'float64']).columns

# Preprocessing pipeline
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), num_features),
        ('cat', OneHotEncoder(), cat_features)
    ])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model 1: Multiple Linear Regression
linear_model = Pipeline(steps=[('preprocessor', preprocessor),
                                ('model', LinearRegression())])

# Train Linear Regression model
linear_model.fit(X_train, y_train)
y_pred_lr = linear_model.predict(X_test)

# Evaluate Linear Regression model
print("Linear Regression Results")
print("MAE:", mean_absolute_error(y_test, y_pred_lr))
print("R-squared:", r2_score(y_test, y_pred_lr))

# Model 2: Random Forest Regressor
rf_model = Pipeline(steps=[('preprocessor', preprocessor),
                           ('model', RandomForestRegressor(n_estimators=100, random_state=42))])

# Train Random Forest model
rf_model.fit(X_train, y_train)
y_pred_rf = rf_model.predict(X_test)

# Evaluate Random Forest model
print("\nRandom Forest Results")
print("MAE:", mean_absolute_error(y_test, y_pred_rf))
print("R-squared:", r2_score(y_test, y_pred_rf))
