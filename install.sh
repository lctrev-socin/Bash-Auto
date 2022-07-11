sudo adduser socinftp --home /usr/socin/econect/ftp --shell /bin/bash
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install ssh vsftpd openjdk-8-jdk mysql-client=5.7* mysql-community-server=5.7* mysql-server=5.7* -y
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
echo "write_enable=YES" >> /etc/vsftpd.conf
echo "local_umask=777" >> /etc/vsftpd.conf
