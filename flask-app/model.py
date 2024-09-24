import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

# Example dataset
data = pd.DataFrame({
    'age': [20, 25, 30, 35, 40],
    'target': [100, 150, 200, 250, 300]  # Example target values
})

# Train a model
X = data[['age']]
y = data['target']
model = LinearRegression()
model.fit(X, y)

# Save the model
with open('model.pkl', 'wb') as model_file:
    pickle.dump(model, model_file)
