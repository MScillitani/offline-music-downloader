from pytube import YouTube


def download(url):  # download function
    youtube_music = YouTube(url)  # sets to the user-input URL
    youtube_music = youtube_music.streams.get_audio_only()  # specifies audio
    try:
        youtube_music.download()  # attempts to download YouTube audio
    except IOError:
        print("Something went wrong. Try again.")
    print("Download successful")


user_url = input("Enter YouTube URL: ")  # gets YouTube URL from user
download(user_url)  # downloads audio file to location specified in download function

