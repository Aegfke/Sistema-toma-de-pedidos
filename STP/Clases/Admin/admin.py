from user import User

class Admin(User):
    def __init__(self, nombre, password):
        super().__init__(nombre, password, role="admin")

    def ver_pedido(self, id_pedido):
        # lógica para ver pedido
        print(f"Viendo el pedido con ID: {id_pedido}")

    def empezar_formulario(self, id_formulario):
        # lógica para crear/editar platillo
        print(f"Iniciando formulario para el platillo con ID: {id_formulario}")

    def agregar_platillo(self, id_p, nombre, categoria, precio, ingredientes, foto):
        # lógica para agregar un nuevo platillo
        print(f"Agregando platillo: {nombre}, Categoría: {categoria}, Precio: {precio}")

    def gestionar_platillo(self, id_p, nombre=None, categoria=None, precio=None, ingredientes=None, foto=None):
        # lógica para actualizar un platillo existente
        print(f"Gestionando platillo con ID: {id_p}")