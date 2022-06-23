import os

os.system("sudo export DEBIAN_FRONTEND=noninteractive")
os.system("sudo debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/repo-codename select bionic'")
os.system("sudo debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/repo-distro select ubuntu'")
os.system("sudo debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/repo-url string http://repo.mysql.com/apt/'")
os.system("sudo debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/select-preview select '")
os.system("sudo debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/select-product select Ok'")
os.system("sudo debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/select-server select mysql-5.7'")
os.system("sudo debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/select-tools select '")
os.system("sudo debconf-set-selections <<< 'mysql-apt-config mysql-apt-config/unsupported-platform select abort'")

os.system("wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb")
os.system("sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb")
os.system("sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29")
os.system("sudo apt update")
os.system("sudo apt-cache policy mysql-server")
os.system("sudo apt install ssh vsftpd openjdk-8-jdk mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y")
os.system("sudo adduser socinftp --home /usr/socin/econect/ftp --shell /bin/bash")
