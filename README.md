# PDV


This project consists in registering all payments made by customers to an establishment.  

 - It was only tested on Linux.

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

- Tests will run with coverage minimum at 90%.

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

There are 2 ways to run this project.

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

This will start the server in your localhost using port 5000.

The server is accessible at the link below, despite there is no root endpoint:
> http://127.0.0.1:5000/

The only available endpoints are:
- POST http://127.0.0.1:5000/

---
## Usage examples

### cURL


