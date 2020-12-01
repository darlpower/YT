import json
import urllib.request
from yt_concate.settings import API_KEY  # 絕對路徑寫法
# from .settings import API_KEY 相對路徑寫法

CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"  # 全域變數，命名時全大寫


def get_all_video_in_channel(channel_id):
    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY,
                                                                                                        channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links


# youtube channel is 'https://www.youtube.com/user/nikhirschi'
video_list = get_all_video_in_channel(CHANNEL_ID)
print(len(video_list))
