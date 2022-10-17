# Youtube-Music-Playlist-Sender.

## Back story

I have been using my Wethinkcode email to listen to music on youtube music.
Since we are leaving soon. I have decided to create a program that
sends all my playlists from my school account to my personal account. noice!!

## How use to use
It is not entirely user friendly but we are developers so yeah...

    * Run the app.py script
    * You will be asked to enter credentials. How do you find the credetials you ask?
 
#### Firefox
    * Verify that the request looks like this: Status 200, Method POST, Domain music.youtube.com, File browse?...
    * Copy the request headers (right click > copy > copy request headers)

#### Chromium (Chrome/Edge)
    * Verify that the request looks like this: Status 200, Name browse?...
    * Click on the Name of any matching request. In the “Headers” tab, scroll to the section “Request headers” and copy everything starting from “accept: */*” to the end of the section


Please help me improve my application.

Here is the documentation I used to create this application
https://ytmusicapi.readthedocs.io/en/stable/

