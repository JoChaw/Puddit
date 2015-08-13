import requests
import json

#Which subreddits would you like to monitor? (subreddits max)

target_subreddit = 'askreddit'
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

r = requests.post(pb_request_url, headers=pb_request_headers, data=json.dumps(pb_request_body))
print(reddit_response.text)



#validate subreddit

#Pushbullet Login

#Monitoring Loop - (When new post detected, send pushbullet message to users' devices)


