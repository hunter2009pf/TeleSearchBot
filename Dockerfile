FROM python:3.12

WORKDIR /telesearchbot

COPY . .

# 设置python国内镜像
RUN python3 --version
RUN python3 -m pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
# RUN python3 -m pip install diffusers-0.25.0-py3-none-any.whl
RUN python3 -m pip install -r requirements.txt

CMD ["python", "main.py"]
