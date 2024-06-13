import os


class EnvironmentVariablesReader():
    def __init__(self, logger) -> None:
        self.logger = logger

        self.PORT = self.__get_env_var_int(
            name='PORT', 
            default=8000
            )
        self.API_KEY = self.__get_env_var_str(
            name='API_KEY', 
            default=''
            )
        self.MODEL = self.__get_env_var_str(
            name='MODEL', 
            default='gpt-4o'
            )
        self.TEMPERATURE = self.__get_env_var_float(
            name='TEMPERATURE', 
            default=0.1
            )
        self.PROMPT_GEN_SERVICE_HOST = self.__get_env_var_int('PROMPT_GEN_SERVICE_HOST', '0.0.0.0')
        self.PROMPT_GEN_SERVICE_PORT = self.__get_env_var_int('PROMPT_GEN_SERVICE_PORT', 8080)
        self.PROMPT_GEN_SERVICE_PATH = self.__get_env_var_str('PROMPT_GEN_SERVICE_PATH', 'generate')

    def __get_env_var_int(self, name, default):
        var = os.environ.get(name)

        if var:
            self.logger.info(f"Initializing variable {name} with {var}")
            return int(var)
        self.logger.info(f"Initializing variable {name} with default {default}")
        return default
    
    def __get_env_var_str(self, name, default):
        var = os.environ.get(name)

        if var:
            self.logger.info(f"Initializing variable {name} with {var}")
            return str(var)
        
        self.logger.info(f"Initializing variable {name} with default {default}")
        return default

    def __get_env_var_float(self, name, default):
        var = os.environ.get(name)

        if var:
            self.logger.info(f"Initializing variable {name} with {var}")
            return float(var)
        
        self.logger.info(f"Initializing variable {name} with default {default}")
        return default
