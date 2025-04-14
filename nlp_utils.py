from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load fine-tuned model (you can fine-tune LegalBERT on clause classification later)
tokenizer = BertTokenizer.from_pretrained('nlpaueb/legal-bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('nlpaueb/legal-bert-base-uncased', num_labels=5)

def detect_clauses(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1)
    return predictions.item()  # returns clause index (e.g., 0 = NDA)
