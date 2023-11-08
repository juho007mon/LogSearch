import yaml

class ConfigLoader:
    @staticmethod
    def load_config(file_path):
        with open(file_path, 'r') as file:
            config = yaml.safe_load(file)
        return config