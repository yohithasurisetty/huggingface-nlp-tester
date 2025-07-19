
from fpdf import FPDF
import datetime

def generate_pdf_report(accuracy, report, cm):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="NLP Model Accuracy Report", ln=1, align="C")
    pdf.cell(200, 10, txt=f"Generated on: {datetime.datetime.now()}", ln=2, align="C")

    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Accuracy: {accuracy:.2%}", ln=3)

    pdf.ln(10)
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 5, txt="Classification Report:" + report)

    pdf.ln(5)
    pdf.multi_cell(0, 5, txt="Confusion Matrix:" + str(cm))

    pdf.output("model_accuracy_report.pdf")
