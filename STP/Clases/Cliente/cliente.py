from user import User

class Cliente(User):
    def __init__(self, nombre, password):
        super().__init__(nombre, password, role="cliente")
    
    def hacer_pedido(self, id_pedido):
        print(f"Pidiendo el pedido con ID: {id_pedido}")

    def añadir_platillo(self, id_p):
        print(f"Se añadió al pedido el platillo con ID: {id_p}")

    def eliminar_platillo(self, id_p):
        print(f"Se eliminó el platillo con ID: {id_p}")

    def pagar(self, monto, id_cuenta):
        print(f"Se pagó {monto}$ por la cuenta con ID: {id_cuenta}")