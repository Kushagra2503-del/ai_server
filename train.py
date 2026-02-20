import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np

# 1. Create a Balanced Dataset
data = {
    'level': [],
    'hours': [],
    'outcome': []
}

# Generate 500 random matches
for _ in range(500):
    lvl = np.random.randint(1, 101)
    hr = np.random.randint(1, 1001)

    # LOGIC: If hours are 3x the level, they should usually win
    if hr > (lvl * 3):
        outcome = 1  # Victory
    else:
        outcome = 0  # Defeat

    data['level'].append(lvl)
    data['hours'].append(hr)
    data['outcome'].append(outcome)

df = pd.DataFrame(data)

# 2. Train the Model
X = df[['level', 'hours']]
y = df['outcome']

model = RandomForestClassifier(n_estimators=100)
model.fit(X, y)

# 3. Save the new "Optimistic" Brain
joblib.dump(model, "model.pkl")
print("New balanced model trained and saved!")