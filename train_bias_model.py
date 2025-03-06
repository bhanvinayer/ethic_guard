import torch
import pandas as pd
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load dataset
df = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", header=None)

# Define column names
columns = ["age", "workclass", "fnlwgt", "education", "education-num", "marital-status", "occupation",
           "relationship", "race", "sex", "capital-gain", "capital-loss", "hours-per-week", "native-country", "income"]
df.columns = columns

# Print column names for debugging
print("\nCorrected Column Names:")
print(df.columns)

# Extract relevant columns
df = df[['relationship', 'race', 'sex']]

# Combine selected columns into a single text field
df['text'] = df[['relationship', 'race']].astype(str).agg(' '.join, axis=1)

# Convert labels to binary (1 = Male, 0 = Female)
df['label'] = df['sex'].apply(lambda x: 1 if x.strip() == 'Male' else 0)

# Keep only text and label
df = df[['text', 'label']]

# Ensure dataset has "text" and "label" columns
if "text" not in df.columns or "label" not in df.columns:
    raise ValueError("Dataset must contain 'text' and 'label' columns.")

# Train-test split (80% train, 20% validation)
train_texts, val_texts, train_labels, val_labels = train_test_split(
    df["text"].tolist(), df["label"].tolist(), test_size=0.2, random_state=42
)

# Load tokenizer
tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

# Tokenization function
def tokenize_data(texts):
    return tokenizer(texts, padding="max_length", truncation=True, max_length=512)

# Tokenize train and validation data
train_encodings = tokenize_data(train_texts)
val_encodings = tokenize_data(val_texts)

# Convert to Hugging Face Dataset
train_dataset = Dataset.from_dict({
    "input_ids": train_encodings["input_ids"],
    "attention_mask": train_encodings["attention_mask"],
    "labels": train_labels
})

val_dataset = Dataset.from_dict({
    "input_ids": val_encodings["input_ids"],
    "attention_mask": val_encodings["attention_mask"],
    "labels": val_labels
})

# Load pre-trained DistilBERT model
model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)
model.to(device)

# Define training arguments with 3 epochs
training_args = TrainingArguments(
    output_dir="./bias_detection_model",
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    per_device_train_batch_size=32,
    per_device_eval_batch_size=32,
    num_train_epochs=3,  # Changed to 3 epochs
    learning_rate=2e-5,
    save_total_limit=2,
    load_best_model_at_end=True,
    metric_for_best_model="accuracy",
    evaluation_strategy="epoch",
    report_to="none"
)

# Function to compute accuracy
def compute_metrics(eval_pred):
    logits, labels = eval_pred
    predictions = torch.argmax(torch.tensor(logits), dim=-1)
    accuracy = accuracy_score(labels, predictions)
    return {"accuracy": accuracy}

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=compute_metrics,  # Add accuracy computation
)

# Train model
trainer.train()

# Evaluate and print accuracy
metrics = trainer.evaluate()
print(f"✅ Model trained with Accuracy: {metrics['eval_accuracy']:.4f}")

# Save model
model.save_pretrained("./bias_detection_model")
tokenizer.save_pretrained("./bias_detection_model")

print("✅ Model trained and saved in './bias_detection_model'")
