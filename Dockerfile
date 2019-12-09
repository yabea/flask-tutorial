FROM ubuntu:16.04

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo "Asia/Shanghai" > /etc/timezone
RUN apt update && apt install -y iputils-ping python3 python3-pip python3-tk libffi-dev libssl-dev
RUN apt install -y nginx && pip3 install uwsgi


ADD ['./', "/app"]
ADD ['./build', "/app"]
WORKDIR /app

RUN pip3 install -r requirements.txt

RUN chmod + x start_script.sh
CMD ['/start_script.sh']
