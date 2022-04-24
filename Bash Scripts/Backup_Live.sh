#!/bin/bash

#Mongo Backup
mongodump -u admin -p "password" --out=/var/log/db_backup/Mongodb/"All_Mongodb_$(date +%Y-%m-%d_%H-%M-%S)"
#rsync -r /var/log/db_backup/Mongodb/ root@"IP[:Port]":/var/log/db_backup/Live/Mongodb
scp -r -P "Port" /var/log/db_backup/Mongodb/* root@"IP":/var/log/db_backup/Live/Mongodb

#Mysql Backup
X=$(date +%Y-%m-%d_%H-%M-%S)
mkdir /var/log/db_backup/Mysql/"All_Mysql-$X"
mysqldump -u root -p"password" core > /var/log/db_backup/Mysql/"All_Mysql-$X"/core-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" iam > /var/log/db_backup/Mysql/"All_Mysql-$X"/iam-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" payment > /var/log/db_backup/Mysql/"All_Mysql-$X"/payment-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" report > /var/log/db_backup/Mysql/"All_Mysql-$X"/report-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" scheduler > /var/log/db_backup/Mysql/"All_Mysql-$X"/scheduler-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" lending > /var/log/db_backup/Mysql/"All_Mysql-$X"/lending-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" payment_facilitator > /var/log/db_backup/Mysql/"All_Mysql-$X"/payment_facilitator-$(date +%Y-%m-%d_%H-%M-%S).sql
#mysqldump -u root -p"password" quartz > /var/log/db_backup/Mysql/quartz-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" sales > /var/log/db_backup/Mysql/"All_Mysql-$X"/sales-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" etebarino_site > /var/log/db_backup/Mysql/"All_Mysql-$X"/etebarino_site-$(date +%Y-%m-%d_%H-%M-%S).sql
#mysqldump -u root -p"password" test > /var/log/db_backup/Mysql/test-$(date +%Y-%m-%d_%H-%M-%S).sql
#mysqldump -u root -p"password" test > /var/log/db_backup/Mysql/test-$(date +%Y-%m-%d_%H-%M-%S)/test-$(date +%Y-%m-%d_%H-%M-%S).sql
#rsync -r /var/log/db_backup/Mysql/ root@"IP[:Port]":/var/log/db_backup/Live/Mysql
scp -r -P "Port" /var/log/db_backup/Mysql/* root@"IP":/var/log/db_backup/Live/Mysql
find /var/log/db_backup/Mongodb -type d -name 'All_Mongodb*' -exec rm -rf {} \;
find /var/log/db_backup/Mysql -type d -name 'All*' -exec rm -rf {} \;

