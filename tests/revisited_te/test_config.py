from pydantic import BaseModel
from revisited.core.conf import setting_to_model, settings


class DynaSetting(BaseModel):
    first_superuser_password: str | None = None


def test_setting_to_model():
    result = setting_to_model(settings, DynaSetting)
    print(result.model_dump())
    assert result.first_superuser_password == "password"
