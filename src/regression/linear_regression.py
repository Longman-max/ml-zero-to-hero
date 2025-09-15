"""
linear_regression.py
--------------------
A simple example of linear regression using scikit-learn.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Generate some sample data
X = np.linspace(0, 10, 100).reshape(-1, 1)   # Feature
y = 3 * X.squeeze() + 7 + np.random.randn(100) * 2  # Target with noise

# Split into train and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print model parameters
print("Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)
print("R^2 Score (test set):", model.score(X_test, y_test))

# Plot results
plt.scatter(X_test, y_test, color="blue", label="Actual")
plt.plot(X_test, y_pred, color="red", linewidth=2, label="Predicted")
plt.title("Linear Regression Example")
plt.xlabel("X")
plt.ylabel("y")
plt.legend()
plt.show()
