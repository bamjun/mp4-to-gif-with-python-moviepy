from moviepy.editor import VideoFileClip

mp4_file = 'test.mp4'
gif_file = 'test.gif'

clip = VideoFileClip(mp4_file)
clip.write_videofile(gif_file, fps=10, codec='gif')
