import os
import tomllib
import subprocess
from pathlib import Path


with open('settings.toml', 'rb') as sf:
    config = tomllib.load(sf)

BASE_DIR = Path(__file__).resolve().parent
DB_CONFIG = config['database']


def create_alembic_migration(base_dir, db_config):
    try:
        print("\033[1;33m Start setting up")
        subprocess.run(["alembic", "init", "student/migrations"])
        
        file_path_alembic = os.path.join(base_dir, "alembic.ini")

        alembic_content =(f'sqlalchemy.url = {db_config["ENGINE"]}+'
                        f'{db_config["DRIVER"]}://{db_config["USER"]}:'
                        f'{db_config["PASSWORD"]}@{db_config["HOST"]}:'
                        f'{db_config["PORT"]}/{db_config["NAME"]}')

        env_content = ("from kernel.database.core import SQLalchemy\n"
                        "from student import models\n"
                        "db = SQLalchemy()\n"
                        "target_metadata = db.Base.metadata")

        with open(file_path_alembic, 'r+') as file:
            lines = file.readlines()
            del lines[63 - 1]
            lines.insert(63 - 1, alembic_content + '\n')

            file.seek(0)
            file.writelines(lines)

        file_path_env = os.path.join(base_dir, "student/migrations/env.py")
        with open(file_path_env, "r+") as file:
            lines = file.readlines()
            del lines[21 - 1]
            lines.insert(21 - 1, env_content + '\n')
            file.seek(0)
            file.writelines(lines)

        subprocess.run(
            [
                "alembic",
                "revision",
                "--autogenerate",
                "-m",
                "'Added account table'"
            ]
        )

        subprocess.run(["alembic", "upgrade", "head"])

    except Exception:
        print("\033[1;31m ERROR: Please do the settings manually!")
    else:
        print("\033[1;32m Settings are done successfully.")


if __name__ == "__main__":
    create_alembic_migration(BASE_DIR, DB_CONFIG)
