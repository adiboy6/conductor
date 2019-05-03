echo "Installing pip"

sudo yum install -y epel-release
sudo yum install -y python-pip

pip --version

echo "pip installed"

echo "installing the required packages"
for i in `cat requirements.txt`
do
	sudo pip install $i
done

python flask_chota.py
