import requests
import json
import time
from bs4 import BeautifulSoup

#Which subreddits would you like to monitor? (subreddits max)

new_posts = []
target_subreddit = 'askreddit'
pb_request_url = 'https://api.pushbullet.com/v2/pushes'
content_type = 'application/json'
authorization = 'Bearer v1s0QnhullE8cI6AB6fEwUpBIrEr2vPEGeujw1WWxXJy8'
pb_request_headers = {'Authorization': authorization, 'Content-Type': content_type}

pb_request_body = {
        "type" : "link",
        }

reddit_request_url = 'http://www.reddit.com/r/{0}/new'.format(target_subreddit)

while(True):
    reddit_response = requests.get(reddit_request_url, headers={'User-Agent': "PudditAgent"})
    reddit_response_text = reddit_response.text
    reddit_soup = BeautifulSoup(reddit_response_text)
    reddit_site_table = reddit_soup.find_all('a', 'title', 'href')
    reddit_time_table = reddit_soup.find_all('time', 'live-timestamp')
    reddit_post_ids = reddit_soup.find_all("div", class_='thing')
    post_ids = []

    for blah in reddit_post_ids:
        post_ids.append(blah['data-fullname'])

    for blah, grah, mrah in zip(reddit_site_table, reddit_time_table, post_ids):
        time_passed = grah.contents[0]

        if time_passed == 'just now' or time_passed == 'a minute ago':
            pb_request_body['title'] = blah.contents[0]
            pb_request_body['url'] = 'http://reddit.com' + blah['href']
            pb_request_body['body'] = mrah
            requests.post(pb_request_url, headers=pb_request_headers, data=json.dumps(pb_request_body))


    time.sleep(5)


#validate subreddit

#Pushbullet Login

#Monitoring Loop - (When new post detected, send pushbullet message to users' devices)


