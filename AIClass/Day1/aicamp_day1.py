def make_text(response):

    # DeepSeek / Hugging Face API response
    if isinstance(response, dict) and "choices" in response:
        return response["choices"][0]["message"]["content"]

    # GPT-2 / TinyLlama / Transformers pipeline response
    elif isinstance(response, list) and len(response) > 0:
        if "generated_text" in response[0]:
            return response[0]["generated_text"]

    raise ValueError("Unsupported AI response format")