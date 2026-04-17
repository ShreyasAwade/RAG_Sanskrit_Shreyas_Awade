# generator.py

from transformers import pipeline

# Load CPU-friendly model
generator = pipeline(
    "text-generation",
    model="google/flan-t5-base"
)


# Generate answer using context
def generate_answer(query, context):
    prompt = f"""
    Answer the question based on the given Sanskrit context.

    Context:
    {context}

    Question:
    {query}
    """

    result = generator(prompt, max_length=200, do_sample=False)

    return result[0]["generated_text"]