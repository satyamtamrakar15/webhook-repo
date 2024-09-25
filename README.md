# Dev Assessment - Webhook Receiver

## Setup

* Create a new virtual environment

```bash
pip install virtualenv
```

* Create the virtual env

```bash
virtualenv venv
```

* Activate the virtual env

```bash
source venv/bin/activate
```

* Install requirements

```bash
pip install -r requirements.txt
```
set  MONGO_URI to mongodb uri by setting  environment variable or use .env file
```bash
python run.py
```

* The endpoint is at:

```bash
POST http://127.0.0.1:5000/webhook/receiver
```

* The frontend endpoint is at:

http://localhost:5000/


* In Webhook,configure - Content Type as application/json



<!-- Using docker-compose.yml  -->

* To start the application it will spin mongodb container and run the main flask app
* I'm using WSL in windows so for me it docker-compose command tool is docker-compose else use `docker compose up` for Docker Desktop
docker-compose up

* Also make sure to remote port forwarding using ngrok using command 
`ngrok http localhost:5000`
* And add the public url provide by ngrok to webhook with specified webhook path and select webhook reponse type to application/json
`${PUBLIC_URL}/webhook/receiver`
