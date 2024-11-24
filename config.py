import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv('.env')


@dataclass
class BotConfig:
    token: str
    admins: list[int]
    api_id: str
    api_hash: str


@dataclass
class API:
    BASE_URL: str


@dataclass
class Instagram:
    username: str
    email: str
    password: str


@dataclass
class AppConfig:
    bot: BotConfig
    api: API
    instagram: Instagram


def load_config() -> AppConfig:
    return AppConfig(
        bot=BotConfig(
            token=os.getenv("BOT_TOKEN", ""),
            admins=list(map(int, os.getenv("ADMINS").split(","))),
            api_hash=os.getenv("TELEGRAM_API_ID", ''),
            api_id=os.getenv("TELEGRAM_API_HASH", ''),
        ),
        api=API(
            BASE_URL=os.getenv("BASE_URL", ""),
        ),
        instagram=Instagram(
            email=os.getenv("INSTAGRAM_EMAIL", ""),
            password=os.getenv("INSTAGRAM_PASSWORD", ""),
            username=os.getenv("INSTAGRAM_USERNAME", ""),
        )
    )
