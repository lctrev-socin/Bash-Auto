import os

os.system("wget https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb")
os.system("sudo dpkg -i mysql-apt-config_0.8.12-1_all.deb")
os.system("sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29")
os.system("sudo apt update")
os.system("sudo apt-cache policy mysql-server")
os.system("sudo apt install ssh vsftpd openjdk-8-jdk mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7*")
os.system("sudo adduser socinftp --home /usr/socin/econect/ftp --shell /bin/bash")
