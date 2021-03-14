<img width="1280" alt="Katana Cover" src="https://user-images.githubusercontent.com/24438869/111058809-03a5a100-84b7-11eb-958a-a846b1a277b1.png">

## Introduction 🌻
> **Katana** project is a template for ASAP 🚀 ML application deployment
>
> Checkout demo at- https://katana-demo.herokuapp.com/

### Features 🎉
1. FastAPI inbuilt
2. Swagger UI and uvicorn integration
3. Docker ready configuration
4. Integrated GitHub actions
5. Production ready code 🚀

## Set-up Instructions 🔧
We recommend using flask default serving for development and uvicorn server for production

We included following setup instructions;

1. Local development 
2. Docker supported deployment


### Local Development 👨🏻‍💻
1. Clone this repo with `git@github.com:shaz13/katana.git`
2. Set up environment using `python3 -m venv .env`
3. Activate envrionment using 
```
# Linux / Mac / Unix
$ source .env/bin/activate

# Windows
$ \.env\Scripts\activate
```
4. Install requirements using `pip install -r requirements.txt`
5. For debugging run from root - `python main.py`
6. Deploy using `Procfile` or `bash scripts/launch.sh`
7. Your API is being served at `localhost:9000`

### Docker Setup ⛴
1. Clone this repo with `git@github.com:shaz13/katana.git`
2. Install docker in your system
3. Run `docker-compose up`
4. Your local port is mapped and being served at `localhost:9000`

![Capture](https://user-images.githubusercontent.com/24438869/111058838-351e6c80-84b7-11eb-916e-bdc191b0a916.PNG)


## Contributors 😎
1. Mohammad Shahebaz - @shaz13
2. Aditya Soni - @AdityaSoni19031997

## License 👩🏻‍💼
MIT License
