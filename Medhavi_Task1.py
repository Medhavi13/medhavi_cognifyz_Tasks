import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('C:\\Users\\medhavi\\Downloads\\Dataset .csv')

data['Cuisines'].fillna(data['Cuisines'].mode()[0], inplace=True)

features = data[['Country Code', 'City', 'Cuisines', 'Average Cost for two', 'Has Table booking', 
                 'Has Online delivery', 'Price range', 'Votes']]
target = data['Aggregate rating']

numerical_features = ['Average Cost for two', 'Price range', 'Votes']
categorical_features = ['Country Code', 'City', 'Cuisines', 'Has Table booking', 'Has Online delivery']

numerical_transformer = SimpleImputer(strategy='median')
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_features),
        ('cat', categorical_transformer, categorical_features)
    ])

X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', LinearRegression())])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

regressor = model.named_steps['regressor']
preprocessor = model.named_steps['preprocessor']

encoded_feature_names = preprocessor.named_transformers_['cat']['onehot'].get_feature_names_out(categorical_features)

feature_names = numerical_features + list(encoded_feature_names)

coefficients = regressor.coef_

coefficients_df = pd.DataFrame({'Feature': feature_names, 'Coefficient': coefficients})

coefficients_df = coefficients_df.reindex(coefficients_df['Coefficient'].abs().sort_values(ascending=False).index)

print(coefficients_df.head(10)) 