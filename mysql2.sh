echo Senha root mysql
read MYSQL_ROOT_PASSWORD

mysql -e "UPDATE mysql.user SET Password = PASSWORD($MYSQL_ROOT_PASSWORD) WHERE User = 'root'"
mysql -e "DROP USER ''@'localhost'"
mysql -e "DROP USER ''@'$(hostname)'"
mysql -e "DROP DATABASE test"
mysql -e "FLUSH PRIVILEGES"

echo 'sql-mode=""' | /etc/mysql/mysql.conf.d/mysqld.cnf
echo 'secure-file-priv=""s' | /etc/mysql/mysql.conf.d/mysqld.cnf