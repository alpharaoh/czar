#!/bin/sh
wget https://github.com/projectdiscovery/subfinder/releases/download/v2.4.1/subfinder_2.4.1_linux_amd64.tar.gz
tar -xzvf subfinder_2.4.1_linux_amd64.tar.gz
rm LICENSE.md
rm README.md
mv subfinder /usr/local/bin
rm subfinder_2.4.1_linux_amd64.tar.gz

sudo apt-get install unzip
wget https://github.com/OWASP/Amass/releases/download/v3.9.1/amass_linux_amd64.zip
unzip amass_linux_amd64.zip
rm amass_linux_amd64.zip
mv ./amass_linux_amd64/amass /usr/local/bin/
rm -r amass_linux_amd64/

wget https://github.com/projectdiscovery/nuclei/releases/download/v2.1.0/nuclei_2.1.0_linux_amd64.tar.gz
tar -xzvf nuclei_2.1.0_linux_amd64.tar.gz
rm LICENSE.md
rm README.md
rm nuclei_2.1.0_linux_amd64.tar.gz
mv nuclei /usr/local/bin/

wget https://github.com/projectdiscovery/httpx/releases/download/v1.0.1/httpx_1.0.1_linux_amd64.tar.gz
tar -xzvf httpx_1.0.1_linux_amd64.tar.gz
rm httpx_1.0.1_linux_amd64.tar.gz
rm LICENSE.md
rm README.md
mv httpx /usr/local/bin/

cd ./Tools/
rm -r livetargetsfinder
rm -r smuggler
rm -r nuclei-templates
git clone https://github.com/allyomalley/LiveTargetsFinder.git
rm livetargetsfinder
mv LiveTargetsFinder livetargetsfinder
apt install python3-pip
cd ./livetargetsfinder
pip3 install -r requirements.txt
chmod +x install_deps.sh
./install_deps.sh

git clone https://github.com/projectdiscovery/nuclei-templates.git
git clone https://github.com/defparam/smuggler.git

wget https://github.com/ffuf/ffuf/releases/download/v1.1.0/ffuf_1.1.0_linux_amd64.tar.gz
tar -xzvf ffuf_1.1.0_linux_amd64.tar.gz 
rm LICENSE 
rm CHANGELOG.md 
rm README.md
rm ffuf_1.1.0_linux_amd64.tar.gz
mv ffuf /usr/local/bin/

wget https://github.com/lc/gau/releases/download/v1.0.3/gau_1.0.3_linux_amd64.tar.gz
tar xvf gau_1.0.3_linux_amd64.tar.gz
rm LICENSE 
rm README.md 
mv gau /usr/local/bin
rm gau_1.0.3_linux_amd64.tar.gz
