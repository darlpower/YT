import logging

from yt_concate.pipeline.steps.preflight import Preflights
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.download_caption import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_videos import EditVideo
from yt_concate.pipeline.steps.postflight import Postflights
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils

# CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"


CHANNEL_ID ='UCIldsycnma5sHR1VRP38vhg'
def config_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')  # 要記錄的格式
    file_handler = logging.FileHandler('yt-contact.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.WARNING)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 20,
    }
    steps = [
        Preflights(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaption(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflights(),
    ]

    logger = config_logger()
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils, logger)


if __name__ == '__main__':
    main()
