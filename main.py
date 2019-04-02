from sultan.api import Sultan
import time

s = Sultan()

account_names = ["","",""]
account_keys = ["","",""]
file_input = "file.mp4"
for stream_key in account_keys:
    command = "ffmpeg -re -i " + file_input + """ -vcodec libx264 -profile:v main -preset:v medium -r 30 -g 60 -keyint_min 60 -sc_threshold 0 -b:v 2500k -maxrate 2500k -bufsize 2500k -filter:v scale="trunc(oh*a/2)*2:720" -sws_flags lanczos+accurate_rnd -acodec aac -strict -2 -b:a 96k -ar 48000 -ac 2 -f flv rtmp://live.twitch.tv/app/""" + stream_key
    s.sudo(command).run()
    index = account_keys.index(stream_key)
    print("Streamed on" + account_names[index])
    time.sleep(86400)
