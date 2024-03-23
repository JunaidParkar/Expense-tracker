import os
from enum import Enum        

class RouteType(Enum):
    ASSETS_DIR = bin(25558)
    ASSETS_FONT_DIR = bin(52102561502)
    DATABASE_DIR = bin(520)
    DATABASE_USER = bin(521)
    DATABASE_MAIN_DIR = bin(1200000000)

class routes:
    def __init__(self, username):
        self.__ASSETS_DIR = os.path.join(os.getcwd(), "assets")
        self.__ASSETS_FONT_DIR = os.path.join(self.__ASSETS_DIR, "font")
        self.__DATABASE_DIR = os.path.join(os.getcwd(), "database")
        self.__DATABASE_USER = os.path.join(self.__DATABASE_DIR, str(username))
        self.__DATABASE_MAIN_DIR = os.path.join(self.__DATABASE_USER, "main.db")

    def getRoute(self, name: RouteType = RouteType.ASSETS_DIR):
        if name == RouteType.ASSETS_DIR:
            return self.__ASSETS_DIR
        elif name == RouteType.ASSETS_FONT_DIR:
            return self.__ASSETS_FONT_DIR
        elif name == RouteType.DATABASE_DIR:
            return self.__DATABASE_DIR
        elif name == RouteType.DATABASE_USER:
            return self.__DATABASE_USER
        elif name == RouteType.DATABASE_MAIN_DIR:
            return self.__DATABASE_MAIN_DIR

a = routes("self")
d = a.getRoute(RouteType.DATABASE_MAIN_DIR)