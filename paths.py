import os
from enum import Enum        

class RouteType(Enum):
    ASSETS_DIR = bin(25558)
    ASSETS_FONT_DIR = bin(52102561502)
    DATABASE_DIR = bin(520)
    DATABASE_USER_DIR = bin(521)
    DATABASE_MAIN_DB = bin(1200000000)
    DATABASE_USER_EXPENSE_DIR = bin(46552)

class routes:
    def __init__(self, username):
        self.__ASSETS_DIR = os.path.join(os.getcwd(), "assets")
        self.__ASSETS_FONT_DIR = os.path.join(self.__ASSETS_DIR, "font")
        self.__DATABASE_DIR = os.path.join(os.getcwd(), "database")
        self.__DATABASE_USER_DIR = os.path.join(self.__DATABASE_DIR, str(username))
        self.__DATABASE_MAIN_DB = os.path.join(self.__DATABASE_USER_DIR, "main.db")
        self.__DATABASE_USER_EXPENSE_DIR = os.path.join(self.__DATABASE_USER_DIR, "exp")

    def getRoute(self, name: None):
        if name == RouteType.ASSETS_DIR:
            return self.__ASSETS_DIR
        elif name == RouteType.ASSETS_FONT_DIR:
            return self.__ASSETS_FONT_DIR
        elif name == RouteType.DATABASE_DIR:
            return self.__DATABASE_DIR
        elif name == RouteType.DATABASE_USER_DIR:
            return self.__DATABASE_USER_DIR
        elif name == RouteType.DATABASE_MAIN_DB:
            return self.__DATABASE_MAIN_DB
        elif name == RouteType.DATABASE_USER_EXPENSE_DIR:
            return self.__DATABASE_USER_EXPENSE_DIR
        
    def getExpenseDBPathsList(self):
        return os.listdir(self.getRoute(RouteType.DATABASE_USER_EXPENSE_DIR))
        
    def geDirList(self):
        return [self.__ASSETS_DIR, self.__ASSETS_DIR, self.__DATABASE_DIR, self.__DATABASE_USER_DIR, self.__DATABASE_USER_EXPENSE_DIR]