

# Python3 Video Editor + YouTube API Uploader
* Python3 based. 
* Combining main clip, intro clip + outro clip + logo into a single video file and saving it.
* Uploading to YouTube automatically the file with all pre-set details such as: title, description, keywords, thumbnail, etc...
* Made to save time, you can run the app multiple times simultaneity and uploading videos to different channels.

## Version 2.x.x (GUI Interface)

![alt text](https://raw.githubusercontent.com/Fixitpanda/youtube-video-editor-api-uploader/main/screenshorts/ver2.x.png)

## Version 1.x.x (Script only)
![alt text](https://raw.githubusercontent.com/Fixitpanda/youtube-video-editor-api-uploader/main/screenshorts/ver1.x.png)

#### Video Uploader
1.  Uploading Video (uploading edited file)
2.  Adding Title
3.  Adding Complete Description + urls + emojis + tags + any info you desire
4.  Adding tags
5.  Video will be "Private", edit status manually once uploaded. Note: you can't upload with API as public. Unless you pass audit with Google
6.  Uploading thumbnail photo (YouTube account must be confirmed)


## How to use?
1. Download and install Python 3.10 or newer if you don't have.
2. Install all python packages from requirements.txt, maybe moviepy will require to install imagemagick (https://imagemagick.org/script/download.php).
3. Get a secret key from Google:
   * Go to:  https://console.cloud.google.com
   * Create cloud project. 
   * Enable YouTube Data API v3.
   * Set a scope for YouTube video management.
   * Create oAuth 2.0 credential id for oAuth 2.0
   * Download secret key.
   * Video with tutorial: https://youtu.be/hDK-nksiyxk
4. Run main.py
5. Browser will be opened automatically (Ver 1.x). You will be asked to approve the app by signing to your YouTube account. Once approved, credentials will be saved to credentials.json, this is temporary file in the root folder. This is 1 time process basically, and you won't be asked again. Unless your credentials expired, or you want to change the YouTube account, if so then simply remove the credentials.json file and re-do the approval.
<br/>
Note: All file locations, directories, video details can be edited in videoDetails.py, I added sample files but please don't use these for production beyond testings.

## Can you help me? I want to integrate it into my project?
#### Short answer, yes. 
But it depends on how much time it will require. If you need my help, you can contact me on LinkedIn: https://www.linkedin.com/in/georgekhananaev/

## Limitations
By default, your app will be restricted to 10000 quotas a day. It takes 1600 quotas to upload a single video. Which means you can upload just 6 videos a day.
You can't post videos as "public" directly by API. Which means once video is uploaded, you must log into your YouTube account and then change the status to "public" manually, if you want to publish it. Otherwise, it will stay private to you.
#### To lift these limitations as shown above, you must do audit with google, url: https://support.google.com/code/contact/oauth_quota_increase
You can bypass 2nd limitation by creating a script with Selenium. (I won't help with this, find yourself)
You can upload more than 6 videos a day, if you upload simultaneity from different apps(projects). However, YouTube might consider this as a spam. I suggest you read the policy first.

#### This project has absolutely no warranty. Do not use it to create spam. Do not use it for any illegal activities. Please follow YouTube terms and policy.
