
import os
from moviepy.editor import *

projectName="output-install-docker"
videoFileName=projectName+".mp4"

cut0a="0:10"
cut0b='0:16'
cut1a='1:01'
cut1b='1:20'
cut2a='1:40'
cut2b='5:30'
cutEnd='5:46'
os.chdir('/home/phil/WORKING-DIR/movies')

clip1 = VideoFileClip(videoFileName).subclip('00:00',cut0a)  
clip1_speed= clip1.fx(vfx.speedx, 2)
clip2 = VideoFileClip(videoFileName).subclip(cut0b,cut1a)  
clip2_speed= clip2.fx(vfx.speedx, 2)
clip3 = VideoFileClip(videoFileName).subclip(cut1b,cut2a)  
clip3_speed= clip3.fx(vfx.speedx, 2)
clip4 = VideoFileClip(videoFileName).subclip(cut2b,cutEnd)  
clip4_speed= clip2.fx(vfx.speedx, 2)
####

final = concatenate_videoclips([clip1_speed, clip2_speed, clip3_speed,clip4], method="compose") 
#concat_clip = concatenate_videoclips(clips, method="compose")

final.write_videofile(projectName+"final-speed"+".mp4", fps=24)


