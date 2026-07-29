import joblib

model = joblib.load("model.pkl")

sample = [[5000,1500,150000,360,1]]

prediction = model.predict(sample)

print(prediction)
