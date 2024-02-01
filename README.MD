<h1 align="center">Backend of the Reservations application 👨‍💻</h1>
<h2>The backend is developed with Django and Django Rest Framework for the construction of REST APIS with PostgreSQL database</h2>
<h3>The entire updated project is located in the Master branch</h3>

<p>The backend is developed to manage different APIS, with methods such as POST, GET, and PUT, and at the same time the database is managed with the Django ORM, the architecture that is managed is through the HTTP protocol, for sending requests and data to the endpoints created in development.

For the creation of APIS, the architecture that was used was:

- DB Model
- Serializer
- View
- URL</p>

<p>The ER model of the database is as follows</p>
<img src="https://i.postimg.cc/k53hPTdg/Reservas-De-Eventos-drawio.png" alt="DB"/>

### Requirements:
    Python: 3.9.0
    PostgreSQL
    Pyenv (https://github.com/pyenv/pyenv)
    It is recommended to use Pyenv to be able to change Python versions

Create database backendReservas in PostgreSQL

All endpoints are configured with the route http://localhost:8000/

### All endpoints created were:
    http://localhost:8000/create-event/
    http://localhost:8000/all-events/
    http://localhost:8000/all-reserv/
    http://localhost:8000/all-user/
    http://localhost:8000/create-reserv/
    http://localhost:8000/create-user/
    http://localhost:8000/auth/

<h2>Below are screenshots of the tests of all the APIS</h2>

<img src="https://i.postimg.cc/Mf8fjKcp/Captura-de-pantalla-2024-02-01-010701.png" alt="api1"/>
<img src="https://i.postimg.cc/Yj1WBgVG/Captura-de-pantalla-2024-02-01-010802.png" alt="api2"/>
<img src="https://i.postimg.cc/K3rk7SLr/Captura-de-pantalla-2024-02-01-010826.png" alt="api3"/>
<img src="https://i.postimg.cc/gxMhBW7g/Captura-de-pantalla-2024-02-01-011126.png" alt="api4"/>
<img src="https://i.postimg.cc/2qMZrxrv/Captura-de-pantalla-2024-02-01-011307.png" alt="api5"/>
<img src="https://i.postimg.cc/ZCS6Wj3x/Captura-de-pantalla-2024-02-01-011419.png" alt="api6"/>

<h2>PYENV IN MAC  <img src="https://user-images.githubusercontent.com/43445037/217332541-e1b3151a-15b6-495d-92cc-daa31feeb408.png" alt="logo" height="60" width="60"/></h2> 


### Activate pyenv virtualenv
    pyenv install 3.9.0
    pyenv local 3.9.0
    pyenv activate venv-3.6.15

### Install dependences
    pip install -r requirements.txt

### Create superuser
    python manage.py createsuperuser
    
### Run server
    python manage.py runserver

### Create .env file
    DATABASE_ENGINE='django.db.backends.postgresql'
    DATABASE_NAME=backendReservas
    DATABASE_USER=usuario_postgres
    DATABASE_PASSWORD=contraseña
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    
    ALLOWED_HOSTS='*'

### Create superuser
    python manage.py createsuperuser
    
### Run server
    python manage.py runserver

<h2>PYENV IN WINDOWS  <img src="https://user-images.githubusercontent.com/43445037/217332759-ea2942d8-ef6b-412f-b86b-b21e174887cc.png" alt="logo" height="60" width="60"/></h2>

### Install pyenv with git (must have git installed)
    git clone https://github.com/pyenv-win/pyenv-win.git "%USERPROFILE%\.pyenv"
    
### To install via chocolatey and add it directly to the PATH
    choco install pyenv-win
    
### Add PYENV, PYENV_HOME and PYENV_ROOT to your environment variables
    [System.Environment]::SetEnvironmentVariable('PYENV',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")

    [System.Environment]::SetEnvironmentVariable('PYENV_ROOT',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")

    [System.Environment]::SetEnvironmentVariable('PYENV_HOME',$env:USERPROFILE + "\.pyenv\pyenv-win\","User")
    
### Now add the following paths to your USER PATH variable to access the pyenv command
    [System.Environment]::SetEnvironmentVariable('path', $env:USERPROFILE + "\.pyenv\pyenv-win\bin;" + $env:USERPROFILE + "\.pyenv\pyenv-win\shims;" + [System.Environment]::GetEnvironmentVariable('path', "User"),"User")
    
### For the operation of changing versions of Python it is recommended to disable these options
    Start Menu (Windows key) -> Manage application execution aliases -> disable python related aliases
    
  <div align="center">
  <a><img src="https://user-images.githubusercontent.com/43445037/217335215-b200b41a-7d08-4246-8533-bde3bb27d376.png" alt="logo"/></a>
  </div>  
    
### Close terminal, open a new one and check the installed version of pyenv
    pyenv --version
    
### Command to install a version of python
    pyenv install 3.9.0
    
### To set a Python version of the project that is active as soon as you enter the project directory, enter the following when inside the project root directory:
    pyenv local 3.9.0

### To install what is needed to start virtualenv
    python -m venv .venv

### Command to run the virtual environment
    .\.venv\Scripts\activate

### Install dependencies
    pip install -r requirements.txt

### Create .env file
    DATABASE_ENGINE='django.db.backends.postgresql'
    DATABASE_NAME=backendReservas
    DATABASE_USER=usuario_postgres
    DATABASE_PASSWORD=contraseña
    DATABASE_HOST=localhost
    DATABASE_PORT=5432
    
    ALLOWED_HOSTS='*'

### Create superuser
    python manage.py createsuperuser
    
### Run server
    python manage.py runserver
