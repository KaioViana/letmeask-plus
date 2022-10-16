from dynaconf import Dynaconf
import os

settings = Dynaconf(
    settings_files=['settings.toml', '.secrets.toml'],
    root_path=os.path.dirname(__file__),
)
