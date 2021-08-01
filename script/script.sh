#!/bin/bash

db_name=
user=
pw=

mysql -h host.docker.internal -P 3307 -u ${user} -p${pw} ${db_name} -e 'show tables;' > ./list.txt

sed -i '1d' list.txt

while read line
do
    mysql -h host.docker.internal -P 3307 -u ${user} -p${pw} ${db_name} -e "desc ${line};" > /tmp/${line}_desc.tsv
    mysql -h host.docker.internal -P 3307 -u ${user} -p${pw} ${db_name} -e "show index from ${line};" > /tmp/${line}_index.tsv
done < ./list.txt