#!/usr/bin/env python
# coding: utf-8

# In[1]:


from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)
chatbot("What is the capital of Nigeria?", max_new_tokens=50)


# In[2]:


from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from llm_guard.input_scanners import PromptInjection
from datasets import load_dataset
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Load Microsoft Phi-2
model_name = "microsoft/phi-2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")

chatbot_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)





# In[3]:


scanner = PromptInjection()

# Load the HuggingFace prompt injection dataset
dataset = load_dataset("xTRam1/safe-guard-prompt-injection")

# Define safe chatbot function
def safe_chatbot(user_prompt):
    sanitized_prompt, is_valid, risk_score = scanner.scan(user_prompt)
    if is_valid:
        response = chatbot_pipeline(sanitized_prompt, max_new_tokens=50)
        return response[0]['generated_text']
    else:
        return f"[BLOCKED] Risk Score: {risk_score}"

# Test on dataset
def test_chatbot_on_dataset(dataset, sample_size=2000):
    results = []
    for example in dataset["train"].select(range(sample_size)):
        prompt = example['text']
        label = "safe" if example['label'] == 0 else "unsafe"

        sanitized_prompt, is_valid, risk_score = scanner.scan(prompt)
        if is_valid:
            response = chatbot_pipeline(sanitized_prompt, max_new_tokens=50)[0]['generated_text']
        else:
            response = f"[BLOCKED] Risk Score: {risk_score}"

        results.append({
            "Original Prompt": prompt,
            "Ground Truth Label": label,
            "Sanitized Prompt": sanitized_prompt,
            "Accepted Prompt": is_valid,
            "Risk Score": risk_score,
            "Chatbot Response": response
        })

    return pd.DataFrame(results)

# Execute evaluation
results_df = test_chatbot_on_dataset(dataset, sample_size=10)

# Print evaluation metrics
true_labels = results_df['Ground Truth Label'].map({'safe': 0, 'unsafe': 1}).tolist()
predicted_labels = results_df['Accepted Prompt'].map({True: 0, False: 1}).tolist()

print("Accuracy:", accuracy_score(true_labels, predicted_labels))
print("Precision:", precision_score(true_labels, predicted_labels))
print("Recall:", recall_score(true_labels, predicted_labels))
print("F1-Score:", f1_score(true_labels, predicted_labels))

print("\nClassification Report:")
print(classification_report(true_labels, predicted_labels, target_names=['safe', 'unsafe']))

print("\nConfusion Matrix:")
print(confusion_matrix(true_labels, predicted_labels))


# In[ ]:




