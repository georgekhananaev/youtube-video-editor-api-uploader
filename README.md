# Python YouTube Video Editor + API Uploader
This Python3 code allows you to add intro + outro + logo + upload complete video, including all video details to YouTube by single click.

## What exactly is this script doing?
It calls two main functions Video Editor and then Video Uploader.  
<br/> 
Note: you can disable editor or uploader in case you want to use just single function in start_process(), simple add "#" before the call row.

#### Here is complete steps:
Video Editor
1.  Adding intro clip
2.  Adding logo
3.  Adding outtro clip

Video Uploader
1.  Uploading Video
2.  Adding Title
3.  Adding Complete Description + Urls any info you desire
4.  Adding tags
5.  Video will be "Private", edit status manually once uploaded. Note: you can't upload with API as public. Unless you pass audit with google
6.  Uploading thumbnail photo (YouTube account must be confirmed)


## How to use?
1. Use Python 3.10 or newer
2. Install all python packages, maybe moviepy will require to install imagemagick (https://imagemagick.org/script/download.php).
3. Create YouTube App at: https://console.cloud.google.com, I will upload complete video tutorial soon.
4. Download client secrets file from google, rename it as "client_secrets.json" place it in the root folder.
5. Run main.py
<br/>
Note: All file locations, directories, video details can be edited in videoDetails.py, I added sample files but please don't use these for production beyong testings.

## Can you help me? I want to integrate it into my project?
Short answer, yes. But it depents on how much time it will require. If you need my help, you can contact me at linkdin (check my profile).
