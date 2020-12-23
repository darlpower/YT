from pytube import YouTube

from yt_concate.pipeline.steps.search import Step
from yt_concate.settings import VIDEOS_DIR

class DownloadVideos(Step):
    def process(self, data, inputs, utils):
        yt_set = set([found.yt for found in data])
        print('準備下載', len(yt_set), '部影片')

        for yt in yt_set:
            url = yt.url
            if utils.video_file_exists(yt):
                print(f'找到存在的影片{url}，跳過下載')
                continue

            print('正在下載', url)
            YouTube(url).streams.first().download(output_path=VIDEOS_DIR, filename=yt.id)

        return data