#! /bin/bash

for jf in ~/test-jsons/*
do
	curl -v -H "Content-Type: application/json" -XPOST "http://192.168.1.12:9200/test-seq/_doc" -d @${jf}
	#echo ${jf}
done
