import fitz  # PyMuPDF
from models.bias_detector import analyze_text_bias 
from models.social_bias_detector import analyze_text_bias_social 
from models.policy_generator import reframe_unbiased_sentence
from models.sentiment_analysis import analyze_sentiment

def get_sentiment_category(score):
    """Convert sentiment score to simple category"""
    if score < 0.3:
        return "Negative"
    elif score > 0.7:
        return "Positive"
    else:
        return "Neutral"

def process_pdf(input_pdf_path, output_pdf_path):
    """Processes a PDF, highlights biased sentences, adds bias key, and appends a bias report."""
    
    doc = fitz.open(input_pdf_path)
    all_bias_reports = []  # Stores bias sentences and unbiased versions

    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text("text")
        sentences = text.split('. ')  # Split text into sentences
        new_page_content = []  # Collect annotations for new summary pages
        
        page_bias_score = 0  # Track total bias score per page
        page_social_bias_score = 0  # Track social bias score per page
        bias_count = 0  # Count biased sentences

        # ✅ 1️⃣ ADD LEGEND (KEY) AT THE TOP
        legend_x_start = 50
        legend_y_start = 20
        
        legend_items = [
            ("Gender Bias", (1, 1, 0)),  # Yellow
            ("Opinion Bias", (0.5, 0.8, 1)),  # Light Blue
            ("Both", (0.3, 0.9, 0.3))  # Green
        ]
        
        for label, color in legend_items:
            page.draw_rect(
                fitz.Rect(legend_x_start, legend_y_start, legend_x_start + 15, legend_y_start + 15),
                color=color, fill=color, width=0  # width=0 ensures it's fully filled
            )
            page.insert_text(
                (legend_x_start + 20, legend_y_start + 10), f"- {label}",
                fontsize=9, color=(0, 0, 0)
            )
            legend_x_start += 100  # Move right for next label
        
        legend_y_start += 25  # Move down for bias scores

        for sentence in sentences:
            if len(sentence.strip()) < 5:  # Ignore very short fragments
                continue

            # ✅ 2️⃣ ANALYZE BIAS
            bias_result = analyze_text_bias(sentence)
            risk_level = bias_result.get('risk_level', 'Low')
            bias_score = bias_result.get('bias_score', 0)
            
            social_bias_result = analyze_text_bias_social(sentence)
            social_risk_level = social_bias_result.get('risk_level', 'Low')
            social_bias_score = social_bias_result.get('bias_score', 0)
            sentiment_result = analyze_sentiment(sentence)
            sentiment_label = sentiment_result['sentiment_label']
            sentiment_score = sentiment_result['sentiment_score']
            
            # Update Page Scores
            page_bias_score += bias_score
            page_social_bias_score += social_bias_score
            bias_count += 1

            # ✅ 3️⃣ HIGHLIGHT TEXT BASED ON BIAS TYPE
            found_instances = page.search_for(sentence)
            
            highlight_color = None
            if risk_level in ["High", "Very High"] and social_risk_level in ["High", "Very High"]:
                highlight_color = (0.3, 0.9, 0.3)  # Green (Both Biases)
            elif risk_level in ["High", "Very High"]:
                highlight_color = (1, 1, 0)  # Yellow (Gender Bias)
            elif social_risk_level in ["High", "Very High"]:
                highlight_color = (0.5, 0.8, 1)  # Light Blue (Social Bias)

            if highlight_color and found_instances:
                for inst in found_instances:
                    highlight = page.add_highlight_annot(inst)
                    highlight.set_colors(stroke=highlight_color)
                    highlight.update()

                # ✅ 4️⃣ COLLECT ONLY HIGHLIGHTED SENTENCES FOR SUMMARY
                unbiased_sentence = reframe_unbiased_sentence(sentence)
                annotation_text = (f"🔸 Biased Sentence: {sentence}\n"
                                   f"✅ Unbiased Suggestion: {unbiased_sentence}\n")
                new_page_content.append(annotation_text)
        
        # ✅ 5️⃣ SHOW PAGE BIAS SCORE AT THE TOP
        avg_bias_score = (page_bias_score / bias_count) if bias_count else 0
        avg_social_bias_score = (page_social_bias_score / bias_count) if bias_count else 0
        
        # Update bias summary with simple sentiment category
        sentiment_category = get_sentiment_category(sentiment_score)
        bias_summary = (
            f"📊 Bias Detector Score: {avg_bias_score:.2f} | Risk: {risk_level}\n"
            f"🌍 Opinion Bias Score: {avg_social_bias_score:.2f} | Risk: {social_risk_level}\n"
            f"💭 Sentiment: {sentiment_category}\n"
        )
        
        # Adjust Y position for the extra line
        page.insert_text(
            (50, legend_y_start + 15),
            bias_summary,
            fontsize=9, color=(0, 0, 0)
        )

        # ✅ 6️⃣ ADD SUMMARY PAGES WITH ANNOTATIONS (WITH PROPER SPACING)
        if new_page_content:
            y_offset = 50  # Reset Y position for text
            page_height = 800  # Approximate height of a page
            line_spacing = 20  # Increased line spacing to avoid overlap
            max_y_offset = page_height - 50  # Maximum Y position for text

            new_page = doc.new_page()
            for content in new_page_content:
                if y_offset + line_spacing * 4 > max_y_offset:  # If text overflows, create a new page
                    new_page = doc.new_page()
                    y_offset = 50  # Reset Y position for new page

                new_page.insert_text((50, y_offset), content, fontsize=10, color=(0, 0, 0))
                y_offset += line_spacing * 4  # Move down for the next block of text
    
    # ✅ 7️⃣ SAVE PROCESSED PDF
    doc.save(output_pdf_path)
    doc.close()
