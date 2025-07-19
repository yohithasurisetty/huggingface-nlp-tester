
# 🤖 NLP Model Accuracy Tester (Hugging Face)

A web-based app to test the accuracy of any Hugging Face NLP model using a labeled dataset.

## 🔧 Features
- Upload your own CSV (with `text`, `label` columns)
- Select any Hugging Face model (e.g., `distilbert-base-uncased-finetuned-sst-2-english`)
- View classification accuracy, report, and confusion matrix
- Generate a downloadable PDF report

## 🚀 How to Run
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run the app:
   ```
   streamlit run app.py
   ```

3. Upload your dataset and analyze results!

## 📁 Sample Input
CSV format:
```
text,label
"I love this movie",1
"This was terrible",0
```

## 📄 Output
- On-screen metrics
- `model_accuracy_report.pdf` file
