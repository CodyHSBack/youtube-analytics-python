from youtube_statistics import YTstats

API_KEY = "AIzaSyCIR_ILZDNu-Yb8wj6i28ILJS2kQNL9qbk"

channel_id = input("Enter channel ID: ")

yt = YTstats(API_KEY, channel_id)
data = yt.get_channel_statistics()
print(data)