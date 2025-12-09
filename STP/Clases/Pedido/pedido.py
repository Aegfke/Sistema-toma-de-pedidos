from django.db import models
from ..Plato.plato import Plato
print(Plato)

## Una clase que representa un pedido.
# El pedido incluye un número identificador, su número
# de mesa y una lista de los platos.
class Pedido(models.Model):
    id = models.BigAutoField(primary_key=True)
    mesa = models.IntegerField()
    seleccionados = models.ManyToManyField('Plato', related_name='pedidos')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    servido = models.BooleanField(default=False)

    # getCuenta ::== None -> Int
    # Devuelve el precio total del pedido, luego de haber 
    # sumado los precios de cada plato individualmente.
    def getCuenta(self):
        total= 0
        for platos in self.seleccionados:
            valor = platos.getPrecio()
            total += valor
        return total
    
    # getMesa ::== None -> Int
    def getMesa(self):
        return self.mesa

    # total_precio ::== None -> Int
    def total_precio(self):
        return sum(plato.getPrecio() for plato in self.seleccionados.all())
    
    # setPedido ::== bool -> None
    def setPedido(self, statement):
        assert(statement.type == bool)
        self.servido = statement
        return None

    # __str__ ::== None -> Str
    # Gives the pedido id and the status
    def __str__(self):
        return f"Pedido #{self.id} - {'Listo' if self.listo else 'En preparación'}"