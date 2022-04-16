
from dynaconf import Dynaconf

config = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
)

try:
    config.telegram_token
except AttributeError:
    print("telegram token not_found")
