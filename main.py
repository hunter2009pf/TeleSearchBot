from config.env_paras import EnvParas
from utils.log_util import logger
from api import start_service


if __name__ == "__main__":
    EnvParas.get_env()
    start_service()
    logger.info("服务已启动")
