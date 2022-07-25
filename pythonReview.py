def create_youtube_video(title,description):
	video = {"Title": title, "Description": description, "Likes": 0, "Dislikes": 0, "Comments":{}}
	return video

def likes(video):
	if "Likes" in video:
		video["Liked"]+=1
	return video

def dislikes(video):
	if "Dislikes" in video:
		video["Dislikes"]+=1
	return video

def add_comment(video,Username,comment_text):
	video["Comments"] += {Username:comment_text}
	return video