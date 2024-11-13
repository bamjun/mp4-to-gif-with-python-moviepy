import argparse
from moviepy.editor import VideoFileClip

mp4_file = 'test.mp4'
gif_file = 'result_file/test.gif'

# Add argument parsing for resolution selection
parser = argparse.ArgumentParser(description='Select video resolution.')
parser.add_argument('--resolution', type=int, choices=[1, 2], required=True,
                    help='Choose resolution: 1 for 320x240, 2 for 640x480')
args = parser.parse_args()

# Set resolution based on user input
if args.resolution == 1:
    new_size = (320, 240)
elif args.resolution == 2:
    new_size = (640, 480)
elif args.resolution == 3:
    new_size = (1280, 720)
elif args.resolution == 4:
    new_size = (1920, 1080)

clip = VideoFileClip(mp4_file)
clip = clip.resize(newsize=new_size)
clip.write_videofile(gif_file, fps=3, codec='gif')
