for file in ~/test-jsons/*
do
	cat $file | tr -d " \t\n\r" > $file.json
	rm -f $file
done
