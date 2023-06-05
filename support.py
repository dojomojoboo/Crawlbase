from dotenv import load_dotenv
import os
from proxycrawl import CrawlingAPI

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

api = CrawlingAPI({ 'token': api_key })

response = api.get ('https://example.com/', {
'autoparse': 'true'
})

# This prints the response
print(response)