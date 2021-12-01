# start from base
FROM python:3.8
LABEL maintainer="ernest.lassman.kayembe@hotmail.com"
# We copy just the requirements.txt first to leverage Docker cache
WORKDIR /app
# install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
# copy sourcecode
COPY appRuntimeMonitor.log .
COPY filemanagement.py /app
COPY answer_file.json /app
COPY main.py /app
COPY build_json_file.py /app
COPY calculator_mw.py /app
COPY templates /app/templates
COPY static   /app/static
CMD ["python", "/app/main.py"]
