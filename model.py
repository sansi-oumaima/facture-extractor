from ctransformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-Instruct-v0.1-GGUF", model_file="*.gguf", model_type="mistral")

def complete_field(prompt):
    return model(f"{prompt}").strip()
