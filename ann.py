from sklearn.datasets import load_digits 
from sklearn.model_selection import train_test_split 
from sklearn.neural_network import MLPClassifier 
from sklearn.metrics import accuracy_score, classification_report 
import matplotlib.pyplot as plt 

data = load_digits() 
X = data.data 
y = data.target 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 

mlp = MLPClassifier(hidden_layer_sizes=(64,), max_iter=300, random_state=42) 
mlp.fit(X_train, y_train) 

y_pred = mlp.predict(X_test) 
 
accuracy = accuracy_score(y_test, y_pred) 
print(f"ANN Classifier Accuracy: {accuracy:.2f}") 
  
print("Classification Report:") 
print(classification_report(y_test, y_pred)) 
 
plt.plot(mlp.loss_curve_) 
plt.xlabel("Iterations") 
plt.ylabel("Loss") 
plt.title("ANN Training Loss Curve") 
plt.show() 
