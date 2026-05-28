from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Split dataset into training and testing sets.
def split_dataset(X, y):
    return train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

#Training the model using Multinomial Naive Bayes algorithm which is suitable for text classification tasks.
def train_model(X_train, y_train):
    model = MultinomialNB()
    model.fit(X_train, y_train)
    return model

# Evaluating the model's performance using accuracy score and classification report.
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    print("\nAccuracy:", accuracy)

    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))