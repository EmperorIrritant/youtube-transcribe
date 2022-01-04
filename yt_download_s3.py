import json
from pytube import YouTube

def lambda_handler(event, context):
	yt_video_urls = event["video_urls"].split("\n")[:5]
	lang = event['language'].strip()
	output_path = '/tmp/'

	for yt_video_url in yt_video_urls:
		yt_video= YouTube(yt_video_url)
		audio_streams = yt_video.streams.filter(only_audio=True)
		audio_qualities = [int(audio_stream.abr[:-4]) for audio_stream in audio_streams]
		max_quality_audio = audio_streams[audio_qualities.index(max(audio_qualities))]
