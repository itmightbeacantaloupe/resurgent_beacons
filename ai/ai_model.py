from sklearn.ensemble import RandomForestRegressor
import numpy as np

class AITOA:

    def __init__(self):
        self.model = self.model = RandomForestRegressor(n_estimators=20,max_depth=10,random_state=42)

    def train(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        return self.model.predict(X)