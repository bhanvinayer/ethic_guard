from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def generate_sample_pdf(output_path):
    c = canvas.Canvas(output_path, pagesize=letter)
    width, height = letter

    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, "Our leadership team firmly believes that men naturally possess stronger decision-making skills and logical thinking, making them ideal candidates for executive roles.")
    c.drawString(100, height - 120, "Our company values diversity and strives for an inclusive workforce. However, we acknowledge that leadership roles often demand assertiveness and confidence, qualities that some employees naturally exhibit more than others.")
    c.drawString(100, height - 140, "We recognize that different individuals bring unique strengths, and we focus on skills, experience, and performance when making hiring and promotion decisions.")
    c.drawString(100, height - 160, "Our hiring, promotion, and leadership development processes are designed to provide equal opportunities for all individuals, regardless of race, gender, or personal background.")
    c.drawString(100, height - 180, "Our team values collaboration and teamwork. Every employee is encouraged to contribute their ideas, and decision-making is based on objective factors such as expertise and innovation.")
    c.drawString(100, height - 200, "We encourage continuous learning and professional growth, ensuring that all employees have access to the resources and mentorship needed to succeed.")

    c.save()

# Generate the sample PDF
output_path = "/c:/Users/RAJAT/OneDrive/Desktop/ethicalreviewsys/backend/models/sample.pdf"
generate_sample_pdf(output_path)
