from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.download_caption import DownloadCaptions
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils
from yt_concate.pipeline.steps.preflight import Preflights
from yt_concate.pipeline.steps.postflight import Postflights

#CHANNEL_ID = "UCKSVUHI9rbbkXhvAXK-2uxA"
CHANNEL_ID ='UCIldsycnma5sHR1VRP38vhg'

def main():
    inputs = {
        'channel_id': CHANNEL_ID,
    }
    steps = [
        Preflights(),
        GetVideoList(),
        DownloadCaptions(),
        Postflights(),
    ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)

if __name__ == '__main__':
    main()
