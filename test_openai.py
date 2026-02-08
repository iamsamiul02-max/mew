"""Test script for the OpenAI-like API."""

from openai import OpenAI

# Test the exact code from the problem statement
client = OpenAI()

response = client.responses.create(
    input="In one sentence, what is cs50?",
    model="gpt-5"
)

print(response.output_text)
