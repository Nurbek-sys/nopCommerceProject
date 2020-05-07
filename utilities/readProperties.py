import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")

class ReadConfig:
    @staticmethod
    def GetApplicationURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def GetUseremail():
        username = config.get('common info', 'useremail')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common info', 'password')
        return password
