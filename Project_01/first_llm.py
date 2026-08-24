from google import genai
from dotenv import load_dotenv


load_dotenv('../.env')
client = genai.Client()

interaction = client.interactions.create(
    model='gemini-3.5-flash',
    input="Write a short poem about the beauty of nature. Output should be within 2 lines"
)

print(interaction.output_text)