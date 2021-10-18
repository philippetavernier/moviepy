# Import everything needed to edit video clips 
from moviepy.editor import *

img = ['output-raspberry-3.jpg']
clips = [ImageClip(m).set_duration(2)
      for m in img]
clip1 = concatenate_videoclips(clips, method="compose")
# loading video dsa gfg intro video 
#clip1 = VideoFileClip("output-raspberry-3.mp4")
clip2 = VideoFileClip("test1.mp4")
clip3 = VideoFileClip("test2.mp4")
#clip4 = VideoFileClip("raspberry-influx-temperature-ok-recording-data.mp4")


# speedup clip2
#clip2_speed= clip2.fx(vfx.speedx, 2)
clip3_speed= clip3.fx(vfx.speedx, 2)

final = concatenate_videoclips([clip1, clip2, clip3_speed], method="compose") 

#concat_clip = concatenate_videoclips(clips, method="compose")
final.write_videofile("output-rasp-3.mp4", fps=24)
