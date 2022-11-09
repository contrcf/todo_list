from dynaconf import Dynaconf, Validator
from pathlib import Path

settings = Dynaconf(
    # validators=[Validator('NUMBER', 'NAME', must_exist=True)],
    envvar_prefix="DYNACONF",
    root_path=Path(__file__).parent,
    settings_files=["settings.toml", ".secrets.toml"],
    environment=True,
    load_dotenv=True,
)

ROOT_DIR = Path(__file__).parent
