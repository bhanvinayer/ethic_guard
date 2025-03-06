import os
from together import Together
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Together AI client
client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

def reframe_unbiased_sentence(sentence):
    """
    Rephrases a biased sentence to remove bias while preserving meaning.

    Args:
        sentence (str): The biased sentence.

    Returns:
        str: The unbiased sentence.
    """
    prompt = f"Rephrase the following sentence to remove any bias while maintaining its original meaning:\n\n'{sentence}'"

    try:
        response = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "You are an expert in unbiased and fair language rephrasing."},
                {"role": "user", "content": prompt}
            ],
            model="meta-llama/Llama-3.3-70B-Instruct-Turbo",
            temperature=0.3,
            max_tokens=100,
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating unbiased sentence: {e}")
        return sentence  # Return original sentence if error occurs


def reframe_policy(text, biased_sentences):
    """
    Rewrites only biased sentences within a business policy document.

    Args:
        text (str): The full policy document.
        biased_sentences (list): List of identified biased sentences.

    Returns:
        dict: A dictionary containing the original policy and the revised version.
    """
    if not text or not isinstance(text, str):
        return {"error": "Invalid input. Please provide a valid text string."}

    revised_text = text  # Start with the original text

    for sentence in biased_sentences:
        unbiased_sentence = reframe_unbiased_sentence(sentence)
        revised_text = revised_text.replace(sentence, unbiased_sentence)

    return {
        "original_policy": text,
        "revised_policy": revised_text
    }