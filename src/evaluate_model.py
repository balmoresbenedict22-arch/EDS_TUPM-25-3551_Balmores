from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

def evaluate_model(model, X_test, y_test):

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    matrix = confusion_matrix(y_test, predictions)

    print("Confusion Matrix:")
    print(matrix)

    return accuracy