# if error code = 401, then get a new bearer token as they expire in 24 hrs
import requests
import sentiment_mod as s

query = 'iphone'

headers = {
    'User-Agent': 'Deadshot244516',
    'Authorization': 'bearer eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzI2OTk2MTg0Ljg5ODY1OCwiaWF0IjoxNzI2OTA5Nzg0Ljg5ODY1OCwianRpIjoiOWNtWWJWbUdjUkkyM0xaZDRSUHlkV0ROd3BuNmlBIiwiY2lkIjoiUDcyVVpSRVM2R2pJc05UQ3o3ZDlIdyIsImxpZCI6InQyXzRtbXpxbWZoIiwiYWlkIjoidDJfNG1tenFtZmgiLCJsY2EiOjE1Njg5ODgxNDU4OTIsInNjcCI6ImVKeUtWdEpTaWdVRUFBRF9fd056QVNjIiwiZmxvIjo5fQ.VdVZuygF3etVJDFDR1xeOHbmmqe_18shkJ_wb7rw8SyWNUqoPZL2FLvjtYU3RXNl7RUVVAcFUJ0hhesArgIF4nFDffDlNzwLhB5bQoZZqDC_rDyWk81qzWtnVdvAlmZmjEcB-9-yoohbWnkXcEqm2bZuR0JwYFspGADeE3W4X8pMPGIobk4xC7hxxfhxxYwZVYYbtzS36SvT12vlW9nS2SK0hjWPLmpigev05N9sVnRncCbZ_QE-HyzJpolvRp2H9sDMMIV5trTwot2ByErxgMilkgxl0UldeRtTzdmf9nmUfjq9aC_VOVQUJCIsWyZnP5PJI0EogZhhVft0SLaj3w',
}


# Endpoint 4: Search v3 (Use for static file):

params = {
    'q': f'{query}+self:yes',
    'restrict_sr': 'on',
    'sort': 'hot',
    'limit': 100,
}

response = requests.get(url=f'https://oauth.reddit.com/search.json', headers=headers, params=params)
response = response.json()

reviews = []

for rev_data in response['data']['children']:
    reviews.append(rev_data['data']['selftext'])

# for i, rev in enumerate(reviews):
#     print(f'{i+1}: {rev}')


def process_reviews(reviews):
    for rev in reviews:
        sentiment_val, confidence = s.sentiment(rev)
        print(rev, sentiment_val, confidence)

        if confidence*100 >= 80:
            with open('reddit-out.txt', 'a') as output:
                output.write(sentiment_val)
                output.write('\n')


process_reviews(reviews)



