#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install gpt4all


# In[2]:


from gpt4all import GPT4All

model_path = r"C:\Users\the_dell\Downloads\ggml-gpt4all-j-v1.3-groovy.bin"

# Correct usage: manually specify model_type
gpt = GPT4All(model_path=model_path, model_type="gptj")

# Test generation
response = gpt.generate("What is the capital of Nigeria?")
print("Bot:", response)


# In[6]:


from gpt4all import GPT4All

model_path = r"C:\Users\the_dell\Downloads\ggml-gpt4all-j-v1.3-groovy.bin"
model_name = "ggml-gpt4all-j-v1.3-groovy"  # just a label

gpt = GPT4All(model_name=model_name, 
              model_path=model_path, 
              model_type="gptj", 
              allow_download=False)

# Test it
response = gpt.generate("What is the capital of Nigeria?")
print(response)


# In[10]:


get_ipython().system('pip uninstall -y gpt4all')
get_ipython().system('pip install gpt4all==0.2.3')


# In[3]:


get_ipython().system('pip uninstall -y backports.tarfile')


# In[4]:


get_ipython().system('pip install --upgrade setuptools jaraco.text jaraco.context')


# In[5]:


from gpt4all import GPT4All

model_path = r"C:\Users\the_dell\Downloads\ggml-gpt4all-j-v1.3-groovy.bin"
model_name = "ggml-gpt4all-j-v1.3-groovy"

gpt = GPT4All(model_name=model_name, model_path=model_path, model_type="gptj")
print(gpt.generate("What is the capital of Nigeria?"))


# In[7]:


from gpt4all import GPT4All

model_path = r"C:\Users\the_dell\Downloads\ggml-gpt4all-j-v1.3-groovy.bin"
model_name = "ggml-gpt4all-j-v1.3-groovy"

gpt = GPT4All(model_name=model_name, model_path=model_path, model_type="gptj", allow_download=False)
print(gpt.generate("What is the capital of Nigeria?"))


# In[8]:


from transformers import pipeline

generator = pipeline('text-generation', model='distilgpt2')
print(generator("Hello, world!", max_length=30))


# In[9]:


#from transformers import pipeline

# Load the text-generation pipeline with DistilGPT-2
#generator = pipeline('text-generation', model='distilgpt2')

# Your prompt/question
prompt = "What is the capital of Nigeria?"

# Generate response
result = generator(prompt, max_length=50, num_return_sequences=1)

# Print the generated text
print(result[0]['generated_text'])


# In[11]:


from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
from llm_guard.input_scanners import PromptInjection
from datasets import load_dataset
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

# Load DistilGPT-2 Model and Tokenizer
model_name = "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

chatbot_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Initialize Prompt Injection Scanner
scanner = PromptInjection()

def safe_chatbot(user_prompt):
    sanitized_prompt, is_valid, risk_score = scanner.scan(user_prompt)
    if is_valid:
        response = chatbot_pipeline(sanitized_prompt, max_new_tokens=100)
        return response[0]['generated_text']
    else:
        return f"Prompt rejected due to security concerns. Risk score: {risk_score}"

# Load Dataset
dataset = load_dataset("xTRam1/safe-guard-prompt-injection")

def test_chatbot_on_dataset(dataset, sample_size=200): #sample sixe 100
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

# Run the test
results_df = test_chatbot_on_dataset(dataset)

# Metrics
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




