from moviepy.editor import VideoFileClip
from moviepy.video.fx.all import speedx

input_path = "video.mp4"
output_path = "video_acelerado.mp4"
aceleracao = 1.429

video = VideoFileClip(input_path)
video_acelerado = video.fx(speedx, aceleracao)
video_acelerado.write_videofile(output_path, codec="libx264", audio_codec="aac")
