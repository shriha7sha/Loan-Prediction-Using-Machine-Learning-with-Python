import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LogisticRegression

from sklearn.metrics import accuracy_score

from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("dataset/loan_data.csv")

encoder = LabelEncoder()

data["Gender"] = encoder.fit_transform(data["Gender"])

data["Married"] = encoder.fit_transform(data["Married"])

data["Education"] = encoder.fit_transform(data["Education"])

data["Self_Employed"] = encoder.fit_transform(data["Self_Employed"])

data["Property_Area"] = encoder.fit_transform(data["Property_Area"])

data["Loan_Status"] = encoder.fit_transform(data["Loan_Status"])

X = data.drop("Loan_Status",axis=1)

y = data["Loan_Status"]

X_train,X_test,y_train,y_test=train_test_split(

X,

y,

test_size=.20,

random_state=42

)

model=LogisticRegression(max_iter=1000)

model.fit(X_train,y_train)

prediction=model.predict(X_test)

print("Accuracy")

print(accuracy_score(y_test,prediction))
