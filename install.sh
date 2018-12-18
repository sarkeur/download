# create a system user for running pyload
sudo adduser --system pyload

# install some dependencies for pyLoad
sudo apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 9165938D90FDDD2E
sudo sh -c "echo deb http://mirrordirector.raspbian.org/raspbian/ jessie main contrib non-free rpi \ >> /etc/apt/sources.list"
sudo sh -c "echo deb-src http://archive.raspbian.org/raspbian/ jessie main contrib non-free rpi \ >> /etc/apt/sources.list"
sudo apt-get install -y python-qt4 python-pil python-imaging python python-crypto python-pycurl python-openssl tesseract-ocr rhino
sudo apt-get update

# install pyload
wget https://github.com/pyload/pyload/releases/download/v0.4.9/pyload_0.4.9_all.deb
