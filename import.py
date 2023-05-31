import urllib.parse
import urllib.request

url = urllib.parse.quote('https://www.glassdoor.com/Reviews/Glassdoor-Reviews-E100431.htm')

handler = urllib.request.urlopen('https://api.crawlbase.com/?token=hDwx1MeuxHbOF8J0EDMRHQ&url=' + url)

print (handler.read())