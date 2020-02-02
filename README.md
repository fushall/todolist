# todolist

## build & run docker container(构建并运行docker容器)
    docker-compose build && docker-compose run

## or pull the docker image from docker hub (或者从docker hub上拉镜像)
    docker pull fushall/todolist:0.0.1
    docker run -p 6066:6066 fushall/todolist:0.0.1

## or run directly via `flask run` command（或者直接通过`flask run`命令运行）
The best practice to start the app is that, run following commands 
with a new python virtual environment.
用这种方式启动服务的好方法是，在新的虚拟python环境中运行下面的命令。

    pip install  -i https://mirrors.aliyun.com/pypi/simple -r requirements.txt
    export FLASK_APP=web  # on windows `set FLASK_APP=web` 
    flask run --eager-loading --port 6066

## to browser the following url to use todolist (浏览下面网址来使用todolist)
    http://127.0.0.1:6066/