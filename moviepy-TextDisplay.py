from moviepy.editor import *


# MAKE THE TITLE SCREEN
## Make the text. Many more options are available.
txt_clip = (
	TextClip(
		"25th century dancing\n(hypothetical)",
		fontsize=70,
		font="Century-Schoolbook-Roman",
		color='white'
		)
             .margin(top=15, opacity=0)
             .set_position('center','top')
             .set_duration(10) )

title = (
    CompositeVideoClip([txt_clip])
    .fadein(0.5)
)


result = CompositeVideoClip([title]) # Overlay text on video
result.write_videofile("edited.webm",fps=25)
