![alt text](http://repository-images.githubusercontent.com/517701519/e88551b1-0411-4113-8bde-beff910047a9)

# Python3 Video Editor + YouTube API Uploader
This Python3 code allows you to add intro + outro + logo + upload complete video, including all video details to YouTube by single click.

## What exactly is this script doing?
It calls two main functions Video Editor and then Video Uploader.  
<br/> 
Note: you can disable editor or uploader in case you want to use just single function in start_process(), simple add "#" before the call row.

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
2. Install all python packages (in case of issue, see my requirements.txt), maybe moviepy will require to install imagemagick (https://imagemagick.org/script/download.php).
3. Create YouTube App at: https://console.cloud.google.com, I will upload complete video tutorial soon.
4. Download client secrets file from google, rename it as "client_secrets.json" place it in the root folder.
5. Run main.py
6. Browser will be opened automaticlly. You will be aksed to approve the app by signing into your youtube account. Once approved, credentials will be saved to credentials.json, this is temporary file in the root folder. This is 1 time process basiclly and you won't be asked again. Unless your credentials expired or you want to change the youtube account, if so then simply remove the credentials.json file and re-do the approval.
<br/>
Note: All file locations, directories, video details can be edited in videoDetails.py, I added sample files but please don't use these for production beyong testings.

## Can you help me? I want to integrate it into my project?
Short answer, yes. But it depents on how much time it will require. If you need my help, you can contact me at linkdin (check my profile).
