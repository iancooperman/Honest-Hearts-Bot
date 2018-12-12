import praw
import pdb
import re
from pathlib import Path
from time import sleep

password = input("Please enter the password: ")

text_file_path = Path.cwd()/Path("text-file/posts_replied_to.txt")
print(text_file_path)

if not Path.exists(text_file_path):
    posts_replied_to = []
else:
    with open(text_file_path, "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))

reddit = praw.Reddit(client_id='RqH3jJN2UOd5ZQ',
                     client_secret='CHbwP2-IiKYMEvruOVMhTFxyeBE',
                     password=password,
                     username='honest_hearts_bot',
                     user_agent='Honest Hearts Bot alpha 1')

subreddit_name = "testingground4bots" # Bot testing ground
#subreddit_name = "EarthPorn"

subreddit = reddit.subreddit(subreddit_name)  # change this to 'EarthPorn' before releasing

print("Logged in.")


while True:
    for submission in subreddit.new(limit=5):
        if re.search("Zion", submission.title, re.IGNORECASE) and submission.id not in posts_replied_to:
            print("Bot replying to:", submission.title, "\nPost ID:", submission.id, "\n")
            submission.reply("something something Honest Hearts\n\n___\n\n^I ^am ^a ^bot ^in ^training. ^This ^action ^was ^performed ^automatically, ^but ^not ^necessarily ^relevantly. ^beep ^boop. ")
            posts_replied_to.append(submission.id)

    with open(text_file_path, "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")

    sleep(60)
