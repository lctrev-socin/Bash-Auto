echo Senha root mysql
read MYSQL_ROOT_PASSWORD

echo "mysql-apt-config mysql-apt-config/unsupported-platform select abort" | /usr/bin/debconf-set-selections
echo "mysql-apt-config mysql-apt-config/repo-codename   select bionic" | /usr/bin/debconf-set-selections
echo "mysql-apt-config mysql-apt-config/select-tools select" | /usr/bin/debconf-set-selections
echo "mysql-apt-config mysql-apt-config/repo-distro select ubuntu" | /usr/bin/debconf-set-selections
echo "mysql-apt-config mysql-apt-config/select-server select mysql-5.7" | /usr/bin/debconf-set-selections
echo "mysql-apt-config mysql-apt-config/select-product select Apply" | /usr/bin/debconf-set-selections

echo "mysql-community-server mysql-community-server/root-pass password $MYSQL_ROOT_PASSWORD" | /usr/bin/debconf-set-selections
echo "mysql-community-server mysql-community-server/re-root-pass password $MYSQL_ROOT_PASSWORD" | /usr/bin/debconf-set-selections
echo "mysql-community-server mysql-community-server/remove-data-dir boolean false" | /usr/bin/debconf-set-selections
echo "mysql-community-server mysql-community-server/data-dir note" | /usr/bin/debconf-set-selections

export DEBIAN_FRONTEND=noninteractive
wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb
apt-get update
apt-get --yes install mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*


SECURE_MYSQL=$(expect -c "
set timeout 10
spawn mysql_secure_installation

expect "Enter password for user root:"
send "$MYSQL\r"

expect "Change the password for root ?\(Press y\|Y for Yes, any other key for No\) :"
send "y\r"

expect "New password:"
send "$MYSQL_ROOT_PASSWORD\r"

expect "Re-enter new password:"
send "$MYSQL_ROOT_PASSWORD\r"

expect "Do you wish to continue with the password provided?\(Press y\|Y for Yes, any other key for No\) :"
send "y\r"

expect "Remove anonymous users?\(Press y\|Y for Yes, any other key for No\) :"
send "y\r"

expect "Disallow root login remotely?\(Press y\|Y for Yes, any other key for No\) :"
send "y\r"

expect "Remove test database and access to it?\(Press y\|Y for Yes, any other key for No\) :"
send "y\r"

expect "Reload privilege tables now?\(Press y\|Y for Yes, any other key for No\) :"
send "y\r"

expect eof
")

echo "$SECURE_MYSQL"
echo 'sql-mode=""' | /etc/mysql/mysql.conf.d/mysqld.cnf
echo 'secure-file-priv=""s' | /etc/mysql/mysql.conf.d/mysqld.cnf