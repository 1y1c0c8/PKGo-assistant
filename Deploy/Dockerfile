FROM python:3.7

WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# COPY {Local fileName} {fileName in Docker}
COPY app.py /app/app.py 
COPY pkmgo_assistant.py /app/pkmgo_assistant.py
COPY ./static /app/static

ENV PATH=/home/app/.local/bin:$PATH
ENV PATH=$PATH:/user/local/python3/bin:$PATH

# CMD ["cd", "/app"]
# CMD ["ls", "-l"]
CMD ["gunicorn", "app:app"]
# CMD ["python3", "/app/app.py"]

# FROM ubuntu

# RUN apt update
# RUN apt install python3-pip -y
# RUN pip3 install Flask
# RUN pip3 install beautifulsoup4, geobatchpy, geographiclib, geopy, graphviz, line-bot-sdk, python-dotenv, requests, transitions

# WORKDIR /app
# COPY . .
# CMD [ "python3", "-m", "flask", "run"]