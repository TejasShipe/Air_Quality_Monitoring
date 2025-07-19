# src/tfidf_analysis.py
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

def train_complaint_model():
    complaints = [
        "It smells bad today",
        "Air is smoky and unhealthy",
        "Fresh and clean air",
        "No pollution today"
    ]
    labels = [1, 1, 0, 0]  # 1: bad air, 0: good

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(complaints)

    model = LogisticRegression()
    model.fit(X, labels)

    joblib.dump(model, 'src/complaint_model.pkl')
    joblib.dump(vectorizer, 'src/vectorizer.pkl')
    print("✅ Complaint classifier trained and saved.")

def analyze_complaint(text):
    model = joblib.load('src/complaint_model.pkl')
    vectorizer = joblib.load('src/vectorizer.pkl')
    X = vectorizer.transform([text])
    prediction = model.predict(X)[0]
    return "⚠️ Bad Air Complaint" if prediction == 1 else "✅ No Issue"
if __name__ == "__main__":
    train_complaint_model()
