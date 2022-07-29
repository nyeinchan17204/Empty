FROM python:3.9.1-buster


RUN pip3 install --upgrade pip setuptools

RUN pip install -U -r requirements.txt

# Starting Worker
CMD ["python3","test.py"]
