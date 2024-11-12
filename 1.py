import json

class Persona:
    def __init__(self, nombre, edad, altura):
        self.__nombre = nombre
        self.__edad = edad
        self.__altura = altura


    def to_json(self):
        persona1={"nombre":self.__nombre, "edad":self.__edad, "altura":self.__altura}
        return json.dumps(persona1)
    @classmethod
    def from_json(cls,json_data):
        datos=json.loads(json_data)
        return cls(datos["nombre"],datos["edad"],datos["altura"])
    
if __name__ == "__main__":
    persona1 = Persona("Juan", 25, 1.75)
    print(persona1.to_json())
    persona2=Persona.from_json(persona1.to_json())
    print(persona2.to_json())
#cual es el error?
#porque necesita si o si el decordadoadsr?sasadasdsassaassadsaasdaasdassadsaas