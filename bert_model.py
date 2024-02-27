from transformers import BertTokenizer, BertForSequenceClassification

# Initialize BERT tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# Initialize BERT for sequence classification
model = BertForSequenceClassification.from_pretrained('bert-base-uncased')

# Set the model to evaluation mode
model.eval()
