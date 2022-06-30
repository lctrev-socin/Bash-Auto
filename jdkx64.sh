mkdir -p ~/Software/JDK
mkdir -p ~/Software/Ant
wget -O /tmp/JDKx64.tar.gz https://cdn.azul.com/zulu/bin/zulu8.62.0.19-ca-jdk8.0.332-linux_x64.tar.gz
tar -xvf  /tmp/JDKx64.tar.gz -C ~/Software/JDK
wget -O /tmp/Ant.tar.gz https://dlcdn.apache.org//ant/binaries/apache-ant-1.9.16-bin.tar.gz
tar -xvf  /tmp/Ant.tar.gz -C ~/Software/Ant
