# Machine Learning: Zero to Hero

This repository contains a collection of machine learning implementations and experiments. The Jupyter notebooks are located in the [src](src/) directory, and relevant datasets are in the [datasets](datasets/) directory.

## Linear Regression

**Predicting Exam Scores (Simple Linear Regression)**

We start with the "Hello World" of machine learning. In this project, we analyze the relationship between study hours and exam scores. We implement a model to fit a line through the data, observing a strong positive correlation where every additional hour of study adds approximately 11.29 points to the score. We also explore error metrics like MSE and RMSE to evaluate our model's performance.

- [Jupyter notebook files](src/regression/linear_regression.ipynb)

---

**Real Estate Price Prediction (Multivariate Regression)**

We expand our Linear Regression model to handle multiple features. Instead of a simple line, we fit a plane in 3D space to predict house prices based on size (sq ft) and the number of bedrooms. This introduces the concept of weights for different features and how they combine to form a prediction.

- [Jupyter notebook files](src/regression/real_estate_price.ipynb)

---

**Marketing ROI Estimation (Multivariate Regression)**

In this business-centric example, we apply Multivariate Regression to optimize marketing strategies. By analyzing historical data on TV and Radio advertising budgets, we build a model to predict future Sales figures. We interpret the model coefficients to understand the return on investment for specific advertising channels and use the R-squared ($R^2$) score to determine how well our model explains the variance in sales.

- [Jupyter notebook files](src/regression/marketing_roi.ipynb)

---

Ongoing...

**License**

MIT