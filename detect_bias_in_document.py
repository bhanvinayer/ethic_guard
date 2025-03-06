from models.social_bias_detector import analyze_text_bias
import fitz  # PyMuPDF

def detect_bias_in_document(input_pdf_path, output_pdf_path):
    # Open the PDF
    doc = fitz.open(input_pdf_path)
    
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        
        # Split text into sentences
        sentences = text.split('. ')
        
        for sentence in sentences:
            # Analyze bias
            bias_result = analyze_text_bias(sentence)
            bias_score = bias_result['bias_score']
            risk_level = bias_result['risk_level']
            
            # Highlight biased sentences in light blue
            if risk_level in ["High", "Very High"]:
                highlight = page.add_highlight_annot(page.search_for(sentence))
                highlight.set_colors(stroke=(0.5, 0.8, 1))  # Light blue color
                highlight.update()
            
            # Add annotations for bias score and risk level
            page.insert_text((72, 72), f"Bias Score: {bias_score:.4f}", fontsize=8, color=(0, 0, 1))
            page.insert_text((72, 84), f"Risk Level: {risk_level}", fontsize=8, color=(0, 0, 1))
    
    # Save the processed PDF
    doc.save(output_pdf_path)

# Example usage
input_pdf_path = "/c:/Users/RAJAT/OneDrive/Desktop/ethicalreviewsys/backend/models/sample.pdf"
output_pdf_path = "/c:/Users/RAJAT/OneDrive/Desktop/ethicalreviewsys/backend/models/sample_processed.pdf"
detect_bias_in_document(input_pdf_path, output_pdf_path)
