
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def evaluate_model(true, pred):
    # Convert both lists to strings to prevent type mismatch

true = [str(x).lower().strip() for x in true]
pred = [str(x).lower().strip() for x in pred]

    acc = accuracy_score(true, pred)
    report = classification_report(true, pred)
    cm = confusion_matrix(true, pred)
    return acc, report, cm


def plot_confusion(cm):
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", ax=ax)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Actual")
    ax.set_title("Confusion Matrix")
    return fig
