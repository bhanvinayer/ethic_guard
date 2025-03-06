from policy_generator import generate_policy

# Example policy text
policy_text = """
We strive to create an inclusive environment where everyone feels valued and respected.
"""

# Generate policy recommendations
result = generate_policy(policy_text)
print("Original Policy:")
print(result["original_policy"])
print("\nRevised Policy:")
print(result["revised_policy"])
