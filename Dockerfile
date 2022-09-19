FROM python:3.9
ENV PYTHONUNBUFFERED=1
RUN apt update && apt -y install mariadb-client
RUN mkdir /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x /app/docker-entrypoint.sh
EXPOSE 8000
CMD ["/app/docker-entrypoint.sh"]
