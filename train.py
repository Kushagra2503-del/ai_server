import joblib
from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.array([[10, 50], [2, 5], [50, 200], [5, 10]])
y = np.array([1, 0, 1, 0])

model = RandomForestClassifier(n_estimators=10, random_state=42)
model.fit(X, y)
joblib.dump(model, "model.pkl")
print(" Model saved!")