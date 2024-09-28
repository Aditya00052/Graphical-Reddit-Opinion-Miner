# if error code = 401, then get a new bearer token as they expire in 24 hrs
import requests
import sentiment_mod as s

query = 'iphone'

headers = {
    'User-Agent': 'YOUR_USERNAME',
    'Authorization': 'YOUR_BEARER_TOKEN',
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



