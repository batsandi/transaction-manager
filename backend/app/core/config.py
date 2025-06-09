from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    This class loads environment variables for the application.
    pydantic-settings automatically finds and loads the .env file.
    """
    # The below causes a crash for some reason
    # use the envars loaded by default by docker instead.
    # model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str
    SECRET_KEY: str

    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
# Other parts of the application will import this 'settings' object.
settings = Settings()
