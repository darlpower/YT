from yt_concate.pipeline.steps.step import Step
from yt_concate.model.yt import YT


# 單元13
class InitializeYT(Step):
    def process(self, data, inputs, utils):
        return [YT(url) for url in data]
