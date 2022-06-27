mkdir -p ~/Software/JDK
mkdir -p ~/Software/Ant
wget -O /tmp/JDKx64.tar.gz https://github.com/adoptium/temurin8-binaries/releases/download/jdk8u332-b09/OpenJDK8U-jdk_x64_linux_hotspot_8u332b09.tar.gz
tar -xvf  /tmp/JDKx64.tar.gz -C ~/Software/JDK
wget -O /tmp/Ant.tar.gz https://dlcdn.apache.org//ant/binaries/apache-ant-1.9.16-bin.tar.gz
tar -xvf  /tmp/Ant.tar.gz -C ~/Software/Ant