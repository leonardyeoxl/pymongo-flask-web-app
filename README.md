# README

## MongoDB Docker

```sh
docker pull mongo
docker run -it -v `pwd`/mongodata/:/mongodata -p 27017:27017 --name mongodb -d mongo
```

## Virtual Environment

```sh
apt-get install python3-pip
pip3 install virtualenv
virtualenv venv
```

```sh
source venv/bin/activate
pip install flask
pip install pymongo
```

```sh
deactivate
```