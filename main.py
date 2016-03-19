import getpass
from github3 import login

username = input('github username : ')
password = getpass.getpass('password for '+username+' : ')

gh = login(username, password=password)

followers = [str(f) for f in gh.iter_followers()]

for f in gh.iter_following():
    u = str(f)
    if not u in followers:
        not_follower = gh.user(u)
        print(not_follower,' is not following you, so unfollowed.')
        gh.unfollow(not_follower)
print('done.')
