
import torch
from transformers import RobertaTokenizer, RobertaForSequenceClassification

# Load the RoBERTa tokenizer and model
tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
model = RobertaForSequenceClassification.from_pretrained('roberta-base', num_labels=2)

# Example short phrases
phrases = ['happy', 'hello world', 'not meaningful', 'good']

# Tokenize the phrases and convert to input IDs
input_ids = []
for phrase in phrases:
    encoded = tokenizer.encode(phrase, add_special_tokens=True)
    input_ids.append(encoded)

# Pad and truncate the input IDs to a fixed length
max_len = 4
padded_inputs = torch.zeros(len(input_ids), max_len, dtype=torch.long)
for i, input_id in enumerate(input_ids):
    padded_inputs[i, :len(input_id)] = torch.tensor(input_id)[:max_len]

# Predict the labels for the phrases
with torch.no_grad():
    outputs = model(padded_inputs)
    predictions = torch.argmax(outputs[0], dim=1)

# Print the predicted labels for the phrases
for i, phrase in enumerate(phrases):
    label = 'meaningful' if predictions[i] == 1 else 'not meaningful'
    print(f'{phrase}: {label}')
