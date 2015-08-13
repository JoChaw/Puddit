import requests
import json
from bs4 import BeautifulSoup

#Which subreddits would you like to monitor? (subreddits max)

target_subreddit = 'teslamotors'
pb_request_url = 'https://api.pushbullet.com/v2/pushes'
content_type = 'application/json'
authorization = 'Bearer v1s0QnhullE8cI6AB6fEwUpBIrEr2vPEGeujw1WWxXJy8'
pb_request_headers = {'Authorization': authorization, 'Content-Type': content_type}

pb_request_body = {
        "type" : "note",
        "title" : "test1",
        "body": "Gerbil"
        }

reddit_request_url = 'http://www.reddit.com/r/{0}/new'.format(target_subreddit)
reddit_response = requests.get(reddit_request_url, headers={'User-Agent': "PudditAgent"})
reddit_response_text = reddit_response.text
reddit_soup = BeautifulSoup(reddit_response_text)
reddit_site_table = reddit_soup.find_all('a', 'title', 'href', text=True)

r = requests.post(pb_request_url, headers=pb_request_headers, data=json.dumps(pb_request_body))


for blah in reddit_site_table:
    print(blah['href'] + blah.contents[0])


#validate subreddit

#Pushbullet Login

#Monitoring Loop - (When new post detected, send pushbullet message to users' devices)


