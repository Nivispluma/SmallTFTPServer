# SmallTFTPServer

This Server will NOT work in a Windows environment due to the way multiprocessing is implemented

## Installation Linux

### Clone Repository from GitHub to your local machine

````
git clone https://github.com/Nivispluma/SmallTFTPServer.git
````

### Install Python Virtual Environment and Dependencies

It might be necessary to install python3-venv first on Ubuntu Linux:

````
sudo apt install python3-venv
````

create the virtual environment for Python
```
python3 -m venv venv
```

activate the virtual environment
```
source venv/bin/activate
```

install the requirements
```
pip3 install -r requirements.txt
```

then you have to edit the necessary parameters in "mainTFTP.py" like IP-Address

start the TFTP Server
```
python mainTFTP.py
```