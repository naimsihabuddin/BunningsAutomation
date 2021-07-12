import logging


class LogGeneration:
    @staticmethod
    def log_generation():
        for handler in logging.root.handlers[:]:
            logging.root.removeHandler(handler)

        logging.basicConfig(filename='./Logs/automation.log',
                            filemode="w",
                            encoding='utf-8',
                            level=logging.INFO,
                            format="%(asctime)s: %(levelname)s %(message)s",
                            datefmt="%Y%m%d%H%M%S")
        logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logger
