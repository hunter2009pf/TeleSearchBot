import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    filename="app.log",  # 指定日志文件名
    filemode="a",
)  # 追加模式

logger = logging.getLogger(__name__)  # 创建logger对象
logger.info("Logger instance is creaetd successfully")  # 记录日志信息
