## Video Porter
It supports douyu.com by now

list.txt saves the downloaded video links

change the initial url in main.py before use

to start:
```
python main.py 
```

it will automatically detect downloaded links and check for video updates on given link. 

Before upload, if video not in youtube-supported format, use 
```
python converter.py inputvideo outputvideo.mp4
``` 
To upload:
```
python youtube_uploader.py folder_dir/
```


## Dependencies
[you-get](https://github.com/soimort/you-get)

[youtube-upload](https://github.com/tokland/youtube-upload)
