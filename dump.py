# from transformers import pipeline

# # Load pre-trained sentiment analysis model
# model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# # Classify the sentiment of a text
# text = "I love this product, it's amazing!"
# result = model(text)[0]

# # Labels: 0 -> Negative; 1 -> Neutral; 2 -> Positive
# print(f"Sentiment: {result['label']}, Score: {result['score']}")
# print(result)



# import requests

# url = "https://amazon23.p.rapidapi.com/reviews"

# querystring = {"asin":"B08P3QVFMK","sort_by":"helpful","country":"US"}

# headers = {
# 	"X-RapidAPI-Key": "e3fddeab38msh1aaaa0444d7b726p1c10e3jsn22b1c149fa9e",
# 	"X-RapidAPI-Host": "amazon23.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)
# with open(r"data.json", "w") as f:
#     f.write(response.text)


import evaluator
import json
# review = "I purchased one of these for my girlfriend for an early Christmas present. I was pretty happy she had spoken about purchasing a bit larger TV for her home and I was just the guy to make that happen. It�s always nice when you�re buying a present for yourself as well as your person. It�s pretty hard watching your team on a 40 inch Insignia when you have a beautiful 65 inch Samsung and an awesome sound system at home. I couldn�t let her do this on her own�Lol!She had some specific criteria about what she wanted even though she didn�t know I was going to do this for HER. 55 inch was as large as she would go and she doesn�t like �clutter�. We obviously need better sound than an old, crappy, no name soundbar as well so we�ll go for the whole show with the Echo Studio speakers and I had an Echo Sub still in the box I didn�t really use. She already had an Echo Show that she loves, so this should be a no brainer, right?The speakers had already been here for a week when the TV arrived Thursday I put them all under her tree before she got home from work. I wasn�t waiting until Christmas, the next game was on Sunday. The speakers were first that evening and they worked mostly as expected. My initial impressions were good, much better than my old Echo�s although speakers that size aren�t really in the same class as my four old Kef 104/2�s that I have loved since new back in �87. Much less �clutter� though and they really do sound pretty good.On Friday it was time for the initial setup of the TV and of course you have to un-pair the speakers in order to set up a �Home Theater�. That seems a bit over the top, these things are supposed to work together, right? Ok, step by step I guess. I get it set up and the sound is coming out of the speakers. We sit down with a beer and listen to some music and all is good.On Saturday morning, it�s time to get serious and down comes the old Insignia and the rest of the �clutter� and up goes the new TV. When I turn it on, there is no sound coming from the speakers. Hmm! I tried lots of commands to Alexa and nothing worked. Couldn�t find anything in the app or online to help. Between Friday night and Saturday morning I did one factory reset on the TV and many multiple un-pairing and re-pairing of the TV and the speakers. The only thing I found that would work for me was to go into settings and do a restart. The factory reset requires you to start over from the beginning but the restart at least keeps your settings. Cycling power alone doesn�t help. The biggest problem with the restart is it has to re-calibrate the Home Theater settings which takes about five minutes and part of that time will be without sound as well.This can�t be that hard. This should be one of the easiest TV�s ever made to set up and use. I have to be missing something but every time I ask Alexa to play music, the speakers won�t switch back to playing sound from the TV no matter what I tried.After I killed the whole morning messing with it, I had to leave so I got it back to the point it was usable with her Apple TV and I told her not to use the A word or it might quit working. Just leave the remote alone also. Saturday evening, I had the same results, couldn�t find any way to fix it. Watched A Star is Born on HBO Max on her Apple TV through this system. Very enjoyable�great movie.Sunday morning, I decided to search the internet for people who might have been having a similar problem but couldn�t find anything. It�s getting close to game time and I need it working. I probably should have just left it alone but I�m determined. I managed to break it one last time just before the game started so I un-paired everything and turned on the TV speaker because I didn�t have time to set it back up again. The TV speaker option isn�t available if you have it paired with the Home Theater, thanks Amazon. The TV speaker isn�t bad for a TV speaker but it�s not exactly what I paid for.Sunday evening, I decided I am probably going to have to send the TV back. I hate returning things but on top of the other problems, the menu is glitchy. At times it will slow down and get to the point of freezing completely. Cycling power at least fixes that temporarily. The TV updated to the latest software as soon as it connected to the internet so you wouldn�t think that would be a problem. It�s not like this tv hasn�t been out long enough to fix most of the bugs. Maybe I just got a bad one. Overall, I would say the picture is fine and when working the sound was great but I�ve never had this many problems with a TV out of the box. When you plug them in, they work. They might need some adjustments but they generally work as advertised. I�ve given it enough of my time this weekend to even think about more hours spent with tech support or waiting on software updates.Monday I purchased a Fire TV Cube and a different TV. Guess what�it worked correctly out of the box. The Apple TV will turn the whole system on when you hit the menu button on the apple remote and the sound plays on the Echo Studios. The Fire TV remote will control the Apple TV. If you hook your HDMI cable to ARC input on the TV, the sound from the TV will play from the Echo Studios also. The concept actually works really well when you pair a Fire TV with Echo Studio�s in a Home Theater setup. Too bad I ended up adding to the clutter. At least it�s pretty small. The Fire TV experience is good and I could probably eliminate the Apple TV but we have already downloaded all the apps she wants and have all the sign in information on it. Besides, we�re both used to and like the interface.I probably just got a bad TV. There are plenty of good reviews here. This one would have been fine hooked up to my system at home. I liked the menus and they were pretty fast when I wasn�t switching apps and inputs every 5 seconds trying to get the speakers to respond correctly. The cube makes me believe I probably just got a bad TV for some reason. I�ll give it a 3."
text = "Tv is great. It's huge and has a nice picture. It's not OLED but in a dark room it does well. There�s nothing cheap about the tv and if you are familiar with their fire stick this tv will be a breeze to operate.You do have to make your picture adjustments once on all the hdmi inputs you�ve got and many of the apps you�ve got as well. Just check the picture by holding down the home button until a side menu appears and scroll down to picture. Here you�ve got plenty of ability to tweak to your liking.Now the one bad thing. I have to restart the tv everytime I turn it on for the audio to work. I have a Dolby Atmos setup and use an Apple TV to stream content in Atmos that Amazon cannot.Once I restart it�s fine and only takes a moment to do. I wish I didn�t have to deal with that but other than that the sound coming out of my surround speakers is as expected.The Alexa feature is really easy to deal with and works as well as their other devices. You can turn the Led light off in the settings. Also, I�ve not seen any bloat ware on this TV or had to suffer through any ads outside the normal stuff you get on a fire stick."
text = text.replace("\ufffd", "")

result1 = evaluator.evaluate(text)

max_score = max(result1, key = lambda i: i[1])[1]

# result1 = list(filter(lambda i: i[1] == max_score, result1))

json.dump(result1, open('out/result.json', 'w'), indent=4)


# result2 = evaluator.evaluate_full_text(text)
# json.dump(result2, open('result_2.json', 'w'), indent=4)