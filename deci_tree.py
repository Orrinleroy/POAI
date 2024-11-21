from sklearn.datasets import load_iris 
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeClassifier, plot_tree 
from sklearn.metrics import accuracy_score 
import matplotlib.pyplot as plt 

data = load_iris() 
X = data.data 
y = data.target 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42) 

classifier = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42) 
classifier.fit(X_train, y_train) 

y_pred = classifier.predict(X_test) 

accuracy = accuracy_score(y_test, y_pred) 
print(f"Decision Tree Classifier Accuracy: {accuracy:.2f}") 

plt.figure(figsize=(12, 8)) 
plot_tree(classifier, filled=True, feature_names=data.feature_names, class_names=data.target_names) 
plt.title("Decision Tree Structure") 
plt.show() 
