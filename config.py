
from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
)

try:
    settings.telegram_token
except AttributeError:
    print("telegram token not_found")
