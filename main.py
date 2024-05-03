import sys
import json
import os
from moviepy.editor import VideoFileClip

event_name = "Hudební týden 2023"

if len(sys.argv) < 3:
    print("ERROR", "Input shut be in format main.py <json_path> <video_path>")
    exit(1)
paths = {
    "json": sys.argv[1],
    "video": sys.argv[2]
}

with open(paths["json"], "r", encoding="utf-8") as f:
    data = json.loads(f.read())

# create folder for output videos
output_folder_path = "out"
if not os.path.exists(output_folder_path): 
    os.makedirs(output_folder_path) 

# generate videos by json
with VideoFileClip("video.mov") as v:
    for i in range(len(data)):
        song = data[i]
        
        # check parameters
        if song["start_time"] < 0 or song["start_time"] > v.duration:
            print("ERROR: start_time is out of the video timeline!")
            exit(1)
        if song["end_time"] < 0 or song["end_time"] > v.duration:
            print("ERROR: end_time is out of the video timeline!")
            exit(1)

        # trim video
        subclip = v.subclip(song["start_time"], song["end_time"])
        
        if "artist" in song:
            video_path = f"{output_folder_path}/{song["name"]} ({song["artist"]}) - {event_name}.mp4"
        else:
            video_path = f"{output_folder_path}/{song["name"]} - {event_name}.mp4"
        subclip.write_videofile(video_path)