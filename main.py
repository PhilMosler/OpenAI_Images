import openai

# Set the OpenAI API key
openai.api_key = "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"

# Generate an image
response = openai.Image.create(
  prompt="a real dog body with a cat head",
  n=5,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
