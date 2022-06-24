import os
import time
print('Senha usuario socinftp')
input(passwd)
print('Selecionar MySql 5.7 e Ubuntu Bionic')
time.sleep(5)

chPasswd= 'echo ',passwd, '| passwd socinftp --stdin'
os.system("wget https://dev.mysql.com/get/mysql-apt-config_0.8.22-1_all.deb")
os.system("sudo dpkg -i mysql-apt-config_0.8.22-1_all.deb")
os.system("sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 467B942D3A79BD29")
os.system("sudo apt update")
os.system("sudo apt-cache policy mysql-server")
os.system("sudo apt install ssh vsftpd openjdk-8-jdk mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y")
os.system("sudo useradd socinftp --home /usr/socin/econect/ftp --shell /bin/bash")
os.system(chngPasswd)