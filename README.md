## Project Stack

| Name           | Version  |
|:--------------:|:--------:|
| Python         | 3.11     |
| Postgres       | 15       |
| Git            | 2.33     |
| pyhton-tk      |          |


## Development Environment Configuration

### Clone Project

The first thing to do is to clone the repository

#### Install Python-tk Package
__Macos__
```sh
brew install python-tk
```
__Linux__
```bash
sudo apt-get install python3-tk
# or
sudo apt-get install python-tk
```

#### Install Postgresql
__Macos__
```sh
brew install postgresql@15
```

### Python Env Setup

Create a virtual environment to install dependencies inside it and activate it.



#### [Poetry](https://python-poetry.org/docs/cli/#new)

__Install Poetry on Linux__

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

__Install Poetry on Windows__

**TIP**: do bellow command on Powershell Administrator

```ps
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

__Install Poetry on Macos__

```sh
brew install poetry
```
__CONFIG__

1) To installing the config build env in the program directory

```sh
# Creates the address of the .env folder in the program directory, It is null by default
poetry config virtualenvs.in-project true
# The address of the .env folder
poetry config virtualenvs.path .
```


2) To install all packages with poetry that is documented in `poetry.lock` do bellow command:

```sh
poetry install
```

3) To activate poetry environment:

```sh
poetry shell
```

## Prepare Settings

### Database Configuration
Transfer the __settings-template.toml__ file from the __config__ folder to the base directory

Then change its name in the settings.toml

1) Config Database in Python by `settings.toml` For example:

```toml
[database]
ENGINE = "postgresql"
DRIVER = "psycopg2"
NAME = "university_db"
USER = "university_user"
PASSWORD = "e2JOV6Y4FAzPCRyA2MRLnqfyPmcM1IxoK9LX2IHLstw"
HOST = "localhost"
PORT = "5432"
```

2) Create a Database in PSQL
 
Enter the terminal page, Connect to `psql`

```sh
CREATE DATABASE university_db;

CREATE USER university_user WITH PASSWORD'e2JOV6Y4FAzPCRyA2MRLnqfyPmcM1IxoK9LX2IHLstw';

ALTER ROLE university_user SET client_encoding TO 'utf8';

ALTER ROLE university_user SET default_transaction_isolation TO 'read committed';

ALTER ROLE university_user SET timezone TO 'UTC';

ALTER USER university_user CREATEDB;

ALTER USER university_user LOGIN;

ALTER DATABASE university_db OWNER TO university_user;

ALTER ROLE university_user WITH CREATEDB;

GRANT ALL PRIVILEGES ON DATABASE university_db TO university_user;

grant usage on schema public to university_user;

grant create on schema public to university_user;

```

3) Create migration with alembic in virtual environment activate

```py
alembic init student/migrations
```
4) After making the initial alembic In the base directory, __alembic.ini__ file was created Apply the following changes inside it

	In fact, we have to enter the database configuration manually
```ini
# line 63:
sqlalchemy.url = postgresql+psycopg2://university_user:e2JOV6Y4FAzPCRyA2MRLnqfyPmcM1IxoK9LX2IHLstw@localhost:5432/university_db
```

5) Changes in the __student/migrations/env.py__ file in the migration folder that was created
```py
# line 21:
from kernel.database.core import SQLalchemy
from student import models
db = SQLalchemy()
target_metadata = db.Base.metadata
```

6) Run below commands
```sh
alembic revision --autogenerate -m "Added account table"
alembic upgrade head
```
#### Run Project

You can now run the app:

```sh
python manage.py
```
