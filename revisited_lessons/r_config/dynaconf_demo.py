import os
from typing import Any

from dynaconf import Dynaconf
from pydantic import BaseModel, Field


# XXX: no promises that these are complete or correct...
class DynaconfConfig(BaseModel):
    ENVVAR_PREFIX_FOR_DYNACONF: str | None
    SETTINGS_FILE_FOR_DYNACONF: bool | list[str]
    RENAMED_VARS: dict[str, Any]  # TODO
    ROOT_PATH_FOR_DYNACONF: str | None
    ENVIRONMENTS_FOR_DYNACONF: bool
    MAIN_ENV_FOR_DYNACONF: str
    LOWERCASE_READ_FOR_DYNACONF: bool
    ENV_SWITCHER_FOR_DYNACONF: str
    FORCE_ENV_FOR_DYNACONF: str | None
    DEFAULT_ENV_FOR_DYNACONF: str
    IGNORE_UNKNOWN_ENVVARS_FOR_DYNACONF: bool
    AUTO_CAST_FOR_DYNACONF: bool
    ENCODING_FOR_DYNACONF: str
    MERGE_ENABLED_FOR_DYNACONF: bool
    DOTTED_LOOKUP_FOR_DYNACONF: bool
    NESTED_SEPARATOR_FOR_DYNACONF: str | None
    ENVVAR_FOR_DYNACONF: str | None
    REDIS_FOR_DYNACONF: dict[str, Any]  # TODO
    REDIS_ENABLED_FOR_DYNACONF: bool
    VAULT_FOR_DYNACONF: dict[str, Any]  # TODO
    VAULT_ENABLED_FOR_DYNACONF: bool
    VAULT_PATH_FOR_DYNACONF: str | None
    VAULT_MOUNT_POINT_FOR_DYNACONF: str | None
    VAULT_ROOT_TOKEN_FOR_DYNACONF: str | None
    VAULT_KV_VERSION_FOR_DYNACONF: int
    VAULT_AUTH_WITH_IAM_FOR_DYNACONF: bool
    VAULT_AUTH_ROLE_FOR_DYNACONF: str | None
    VAULT_ROLE_ID_FOR_DYNACONF: str | None
    VAULT_SECRET_ID_FOR_DYNACONF: str | None
    VAULT_USERNAME_FOR_DYNACONF: str | None
    VAULT_PASSWORD_FOR_DYNACONF: str | None
    CORE_LOADERS_FOR_DYNACONF: list[str]
    LOADERS_FOR_DYNACONF: list[str]
    SILENT_ERRORS_FOR_DYNACONF: bool
    FRESH_VARS_FOR_DYNACONF: list[str]
    DOTENV_PATH_FOR_DYNACONF: str | None
    DOTENV_VERBOSE_FOR_DYNACONF: bool
    DOTENV_OVERRIDE_FOR_DYNACONF: bool
    INSTANCE_FOR_DYNACONF: str | None
    YAML_LOADER_FOR_DYNACONF: str
    COMMENTJSON_ENABLED_FOR_DYNACONF: bool
    SECRETS_FOR_DYNACONF: str | None
    INCLUDES_FOR_DYNACONF: list[str]
    PRELOAD_FOR_DYNACONF: list[str]
    SKIP_FILES_FOR_DYNACONF: list[str]
    APPLY_DEFAULT_ON_NONE_FOR_DYNACONF: None
    VALIDATE_ON_UPDATE_FOR_DYNACONF: bool
    SYSENV_FALLBACK_FOR_DYNACONF: bool
    DYNACONF_NAMESPACE: str
    NAMESPACE_FOR_DYNACONF: str
    DYNACONF_SETTINGS_MODULE: list[str]
    DYNACONF_SETTINGS: list[str]
    SETTINGS_MODULE: bool | list[str]
    SETTINGS_MODULE_FOR_DYNACONF: list[str]
    PROJECT_ROOT: str | None
    PROJECT_ROOT_FOR_DYNACONF: str | None
    DYNACONF_SILENT_ERRORS: bool
    DYNACONF_ALWAYS_FRESH_VARS: list[str]
    BASE_NAMESPACE_FOR_DYNACONF: str
    GLOBAL_ENV_FOR_DYNACONF: str
    ENV_FOR_DYNACONF: str | None


# XXX: all attributes must be uppercase because Dynaconf converts everything to uppercase
# might be optional in Dynaconf 4.0:
# https://github.com/dynaconf/dynaconf/issues/761
class Config(DynaconfConfig, extra="forbid", validate_default=True):
    DB_HOST: str = Field(default="127.0.0.1")
    DB_PORT: int = Field(default=7687)
    # ... etc ...


# settings = Config(**dynaconf_settings)

dynaconf_settings = Dynaconf(
    settings_file=[
        "configs/settings.toml",
        "configs/.secrets.toml",
        "settings.toml",
        ".secrets.toml",
    ],
    environment=True,
    load_dotenv=True,
    envvar_prefix=False,
    includes=["../config/custom_settings.toml"],
)

dynaconf_settings.validators.validate()


def ensure_env_settings(env_name: str):
    env_switcher_key = dynaconf_settings.ENV_SWITCHER_FOR_DYNACONF
    os.environ[env_switcher_key] = env_name
    dynaconf_settings.reload()


class DynaSetting(BaseModel):
    first_superuser_password: str | None = None


def setting_to_model(setting: Dynaconf, model_type: type[BaseModel]):
    result = model_type()
    for model in model_type.model_fields:
        setattr(result, model, getattr(setting, model))
    return result


if __name__ == "__main__":
    print(dynaconf_settings.db_url)
    print(dynaconf_settings.PROJECT_NAME)
    print(dynaconf_settings.ENVVAR_PREFIX_FOR_DYNACONF)
    print(dynaconf_settings.ENV_SWITCHER_FOR_DYNACONF)
    print(dynaconf_settings.db_url)
    print(dynaconf_settings.project_name)
    print(dynaconf_settings.PROJECT_NAME)
    result = setting_to_model(dynaconf_settings, DynaSetting)
    print(result.model_dump())
