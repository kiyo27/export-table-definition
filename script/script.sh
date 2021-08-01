#!/bin/bash

# DATABASE=blog
# USER=root
# PASSWORD=root
# PORT=3306

mysql -h host.docker.internal -P ${PORT} -u ${USER} -p${PASSWORD} ${DATABASE} -e 'show tables;' > /script/list.txt

sed -i '1d' /script/list.txt

while read line
do
    mysql -h host.docker.internal -P ${PORT} -u ${USER} -p${PASSWORD} ${DATABASE} -e "desc ${line};" > /tmp/${line}_desc.tsv
    mysql -h host.docker.internal -P ${PORT} -u ${USER} -p${PASSWORD} ${DATABASE} -e "show index from ${line};" > /tmp/${line}_index.tsv
done < /script/list.txt