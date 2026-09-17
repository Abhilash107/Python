from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('api_key')

print(api_key)