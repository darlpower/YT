from yt_concate.pipeline.steps.step import Step

class Preflights(Step):
    def process(self, data, inputs, utils, logger):
        logger.info('in Preflight')
        utils.create_dirs()