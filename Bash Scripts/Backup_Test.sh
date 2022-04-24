#!/bin/bash

#Mongo Backup
mongodump -u "username" -p "password" --out=/var/log/db_backup/Mongodb/"All_Mongodb_$(date +%Y-%m-%d_%H-%M-%S)"
rsync -r /var/log/db_backup/Mongodb/ root@"ip":/var/log/db_backup/Test/Mongodb

#Mysql Backup
X=$(date +%Y-%m-%d_%H-%M-%S)
mkdir /var/log/db_backup/Mysql/"All_Mysql-$X"
mysqldump -u root -p"password" core > /var/log/db_backup/Mysql/"All_Mysql-$X"/core-$(date +%Y-%m-%d_%H-%M-%S).sql
#mysqldump -u root -p"password" core > /var/log/db_backup/Mysql/core-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" iam > /var/log/db_backup/Mysql/"All_Mysql-$X"/iam-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" payment > /var/log/db_backup/Mysql/"All_Mysql-$X"/payment-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" report > /var/log/db_backup/Mysql/"All_Mysql-$X"/report-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" scheduler > /var/log/db_backup/Mysql/"All_Mysql-$X"/scheduler-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" lending > /var/log/db_backup/Mysql/"All_Mysql-$X"/lending-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" payment_facilitator > /var/log/db_backup/Mysql/"All_Mysql-$X"/payment_facilitator-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" quartz > /var/log/db_backup/Mysql/"All_Mysql-$X"/quartz-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" sales > /var/log/db_backup/Mysql/"All_Mysql-$X"/sales-$(date +%Y-%m-%d_%H-%M-%S).sql
mysqldump -u root -p"password" test > /var/log/db_backup/Mysql/"All_Mysql-$X"/test-$(date +%Y-%m-%d_%H-%M-%S).sql
#mysqldump -u root -p"password" test > /var/log/db_backup/Mysql/test-$(date +%Y-%m-%d_%H-%M-%S)/test-$(date +%Y-%m-%d_%H-%M-%S).sql
rsync -r /var/log/db_backup/Mysql/ root@"ip":/var/log/db_backup/Test/Mysql
find /var/log/db_backup/Mongodb -type d -name 'All_Mongodb*' -exec rm -rf {} \;
find /var/log/db_backup/Mysql -type d -name 'All*' -exec rm -rf {} \;

