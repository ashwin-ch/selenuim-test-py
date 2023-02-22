import os
import logging as log

# This module contains all the configurations for different env
# such as production, qa and development

class ConfigLoader:

    ENV = os.getenv("env")

    @classmethod
    def load_config(cls):
        log.info("Setting up config based on environment: %s", cls.ENV)
        config_by_env = {
            "qa" : QAConfig,
            "dev" : DevConfig,
            "prod": ProdConfig
        }

        return config_by_env[cls.ENV]()

class QAConfig:
    environment = "qa"
    url = "http://the-internet.herokuapp.com"

class DevConfig:
    environment = "dev"
    url = "http://the-internet.herokuapp.com"

class ProdConfig:
    environment = "prod"
    url = "http://the-internet.herokuapp.com"
