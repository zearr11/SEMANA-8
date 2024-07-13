
class Curso:
    
    def __init__(self, codigo, nombre, credito):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__credito = credito
        
    def bienvenido(self):
        print(f"Welcome to the curse {self.__nombre}. I have {self.__credito} credits.")
        
    def c_curso(self):
        print(f"Nombre del curso: {self.__nombre}")
        print(f"Codigo del curso: {self.__codigo}")
        print(f"Creditos del curso: {self.__credito}")
        
    def set_codigo(self, codigo):
        self.__codigo = codigo
        
    def set_nombre(self, nombre):
        self.__codigo = nombre
        
    def set_credito(self, credito):
        self.__credito = credito
        
   
    def get_codigo(self):
        return self.__codigo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_credito(self):
        return self.__credito
    