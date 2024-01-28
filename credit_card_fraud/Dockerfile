FROM mysql:latest
ENV MYSQL_ROOT_PASSWORD=root
COPY banktest.sql /docker-entrypoint-initdb.d/
COPY test.csv /docker-entrypoint-initdb.d/