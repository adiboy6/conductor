echo "Installing pip"

sudo yum install -y epel-release
sudo yum install -y python-pip
pip --version

if [ $? -ne 0 ]
then
	echo "pip not installed"
else
	echo "pip installed"
fi

sudo yum install -y jq

echo "installing the required packages"

for i in `cat requirements.txt`
do
	pip install $i
done

python flask_chota.py
