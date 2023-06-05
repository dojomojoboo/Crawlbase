from dotenv import load_dotenv
import os
import urllib.parse
import urllib.request

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

url = urllib.parse.quote('https://www.glassdoor.com/Reviews/Glassdoor-Reviews-E100431.htm')

handler = urllib.request.urlopen('https://api.crawlbase.com/?token=' + api_key'&url=' + url)

print (handler.read())