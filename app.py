import os

os.system('sudo echo "mysql-apt-config mysql-apt-config/unsupported-platform select abort" | /usr/bin/debconf-set-selections')
os.system('sudo echo "mysql-apt-config mysql-apt-config/repo-codename   select trusty" | /usr/bin/debconf-set-selections')
os.system('sudo echo "mysql-apt-config mysql-apt-config/select-tools select" | /usr/bin/debconf-set-selections')
os.system('sudo echo "mysql-apt-config mysql-apt-config/repo-distro select ubuntu" | /usr/bin/debconf-set-selections')
os.system('sudo echo "mysql-apt-config mysql-apt-config/select-server select mysql-5.7" | /usr/bin/debconf-set-selections')
os.system('sudo echo "mysql-apt-config mysql-apt-config/select-product select Apply" | /usr/bin/debconf-set-selections')

os.system('sudo echo "mysql-community-server mysql-community-server/root-pass password $ROOT_PASSWORD" | /usr/bin/debconf-set-selections')
os.system('sudo echo "mysql-community-server mysql-community-server/re-root-pass password $ROOT_PASSWORD" | /usr/bin/debconf-set-selections')
os.system('sudo echo "mysql-community-server mysql-community-server/remove-data-dir boolean false" | /usr/bin/debconf-set-selections')
os.system('sudo echo "mysql-community-server mysql-community-server/data-dir note" | /usr/bin/debconf-set-selections')
os.system('export DEBIAN_FRONTEND=noninteractive')

os.system("wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb")
os.system("sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb")
os.system("sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29")
os.system("sudo apt update")
os.system("sudo apt-cache policy mysql-server")
os.system("sudo apt install ssh vsftpd openjdk-8-jdk mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y")
os.system("sudo adduser socinftp --home /usr/socin/econect/ftp --shell /bin/bash")
