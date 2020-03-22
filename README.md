# ⚔️ Project Katana 
> Katana project is a pre-built bioler plate code for production level model deployement. 

## Features 
1. Flask RestFul at your rescue!
2. Swagger UI and endpoints structured 
3. Pre-defined action integration
4. Docker and Kubernetes compatible
5. Production code deployment with `gunicorn`
6. Awesome logging configurations


## Set-up Instructions 

### Local Development
1. Clone this repo with `git@github.com:shaz13/katana.git`
2. Set up environment using `python3 -m venv .env`
3. Activate envrionment using 
```
# Linux / Mac / Unix
$ source activate .env/bin/activate

# Windows
.\env\Scripts\activate

```
4. Install requirements using `pip install -r requirements.txt`
5. For debugging run from root - `python main.py`
6. Deploy using `Procfile` or `bash scripts/start.sh`

### Docker Setup
1. Clone this repo with `git@github.com:shaz13/katana.git`
2. Install docker in your system
3. Run `docker-compose up`


