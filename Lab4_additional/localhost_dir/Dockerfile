FROM python:3
WORKDIR /opt
ADD Lab2.py tree.py /
RUN python3 -m venv env
CMD ['source', 'env/bin/activate']
ENTRYPOINT ["python3", "/Lab2.py"]