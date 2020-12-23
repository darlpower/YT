import time

from pytube import YouTube

from yt_concate.pipeline.steps.step import Step


class DownloadCaptions(Step):
    def process(self, data, inputs, utils):
        start = time.time()
        cnt = 0
        for yt in data:
            print('正在下載', yt.id)
            if utils.caption_file_exists(yt):
                cnt += 1
                print('found existing caption file')
                continue

            try:
                source = YouTube(yt.url)
                en_caption = source.captions.get_by_language_code('a.en')
                en_caption_convert_to_srt = (en_caption.generate_srt_captions())
            except AttributeError:
                print('Error when downloading caption for', yt.url)
                print('影片本身可能沒有字幕，請確認', yt.url)
                continue

            text_file = open(yt.caption_filepath, "w", encoding='utf-8')
            text_file.write(en_caption_convert_to_srt)
            text_file.close()
            # break

        end = time.time()
        print('took', end - start, 'seconds')

        return data

