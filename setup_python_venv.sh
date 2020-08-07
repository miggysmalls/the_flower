# Create python virutal environment with version 3.7.4
sudo apt-get install python3-pip
pip3 install virtualenv
python3 -m virtualenv --python=/usr/local/bin/python3.7 venv
source venv/bin/activate
python --version

