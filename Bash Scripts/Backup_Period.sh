#Test:
find /var/log/db_backup/Test/Mongodb -type d -name 'All_Mongodb*' -mtime +6 -exec rm -rf {} \;
find /var/log/db_backup/Test/Mysql -type d -name 'All*' -mtime +6 -exec rm -rf {} \;
#find /var/log/db_backup/Test/Mysql -type f -name 'something*' -mtime +6 -exec rm -rf {} \;
#find /var/log/db_backup/Test/Mysql -type f -name 'lending*' -mtime +6 -exec rm -rf {} \;
#find /var/log/db_backup/Test/Mysql -type f -name 'payment*' -mtime +6 -exec rm -rf {} \;
#find /var/log/db_backup/Test/Mysql -type f -name 'quartz*' -mtime +6 -exec rm -rf {} \;
#find /var/log/db_backup/Test/Mysql -type f -name 'sales*' -mtime +6 -exec rm -rf {} \;
#find /var/log/db_backup/Test/Mysql -type f -name 'test*' -mtime +6 -exec rm -rf {} \;

#Live:
find /var/log/db_backup/Live/Mongodb -type d -name 'All_Mongodb*' -mtime +13 -exec rm -rf {} \;
find /var/log/db_backup/Live/Mysql -type d -name 'All*' -mtime +13 -exec rm -rf {} \;
#find /var/log/db_backup/Live/Mysql -type f -name 'something*' -mtime +13 -exec rm -rf {} \;
#find /var/log/db_backup/Live/Mysql -type f -name 'lending*' -mtime +13 -exec rm -rf {} \;
#find /var/log/db_backup/Live/Mysql -type f -name 'payment*' -mtime +13 -exec rm -rf {} \;
