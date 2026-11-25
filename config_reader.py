import json

class ConfigReader:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self):
        if hasattr(self, 'config'):
            return
        else:
            with open("config.json", encoding="utf-8") as file:
                self.config = json.load(file)