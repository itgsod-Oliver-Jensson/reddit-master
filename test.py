from reddit  import client
from reddit.user import User
from reddit.reddits import Subreddit
from reddit.post import Post
from reddit.check import Check

bojohan = client.login('olliebot123')

# python = Subreddit("python")
#
# python.hot()


## Super bra kod

sub = Subreddit("atheism")

p = Post(sub.hot_children()[0])

ch = Check(p.title())

if ch.check_if_title_is_cool():
    print("Cool text found!!! x XXxXxXx")








