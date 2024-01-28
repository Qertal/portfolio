docker build -t mysql_db .
docker run -p 4949:3306 -d mysql_db --secure-file-priv="/docker-entrypoint-initdb.d/"