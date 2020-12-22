from pytube import YouTube

from yt_concate.pipeline.steps.step import Step

import time

class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        cnt = 0
        for url in data:
            print('正在下載', url)
            if utils.caption_file_exists(url):
                cnt += 1
                print('found existing caption file')
                continue

            try:
                yt = YouTube(url)
                en_caption = yt.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except AttributeError:
                print('Error when downloading caption for', url)
                print('影片本身可能沒有字幕，請確認', url)
                continue

            text_file = open(utils.get_caption_filepath(url), "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            # break

        end = time.time()
        print('took', end - start, 'seconds')

