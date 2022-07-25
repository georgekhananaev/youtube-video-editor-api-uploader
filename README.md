![alt text](http://repository-images.githubusercontent.com/517701519/e88551b1-0411-4113-8bde-beff910047a9)

# Python3 Video Editor + YouTube API Uploader
This Python3 code allows you to add intro + outro + logo + upload complete video, including all video details to YouTube by single click.

## What exactly is this script doing?
It calls two main functions Video Editor and then Video Uploader.  
<br/> 
Note: you can disable editor or uploader in case you want to use just single function in start_process(), simply add "#" before the call row.

### Here is complete steps:
#### Video Editor
1.  Adding intro clip (replace intro.mp4 with your own file)
2.  Adding logo (any gif file or edit the code for png, jpg formats)
3.  Adding outro clip (replace outro.mp4 with your own file)

#### Video Uploader
1.  Uploading Video (uploading edited file)
2.  Adding Title
3.  Adding Complete Description + urls + emojis + tags + any info you desire
4.  Adding tags
5.  Video will be "Private", edit status manually once uploaded. Note: you can't upload with API as public. Unless you pass audit with google
6.  Uploading thumbnail photo (YouTube account must be confirmed)


## How to use?
1. Use Python 3.10 or newer
2. Install all python packages (in case of an issue, see my requirements.txt, install equal versions), maybe moviepy will require to install imagemagick (https://imagemagick.org/script/download.php), I originally wrote this code for much larger project and can't remember if it was required for the logo editing.
3. Create clould project, install YouTube Data API v3. Can do it at: https://console.cloud.google.com, I will upload complete video tutorial soon.
4. Download OAuth client secrets file from google clouds, rename it to: "client_secrets.json" and place it in the root folder.
5. Run main.py
6. Browser will be opened automaticlly. You will be aksed to approve the app by signing into your youtube account. Once approved, credentials will be saved to credentials.json, this is temporary file in the root folder. This is 1 time process basiclly and you won't be asked again. Unless your credentials expired or you want to change the youtube account, if so then simply remove the credentials.json file and re-do the approval.
<br/>
Note: All file locations, directories, video details can be edited in videoDetails.py, I added sample files but please don't use these for production beyong testings.

## Can you help me? I want to integrate it into my project?
#### Short answer, yes. 
But it depents on how much time it will require. If you need my help, you can contact me on linkdin: https://www.linkedin.com/in/georgekhananaev/

## Limitations
By default your app will be restricted to 10000 quotas a day. It takes 1600 quotas to upload a single video. Which means you can upload just 6 videos a day.
You can't post videos as "public" direclty by API. Which means once video is uploaded, you must log into your youtube account and then change the status to "public" manually, if you want to publish it. Otherwise it will stay private to you.
#### To lift these limitations as shown above, you must do audit with google, url: https://support.google.com/code/contact/oauth_quota_increase
You can bypass 2nd limitation by creating a script with Selenium. (I won't help with this, find yourself)
You can upload more than 6 videos a day, if you upload simultanity from different apps(projects). However YouTube might consider this as a spam. I suggest you read the policy first.

#### This project has absolutly no warranty. Do not use it to create spam. Do not use it for any illegal activities. Please follow YouTube terms and policy.
