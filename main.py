import sys

if len(sys.argv) < 4:
   print("ERROR", "Input shut be in format main.py <json_path> <video_path> <covers_path>")
   exit(1)
paths = {
   "json": sys.argv[1],
   "video": sys.argv[2],
   "covers": sys.argv[3]
}

