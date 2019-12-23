# a-song-a-day
A song a day keeps the doctor away... 

This project is, first and foremost, a Christmas present.

# Problem space: 

1) Someone close to me is always wishing for me to share music them.

2) With a tight schedule and a glut of podcasts, songs, audiobooks, and additional auditory stimuli that exist in said individual's life,
   it can be difficult for them to remember, choose... 
   well - whatever the excuse is - they often do not listen to the music that has been reccomended to them.

# Solution:

This simple application ("simple" could be an understatement - "rudimentary" may also come to mind...) solves for the above problems by:

Selecting one, random track from any playlist of your choice and texting the appropriate Spotify track link to anyone you like.
I have used Twilio for the text messaging service API (as you'll see in the .py), and an AWS EC2 instance for scheduling and running the app.
Currently, I have several family members and friends who recieve a song a day from me, every morning during their commute (without any effort on my end..!).

Any and all feedback is welcomed and appreciated!

Oh, and I rely heavily on Spotify and Twilio to make this app run. Check them out, here: https://developer.spotify.com/, and here: https://www.twilio.com/console.
