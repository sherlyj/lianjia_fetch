#!/bin/sh
BASE_DIR=/home/ubuntu/Documents/lianjia_fetch/lianjia_fetch
echo date 
PATH=/home/ubuntu/bin:/home/ubuntu/.local/bin:/opt/anaconda2/bin:/usr/lib/jvm/java-8-oracle//bin:/home/ubuntu/anaconda2/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/lib/jvm/java-8-oracle/bin:/usr/lib/jvm/java-8-oracle/db/bin:/usr/lib/jvm/java-8-oracle/jre/bin

echo "[INFO] 开始抓取数据..."
python $BASE_DIR/fetch_lianjia.py  2>&1 
