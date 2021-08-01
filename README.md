# export-table-def

## docker コンテナで実行

```bash
docker run -e DATABASE=blog -e USER=root -e PASSWORD=root -e PORT=3306 -v ${PWD}/tsv:/tmp -v ${PWD}/script:/script mysql:5.7 sh /script/script.sh
docker run -v ${PWD}:/app python:alpine3.10 python3 /app/sql-md.py
```

## docker mysqlの再起動

```
service mysql start
```