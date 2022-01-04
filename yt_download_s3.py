import json

def lambda_handler(event, context):
	yt_video_urls = event["video_urls"].split("\n")[:5]
	lang = event['language'].strip()
	output_path = '/tmp/'
