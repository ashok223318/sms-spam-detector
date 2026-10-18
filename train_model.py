from pathlib import Path
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    make_scorer,
    f1_score
)

folder = Path(__file__).parent
df = pd.read_csv(folder / "data" / "clean_sms.csv")

X_train, X_test, y_train, y_test = train_test_split(
    df["message"],
    df["label"],
    test_size=0.2,
    random_state=42,
    stratify=df["label"]
)

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", MultinomialNB())
])

parameters = {
    "tfidf__ngram_range": [(1, 1), (1, 2)],
    "classifier__alpha": [0.1, 0.5, 1.0]
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

search = GridSearchCV(
    pipeline,
    parameters,
    scoring=make_scorer(f1_score, pos_label="spam"),
    cv=cv,
    n_jobs=1
)

print("Comparing model settings. Please wait...")
search.fit(X_train, y_train)

model = search.best_estimator_
predictions = model.predict(X_test)

print("\nBest settings:", search.best_params_)
print(f"Best cross-validation spam F1: {search.best_score_:.3f}")
print(f"\nTest accuracy: {accuracy_score(y_test, predictions):.2%}")

print("\nTest classification report:")
print(classification_report(y_test, predictions, zero_division=0))

print("Confusion matrix (order: ham, spam):")
print(confusion_matrix(y_test, predictions, labels=["ham", "spam"]))

joblib.dump(model, folder / "spam_model.joblib")
print("\nUpdated model saved as spam_model.joblib")