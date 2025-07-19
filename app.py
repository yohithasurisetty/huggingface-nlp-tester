
import streamlit as st
from model_utils import load_model, predict
from metrics_utils import evaluate_model, plot_confusion
from report_generator import generate_pdf_report
import pandas as pd

st.title("🤖 NLP Model Accuracy Tester (Hugging Face)")

uploaded_file = st.file_uploader("Upload CSV (text, label)", type=["csv"])

model_name = st.text_input("Enter Hugging Face Model ID", "distilbert-base-uncased-finetuned-sst-2-english")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    texts = df["text"].tolist()
    labels = df["label"].tolist()

    model = load_model(model_name)
    preds = predict(model, texts)

    st.success("Prediction completed ✅")

    acc, clf_report, cm = evaluate_model(labels, preds)

    st.metric("Accuracy", f"{acc*100:.2f}%")
    st.text("Classification Report:")
    st.text(clf_report)

st.pyplot(plot_confusion(labels, preds))


    if st.button("Generate PDF Report"):
        generate_pdf_report(acc, clf_report, cm)
        st.success("PDF report generated ✅ (check your project folder)")
