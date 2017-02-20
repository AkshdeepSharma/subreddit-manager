import praw
import time
import pyperclip

#logs the bot into reddit servers
def bot_login():
    print ('Logging in..')
    reddit = praw.Reddit('WorldDudeMan', user_agent = "world news puller but I love cats")
    print ('Logged in.')
    return reddit

#the bot does stuff here    
def run_bot(reddit):
    print ('Obtaining 15 submissions.')
    for submission in reddit.subreddit('worldnews').new(limit=15):
        if "Trump" in submission.title:
            threadURL = submission.url
            threadTitle = submission.title
            file = open("worldnews.txt", 'a')
            pyperclip.copy(threadTitle + ' ')
            file.write(pyperclip.paste())
            pyperclip.copy(threadURL + '\n')
            file.write(pyperclip.paste())
            print ('Submission titled "' + str(threadTitle) + '" pasted')

    #Sleep for 1 minute
    print ('Sleeping for 1 hour. Zzz...')
    time.sleep(6000)
    
reddit = bot_login()
while True:
    run_bot(reddit)