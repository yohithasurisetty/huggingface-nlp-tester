from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(true, pred):
    true = [str(x).lower().strip() for x in true]
    pred = [str(x).lower().strip() for x in pred]

    acc = accuracy_score(true, pred)
    report = classification_report(true, pred)
    cm = confusion_matrix(true, pred)
    return acc, report, cm

def plot_confusion(true, pred):
    true = [str(x).lower().strip() for x in true]
    pred = [str(x).lower().strip() for x in pred]

    cm = confusion_matrix(true, pred)
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    return plt
