import asyncio
from config.env_paras import EnvParas
from utils.log_util import logger
from api import start_service


if __name__ == "__main__":
    start_service()
    logger.info("Telegram Search Bot Service Start...")
