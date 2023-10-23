# from config import config

import os

from dotenv import load_dotenv

load_dotenv()


class config:
    openai_api_key: str = os.getenv("openai_api_key")
    # api_path: str = os.getenv("api_path")

    db_proto: str = os.getenv("db_proto")
    db_user: str = os.getenv("db_user")
    db_pass: str = os.getenv("db_pass")
    db_host: str = os.getenv("db_host")
    db_name: str = os.getenv("db_name")
    db_port: str = os.getenv("db_port")
    db_echo: bool = os.getenv("db_echo") == "True"

    # secret_key: str = os.getenv("FLASK_WTF_SECRET")

    # selenium_host = os.getenv("selenium_host")
    # selenium_prefix = os.getenv("selenium_prefix")
    # selenium_port = os.getenv("selenium_port")
    # selenium_postfix = os.getenv("selenium_postfix")

    # rabbit_host = os.getenv("rabbit_host")
    # rabbit_user = os.getenv("rabbit_user")
    # rabbit_pass = os.getenv("rabbit_pass")
    # rabbit_port_int = int(os.getenv("rabbit_port"))
    # rabbit_timeout_int = int(os.getenv("rabbit_timeout"))
    # rabbit_expiration_seconds_int = int(os.getenv("rabbit_expiration_seconds"))
    # rabbit_front_listener_queue = os.getenv("rabbit_front_listener_queue")
    # rabbit_listener_parser_queue = os.getenv("rabbit_listener_parser_queue")

    # redis_host = os.getenv("redis_host")
    # redis_port_int = int(os.getenv("redis_port"))
    # redis_hash_field_count_name = os.getenv("redis_hash_field_count_name")
    # redis_message_hash_prefix = os.getenv("redis_message_hash_prefix")
    # redis_hash_list_name = os.getenv("redis_hash_list_name")
    # redis_hash_list_max_count_int = int(os.getenv("redis_hash_list_max_count"))
    # redis_hash_list_max_seconds_from_now_int = int(
    #     os.getenv("redis_hash_list_max_seconds_from_now")
    # )
    # redis_hash_algorithm = os.getenv("redis_hash_algorithm")

    # sentry_sdk_dsn = os.getenv("sentry_sdk_dsn")
