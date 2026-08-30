from google import genai
from dotenv import load_dotenv


load_dotenv('../.env')
client = genai.Client()