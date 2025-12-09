from django.db import models

class Plato(models.Model):
    id = models.BigAutoField(primary_key=True)
    precio = models.IntegerField()
    categoria = models.CharField(max_length=50)
    nombre = models.CharField(max_length=150)
    ingredientes = models.CharField(max_length=150)

    def setIngredientes(self, newIngredientes):
        self.ingredientes = newIngredientes

    def setCategoria(self, newCategoria):
        self.categoria = newCategoria

    def setNombre(self, newNombre):
        self.nombre = newNombre

    def setFoto(self, newFoto):
        self.foto = newFoto

    def setPrecio(self, newPrecio):
        self.precio = newPrecio

    def getPrecio(self):
        return self.precio
        
    def inyeccionFormulario(Cat, Nom, Pre, Path, NIng):
        print("Inyección en formulario")
