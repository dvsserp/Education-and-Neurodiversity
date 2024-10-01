from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the LLaMA model and tokenizer
model_name = "meta-llama/Llama-2-7b"  # Use the appropriate model version
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Prepare input
input_text = "What is the capital of France?"
inputs = tokenizer(input_text, return_tensors="pt")

# Generate the output
outputs = model.generate(inputs["input_ids"], max_length=50, num_return_sequences=1)

# Decode the output
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)
