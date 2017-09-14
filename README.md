# Reddit_Bot
A reddit bot that let's you pull post titles and urls from subreddits and repost it back to a private sub.

To use:
Include a praw.ini file in the project folder with the following format: 

--

[name]

username=

password=

client_id=

client_secret=

--

Where username/password are your reddit username and password, and client_id and client_secret are your reddit application's personal use
script code and secret code. This will make sure your credentials aren't in your main program. Make sure you replace [WorldDudeMan] with
whatever you decide to name your bot.

* Include a .txt file in your project folder. Make sure to replace 'subredditlinks.txt' with the name of your .txt file.

* Copy+paste the subreddit search function as many times as you need for each subreddit you wish to get links from (inside the while loop. You may also upload the script server side like digitalocean or amazon aws so it doesn't have to run on a local machine).

* Change the keywords you'd like to include in your submission titles (for example, this bot uses 'Trump' as a keyword in
/r/worldnews).

*Note, in-depth instructions are included in the commenting of the python script.*

Enjoy the bot!
