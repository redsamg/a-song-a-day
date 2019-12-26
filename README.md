# a-song-a-day

This project is, first and foremost, a Christmas present. You'll need a Spotify account, and a Twilio account (links below).

tl;dr - use this app to send assorted Spotify tracks from any playlist to your friends/family via SMS

# Problem space: 

1) Someone that I know well is always wishing for me to share music with them.

2) With tight schedules and a glut of podcasts, songs, audiobooks, and additional auditory stimuli to choose from,
   it can be difficult to remember, choose... 
   well, whatever the excuse is, one often needs a reminder to listen to the music that has been reccomended.

# Solution:

This simple application ("simple" could be an understatement - "rudimentary" may also come to mind...) solves for the above problems, and is:

Simplifying <- a-song-a-day selects one random track from a playlist of your choice

Engaging <- the app is designed to text (SMS) the Spotify link to said track to any phone number you choose 

Hands-off <- the app (once hooked up to a server - I'm using the free version of pythonanywhere to schedule this task) is completely hands-off and will text on a schedule for you (another, less automated solution would be for the app to run on your local machine at log-in)

# Next Steps:

As a next step, I am looking to incorporate user feedback into the app. Spotify already has user preference functionality built in, so I will be incorporating this logic into the track selection process, going forward.


Any and all feedback is welcomed and appreciated!

Oh, and I rely heavily on Spotify and Twilio to make this app run. Check them out, here: https://developer.spotify.com/, and here: https://www.twilio.com/console.
