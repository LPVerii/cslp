FROM python:3.10-slim

# ENV APP_HOME /app
# WORKDIR $APP_HOME
COPY . ./

RUN pip install -r requirements.txt

EXPOSE 1234
ENTRYPOINT ["python", "main.py"]
