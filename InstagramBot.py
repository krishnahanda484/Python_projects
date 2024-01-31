from instabot import Bot
#project made with pylance
bot=Bot()
bot.login(username='krishnahanda.ai',password='B**********d')
bot.follow('Instagram')
bot.upload_photo("C:/Users/pc/Pictures/Screenshots/Screenshot 2024-01-25 200657.png",caption="This is my project")
bot.unfollow('Instagram')
bot.send_message("I Love Python",['__mukul____._','g.aura.v__01'])#__mukul____._ and g.aura.v__01 are my friends from following
followers=bot.get_user_followers("krishnahanda.ai")
for follower in followers:
    print(bot.get_user_info(follower))
following=bot.get_user_following("krishnahanda.ai")
for Following in following:
    print(bot.get_user_info)
