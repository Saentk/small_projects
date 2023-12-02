import pandas as pd
import statsmodels.api as sm
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from scipy import stats

# Load the data from an xlsx file
data = pd.read_excel('Data_oil.xlsx', index_col=0)
data = data.fillna(data.mean())

independent_variables = ["oil_cons_usa", "oil_prod_usa", "share_pipelines", "gdp_real_usa", "pop_usa", "cpi_all_usa", "ir_usa", "employed_usa", "unemploy_rate_usa"]

for variable in independent_variables:
    plt.scatter(data[variable], data['oil_price_br'])
    plt.xlabel(variable)
    plt.ylabel('oil_price_br')
    plt.title(f'oil_price_br vs {variable}')
    plt.show()

X = data[independent_variables]
y = data['oil_price_br']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R2 Score: {r2}')

# Test the significance of the model and each independent variable
X2 = sm.add_constant(X)
est = sm.OLS(y, X2)
est2 = est.fit()
print(est2.summary())


# Identify significant independent variables (p-value < 0.05)
significant_variables = est2.pvalues[est2.pvalues < 0.05].index[1:]

# Develop a new multiple regression equation
X_sig = data[significant_variables]
y_sig = data['oil_price_br']

X_train_sig, X_test_sig, y_train_sig, y_test_sig = train_test_split(X_sig, y_sig, test_size=0.2, random_state=42)
model_sig = LinearRegression()
model_sig.fit(X_train_sig, y_train_sig)

y_pred_sig = model_sig.predict(X_test_sig)
mse_sig = mean_squared_error(y_test_sig, y_pred_sig)
r2_sig = r2_score(y_test_sig, y_pred_sig)
print(f'Mean Squared Error: {mse_sig}')
print(f'R2 Score: {r2_sig}')

# Test the significance of the new model and each significant independent variable
X2_sig = sm.add_constant(X_sig)
est_sig = sm.OLS(y_sig, X2_sig)
est2_sig = est_sig.fit()
print(est2_sig.summary())


# Create a new variable
data['interaction_term'] = data['employed_usa'] * data['unemploy_rate_usa']

# Add the new variable to the list of independent variables
independent_variables_transformed = independent_variables + ['interaction_term']

# Develop a new multiple regression equation
X_trans = data[independent_variables_transformed]
y_trans = data['oil_price_br']

X_train_trans, X_test_trans, y_train_trans, y_test_trans = train_test_split(X_trans, y_trans, test_size=0.2, random_state=42)
model_trans = LinearRegression()
model_trans.fit(X_train_trans, y_train_trans)

y_pred_trans = model_trans.predict(X_test_trans)
mse_trans = mean_squared_error(y_test_trans, y_pred_trans)
r2_trans = r2_score(y_test_trans, y_pred_trans)
print(f'Mean Squared Error: {mse_trans}')
print(f'R2 Score: {r2_trans}')

# Test the significance of the new model and each independent variable
X2_trans = sm.add_constant(X_trans)
est_trans = sm.OLS(y_trans, X2_trans)
est2_trans = est_trans.fit()
print(est2_trans.summary())
