# import Modules
from pytube import YouTube
import os
import sys
# url
url = YouTube(input("type your url here : "))
base_path = os.path.expanduser('~')
downloads_path = os.path.join(base_path, 'Downloads/output')
print('###############################################')
print('###############################################')


# choing formats
print('Choose your format : ')
print('For video format type 1')
print('For audio format type 2')
FormatType = int(input("... : > "))
formats = ['1080', '720', '480', '360']
if (FormatType == 1):
    print('Choose your video format :')
    for i, f in enumerate(formats):
        print(f'for {f} type :{i+1}')
    fvalue = int(input('... : '))
else:
    fvalue = 0

# main func


def do_FilteringStreams():
    if (FormatType == 1):
        stream1080 = url.streams.filter(progressive=True,
                                        file_extension='mp4').order_by('resolution').desc()
        stream720 = url.streams.filter(progressive=True,
                                       res="720p", mime_type="video/mp4", )
        stream480 = url.streams.filter(progressive=True,
                                       res="480p", mime_type="video/mp4", )
        stream360 = url.streams.filter(progressive=True,
                                       res="360p", mime_type="video/mp4", )
        if (fvalue == 1):
            try:
                stream1080.first().download(downloads_path)
                print("download done check " + downloads_path)
            except:
                print("Oops! That video can't download in 1080p. Try again lower Res...")
        elif (fvalue == 2):
            try:
                stream720.first().download(downloads_path)
                print("download done check " + downloads_path)
            except:
                print("Oops! That video can't download in 720p. Try again..")
        elif (fvalue == 3):
            try:
                stream480.first().download(downloads_path)
                print("download done check " + downloads_path)
            except:
                print("Oops! That video can't download in 480p. Try again...")
        elif (fvalue == 4):
            try:
                stream360.first().download(downloads_path)
                print("download done check " + downloads_path)
            except:
                print("Oops! That video can't download in 360p. Try again..")
        else:
            print("You didn't choose your format resolution")
    elif (FormatType == 2):
        audioStream = url.streams.filter(only_audio=True)
        try:
            out_file = audioStream.first().download(output_path=downloads_path)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print("download done check " + downloads_path)

        except:
            print("Oops! That audio can't be downloaded. Try again...")
    else:
        print('You chose the wrong option!')


# calling the main func
do_FilteringStreams()
print('###############################################')
os.system('cmd /k "PAUSE"')
os.system('cmd /k "EXIT"')

