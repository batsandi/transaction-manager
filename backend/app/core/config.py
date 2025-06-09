from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    """
    This class loads environment variables for the application.
    pydantic-settings automatically finds and loads the .env file.
    """
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    DATABASE_URL: str
    SECRET_KEY: str
    
# Other parts of the application will import this 'settings' object.
settings = Settings()