# export-table-def

## mysqlの定義を書き出す

```bash
docker run -it --rm -v ${PWD}/tsv:/tmp -v ${PWD}/script:/script mysql:5.7 /bin/bash
# cd /script
# sh script.sh
```