from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, classification_report, f1_score

print("Libraries Imported Successfully")
iris = load_iris()

X = iris.data
y = iris.target

print("Features Shape:", X.shape)
print("Labels Shape:", y.shape)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
model = KNeighborsClassifier(n_neighbors=5)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
accuracy = model.score(X_test, y_test)

print("Accuracy:", accuracy)
cm = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(cm)
f1 = f1_score(y_test, predictions, average='weighted')

print("\nF1 Score:", f1)
print("\nClassification Report:")
print(classification_report(y_test, predictions))