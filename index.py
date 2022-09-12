class automovil:
    

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def dar_marca(self):
        return self.marca

    def dar_modelo(self):
        return self.modelo

    def __str__(self):
        return "%s El automovil es un %s" % (self.marca, self.modelo)


class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hablar (self):
        print (f"Mi nombre es {self.nombre}. Tengo {self.edad} años.")

    def saludar (self, persona):
        if persona.name == "Pablo":
            print ("Hola vecino!")
        else:
            print (f"Hola {persona.name}!")
