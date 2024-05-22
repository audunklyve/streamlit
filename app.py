import streamlit as st

from gradio_client import Client

client = Client("https://11329a4dd2bac10b83.gradio.live/demo/")
result = client.predict(
		"https://super-duper-orbit-pg7v9x9r44p2r56r-8501.app.github.dev/assets/kennedy-video.mp4",	# str (filepath on your computer (or URL) of file) in 'Video or Image' File component
		"https://super-duper-orbit-pg7v9x9r44p2r56r-8501.app.github.dev/assets/Kvinne-Deep-fake-e.wav",	# str (filepath on your computer (or URL) of file) in 'Audio' File component
		"wav2lip",	# str  in 'Checkpoint' Radio component
		True,	# bool  in 'No Smooth' Checkbox component
		1,	# int | float (numeric value between 1 and 4) in 'Resize Factor' Slider component
		0,	# int | float (numeric value between 0 and 50) in 'Pad Top' Slider component
		10,	# int | float (numeric value between 0 and 50) in 'Pad Bottom (Often increasing this to 20 allows chin to be included' Slider component
		0,	# int | float (numeric value between 0 and 50) in 'Pad Left' Slider component
		0,	# int | float (numeric value between 0 and 50) in 'Pad Right' Slider component
		api_name="/Wav2Lip"
)
print(result)
