FROM python:3.8.8-slim
WORKDIR /app
COPY . .
RUN apt-get update && apt-get install build-essential iputils-ping -y
RUN chmod +x *.sh
RUN pip install -r requirements.txt
ENTRYPOINT ["/app/entrypoint.sh"]
EXPOSE 80


