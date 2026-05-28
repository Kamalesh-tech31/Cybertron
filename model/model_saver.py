import joblib

def save_model(model, filename):
    joblib.dump(model, filename)
    print(f"\nModel saved as {filename}")

def load_model(filename):
    return joblib.load(filename)