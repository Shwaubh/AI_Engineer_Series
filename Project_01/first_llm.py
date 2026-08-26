from google import genai
from dotenv import load_dotenv


load_dotenv('../.env')
client = genai.Client()

interaction = client.interactions.create(
    model='gemini-3.5-flash',
    input="Write a investigation report on some mystery",
    system_instruction="You are a comic agent, who answers within 3 lines",
    generation_config={
        "temperature": 0
    }
)

print(interaction.output_text)