# myconfig.py:
import os
from googleapiclient.http import MediaFileUpload  # noqa

YOUR_CLIENT_SECRETS_FILE = './client_secrets.json'  # YOUR CLIENT SECRET, Download it from https://console.cloud.google.com


class YourEditor:

    # Default values (some will be overwritten by the Gui)
    fps = 60  # maximum frame peer second, final output video. change to whatever value to desire. the higher rate, the longer it takes to process the video.
    # Static directories
    raw_video_file = str('./Media/Video/your_video.mp4')   # your raw video file
    thumbnail_image = str('./Media/Video/sample_thumbnail.jpg')  # your YouTube thumbnail image
    video_file_out = str('./Media/Video/final_clip/your_video_edited.mp4')  # final result, just before uploading to your YouTube channel.
    video_dir = str('./Media/Video/')  # Final video output directory
    intro_file_location = str('./Media/Video/intro.mp4')  # intro clip
    outro_file_location = str('./Media/Video/outro.mp4')  # outro clip
    youtube_video_patch = str('./Media/Video/final_clip')  # this folder will be uploaded into YouTube.
    black_image_file = str(
        './Media/Images/black.png')  # sets the final output resolution, replace with 4k black picture, if you desire 4k output otherwise your video will be 1080p.
    logo_file = str('./Media/Images/logo.gif')  # you can use gif animations as logo!


class Video:
    static_description = """
This is a test description.
You can insert here whatever you want.
It will be displayed exactly the same way on YouTube.
It will be the rows structure too.
"""

    title = 'your_new_title'  # up to 100 characters
    category = "22"
    keywords = 'Tag1, Tag2, Tag3, Tag4, Tag4'
    # print(len(keywords)) # remove the hash before print, if you want to check how many characters entered. maximum allowed is 500

    privacyStatus = "private"

    @staticmethod
    def getFileName(type):
        for file in os.listdir(YourEditor.youtube_video_patch):
            if type == "video" and file.split(".", 1)[1] != "jpg":
                return file
                break  # noqa
            elif type == "thumbnail" and file.split(".", 1)[1] != "mp4":
                return file
                break  # noqa

    def insertThumbnail(self, youtube, videoId):  # noqa
        thumnailPath = YourEditor.youtube_video_patch + "/%s" % (self.getFileName("thumbnail"))

        request = youtube.thumbnails().set(
            videoId=videoId,
            media_body=MediaFileUpload(thumnailPath)
        )
        response = request.execute()
        print(response)
