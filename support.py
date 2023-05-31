from proxycrawl import CrawlingAPI

api = CrawlingAPI({ 'token': 'hDwx1MeuxHbOF8J0EDMRHQ' })

response = api.get ('https://example.com/', {
'autoparse': 'true'
})

print(response)