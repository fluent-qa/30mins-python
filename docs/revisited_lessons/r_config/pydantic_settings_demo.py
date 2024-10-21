from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DemoSettings(BaseSettings):
    model_config = SettingsConfigDict(
        pyproject_toml_depth=1,
        env_file=".env",
        env_file_encoding="utf-8",
        validate_default=False,
    )
    first_super_password: str = Field("password", validate_default=False)


if __name__ == "__main__":
    print(DemoSettings().first_super_password)
