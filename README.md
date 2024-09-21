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