import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

data = pd.read_csv("transformer_data.csv")

X = data[["Load_kW","Temp_C","Voltage","Oil_Level","Age_Years"]]
y = data["Failure"]

X_train,X_test,y_train,y_test=train_test_split(
X,y,test_size=0.2,random_state=42)

lr=LogisticRegression(max_iter=1000)
lr.fit(X_train,y_train)

lr_pred=lr.predict(X_test)
lr_acc=accuracy_score(y_test,lr_pred)

rf=RandomForestClassifier(random_state=42)

rf.fit(X_train,y_train)

rf_pred=rf.predict(X_test)

rf_acc=accuracy_score(y_test,rf_pred)

print("Logistic Regression:",lr_acc)
print("Random Forest:",rf_acc)

with open("model.pkl","wb") as f:
    pickle.dump(rf,f)

print("Best Model Saved!")