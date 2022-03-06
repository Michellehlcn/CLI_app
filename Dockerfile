
FROM python:3.8.6
WORKDIR /pycli
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 8501
COPY . /pycli
CMD python3 run __main__.py