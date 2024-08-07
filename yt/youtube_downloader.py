from pytube import YouTube

link = input('Enter the Youtube Video URL:')
try:
    yt = YouTube(link)
    mp4_streams = yt.streams.filter(file_extension='mp4').all()
    chosen_stream = mp4_streams[-1]
    SAVE_PATH = "D:/Downloads"
    chosen_stream.download(output_path=SAVE_PATH)
    print('Video downloaded successfully!')
except Exception as e:
    print(f"error: {e}")

print('Video URL:', link)

