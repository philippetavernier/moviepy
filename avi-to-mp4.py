import moviepy.editor as moviepy

clip = moviepy.VideoFileClip("clip.avi")
clip.write_videofile("clio.mp4")
