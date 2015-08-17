'''
Python script to monitor a subreddit for new posts.
User will be notified via pushbullet when a new post is detected.
'''
import os
import requests
import json
import time

already_pushed = []
loop_count = 0
pb_request_url = 'https://api.pushbullet.com/v2/pushes'
pb_request_body = {"type":"link"}
content_type = 'application/json'

target_subreddit = input("Which subreddit would you like to monitor?: ")
reddit_request_url = 'http://www.reddit.com/r/{0}/new.json?count=25&sort=new'.format(target_subreddit)

if 'access-token.txt' in os.listdir('.'):
    with open('access-token.txt', 'r') as token_file:
        token_content = token_file.readlines()
        access_token = token_content[0]
else:
    print("It seems like you don't have a stored Pushbullet access token ... ")
    access_token = input("Access Token (Will be stored for future use): ")

    with open('access-token.txt', 'w+') as token_file:
        token_file.write(access_token)

authorization = 'Bearer {0}'.format(access_token)
pb_request_headers = {'Authorization': authorization, 'Content-Type': content_type}

print("====================================")
print("Monitoring Subreddit - " + target_subreddit)
print("====================================")

while(True):
    reddit_response = requests.get(reddit_request_url, headers={'User-Agent': "PudditAgent"})
    reddit_response_json = json.loads(reddit_response.text)
    push_list = []

    for post in reddit_response_json['data']['children']:
        post_data = post['data']
        post_id = post_data['name']
        post_elasped_time = int(time.time()) - int(post_data['created_utc'])

        if post_elasped_time < 300 and post_id not in already_pushed:
            post_title = post_data['title']
            post_url = post_data['url']
            post_text = post_data['selftext']
            push_list.append((post_id, post_title, post_url, post_text))
            already_pushed.append(post_id)

    for post in push_list:
        pb_request_body['title'] = post[1]
        pb_request_body['url'] = post[2]
        pb_request_body['body'] = post[3]
        requests.post(pb_request_url, headers=pb_request_headers, data=json.dumps(pb_request_body))
        print("* New Post! - " + post[1])
        print("  " + post[2])
        print("")

    loop_count += 1
    time.sleep(5)

    if loop_count > 500:
        already_pushed = []
        loop_count = 0

