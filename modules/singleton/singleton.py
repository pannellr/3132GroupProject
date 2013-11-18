class Singleton:
    __instance = None

    def __init__(self, instance=None):
        self.__instance = instance

    def get_instance(self):
        if self.__instance == None :
            self.__instance = Singleton()
        return self.__instance
