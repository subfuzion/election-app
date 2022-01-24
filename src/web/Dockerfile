FROM pglet/server as SERVER

FROM python:3.10-alpine3.15
EXPOSE 8080
ENV PGLET_SERVER_PORT=8080
ENV PGLET_ALLOW_REMOTE_HOST_CLIENTS=true
ENV VOTE=http://vote

COPY --from=SERVER /pglet /usr/local/bin/pglet
RUN /usr/local/bin/pglet &

WORKDIR /app
ENV PYTHONPATH=/app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . .

ENTRYPOINT ["python", "votingapp/app.py"]
