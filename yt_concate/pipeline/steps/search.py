from yt_concate.pipeline.steps.step import Step
from yt_concate.model.found import Found

#單元13
class Search(Step):
    def process(self, data, inputs, utils):
        search_word = inputs['search_word']

        found = []
        for yt in data:
            captions = yt.captions
            if not captions:
                continue
            for caption in captions:
                if search_word in caption:
                    time = captions[caption]
                    f = Found(yt, caption, time)
                    found.append(f)
        print('找到' + str(len(found)) + '部影片符合搜尋字串:' + search_word)
        return found