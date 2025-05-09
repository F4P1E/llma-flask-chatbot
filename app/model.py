from transformers import AutoTokenizer, AutoModelForCausalLM, TextGenerationPipeline
import os

model_id = "meta-llama/Llama-4-Scout-17B-16E-Instruct"
hf_token = os.getenv("HUGGINGFACE_TOKEN")

tokenizer = AutoTokenizer.from_pretrained(model_id, token=hf_token)
model = AutoModelForCausalLM.from_pretrained(model_id, token=hf_token, device_map="auto")

pipeline = TextGenerationPipeline(model=model, tokenizer=tokenizer, max_new_tokens=512)

def generate_response(prompt: str) -> str:
    """
    Generates a response based on the given prompt using a pre-defined text generation pipeline.

    Args:
        prompt (str): The input text prompt to generate a response for.

    Returns:
        str: The generated text response.

    Note:
        - The function uses a text generation pipeline with sampling enabled.
        - The `temperature` parameter controls the randomness of the generated text.
        - Ensure that the `pipeline` object is properly initialized before calling this function.
    """
    result = pipeline(prompt, do_sample=True, temperature=0.7)
    return result[0]["generated_text"]
