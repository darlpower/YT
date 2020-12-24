from yt_concate.pipeline.steps.step import Step

class Postflights(Step):
    def process(self, data, inputs, utils, logger):
        logger.info('in Postflight')
