FROM python:3.7-slim

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ -r /requirements.txt \
    && rm -rf /tmp \
    && rm -rf ~/.cache/pip/wheels \
    && echo 'Asia/Shanghai' >/etc/timezone \
    && export TZ='Asia/Shanghai'

COPY . /todolist/
WORKDIR /todolist
CMD gunicorn -b 0.0.0.0:6066 --log-level info --access-logfile - web:app
