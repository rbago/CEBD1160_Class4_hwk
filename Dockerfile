FROM ubuntu:16.04
MAINTAINER Rafael Badillo-Gomez <https://github.com/rbago>

COPY housing.data.txt diabetes.tab.txt thecsvparser.py ./

RUN apt-get update \
    && apt-get install -y python3-pip \
    && python3 -m pip install numpy pandas

CMD ["python3", "thecsvparser.py"]
