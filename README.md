# PDV


This project consists in registering all payments made by customers to an establishment.
The main idea of the architecture was based on the Clean Architecture, so I chose to follow the Hexagonal Architecture.  

 - It was only tested on Linux.
 
The "Nosso Segundo Desafio" is in this link: https://github.com/renanbs/pdv/blob/master/code-review.py
 

## Requirements

 - Make
 - Python 3.8+
 - pyenv


## Development Environment
 
 
### Automation tool

This project uses `Makefile` as automation tool. Replace `pdv` label to your project name.

### Set-up Virtual Environment

The following commands will install and set-up `pyenv` tool (https://github.com/pyenv/pyenv) used to create/manage virtual environments:

> Just replace `zshrc` with the configuration file of your interpreter, like `bashrc`

```bash
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.zshrc
$ exec "$SHELL"
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
$ exec "$SHELL"
```

After that, access the project directory and execute `make create-venv` to create and recreate the virtual environment.

> The environment will be create in your home directory:

> `$PROJECT_NAME` and `$PYTHON_VERSION` are variables defined in the Makefile

```bash
$HOME/.pyenv/versions/$PROJECT_NAME-$PYTHON_VERSION/bin/python

/home/renan/.pyenv/versions/pdv-3.8.5/bin/python
```


### Run unit tests, style and convention

- Tests will run with coverage minimum at 80%.

Running code style
```bash
➜ make code-convention
```
Running unit tests
```bash
➜ make test
```
Running code style and all tests
```bash
➜ make
```

## How to run this project

There are some ways to run this project.

> When you create virtual environment, you have those 3 options above:

```bash
➜ flask run
```
or

```bash
➜ python wsgi.py
```
or 

```bash
➜ make run
```

> Or if you want, you can build a docker and run it:

```bash
➜ make build-docker
➜ make run-docker
```

Both options will start the server in your localhost using port 5000.

The server is accessible at the link below, despite there is no root endpoint:
> http://127.0.0.1:5000/

The endpoints available are:

- **POST** http://127.0.0.1:5000/api/v1/transacao
- **GET** http://127.0.0.1:5000/api/v1/transacoes/estabelecimento

> Extra endpoints
- **POST** http://127.0.0.1:5000/api/v1/estabelecimento
- **GET** http://127.0.0.1:5000/api/v1/estabelecimentos

---
## Usage examples

### cURL

**Create a establishment**
```bash
➜ curl -X POST http://127.0.0.1:5000/api/v1/estabelecimento -d '{"nome": "Meu EC", "cnpj": "970.640.320001-92", "dono": "juca owner", "telefone": "51999999999"}' -H 'Content-Type: application/json'
```

**Create a transaction with the establishment from the command above**
```bash
➜ curl -X POST http://127.0.0.1:5000/api/v1/transacao -d '{"cliente": "48779229034", "estabelecimento": "970.640.320001-92", "valor": 10, "descricao": "my lunch"}' -H 'Content-Type: application/json'
```

**List the transactions from a establishment**
```bash
➜ curl http://127.0.0.1:5000/api/v1/transacoes/estabelecimento?cnpj=97064032000192 -H 'Content-Type: application/json'
```

**List all establishments**
```bash
➜ curl http://127.0.0.1:5000/api/v1/estabelecimentos -H 'Content-Type: application/json'
```
