FROM alpine AS base

COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

#Multistage
FROM python:3.7-alpine
COPY --from=base /app/app.py .
COPY --from=base /app/requirements.txt .  

RUN apk add --no-cache gcc musl-dev linux-headers curl mysql-client mysql-dev
RUN pip install -r requirements.txt

# ENV FLASK_APP=app.py
# ENV FLASK_ENV=development
# ENV FLASK_RUN_HOST=0.0.0.0
# ENV MYSQL_USER=mycontador
# ENV MYSQL_PASSWORD=ositodepeluche
# ENV MYSQL_HOST=mysql-db
# ENV MYSQL_DB=mysql-database

EXPOSE 5000

CMD flask run


