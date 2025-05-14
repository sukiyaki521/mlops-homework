def evaluate_accuracy():
    model = joblib.load("model.joblib")
    X, y = load_iris(return_X_y=True)
    pred = model.predict(X)
    return accuracy_score(y, pred)
