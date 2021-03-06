FROM python:3.8.3-slim
WORKDIR /opt/flaskapp


RUN apt update && apt install -y curl build-essential unixodbc-dev unixodbc gettext-base
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt update && ACCEPT_EULA=Y apt install -y msodbcsql17 mssql-tools
ENV PATH="$PATH:/opt/mssql-tools/bin"

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app.py .
COPY templates/ ./templates/
COPY static/ ./static/
COPY particle/ ./particle/
COPY tools/ ./tools/
COPY config.tmpl .
COPY entrypoint.sh .
EXPOSE "5000/tcp"
ENTRYPOINT ["./entrypoint.sh"]
