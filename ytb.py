import pytube

select = input("Select audio or video: ")

url = input("Url video:")

# to use in termux or linux and the directory is not "C:" change to the desired location.
path= r'C:\Users\Administrator\Downloads\YTBDownloader'

def dvideo():
    pytube.YouTube(url).streams.get_highest_resolution().download(path)
    
def daudio():
    pytube.YouTube(url).streams.get_audio_only().download(path)
    
if select == "Video" or "video":
    dvideo()
if select == "Audio" or "audio":
    daudio()





