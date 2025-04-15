class Usuario:
    def __init__(self,nombre,email):
        self.nombre=nombre
        self.email=email
    
    def enviar_correo(self,asunto,mensaje):
        #logica para enviar correo electronico
        print(f'enviando correo a {self.email} con asunto {asunto} y mensaje {mensaje}')
    
    def guardar_registro(self,accion):
        #logica para guardar registro de acciones del usuario
        print(f'Guardando registro de accion: {accion}')

class GestorUsuarios:
    def __init__(self):
        self.usuarios=[]
    
    def agregar_usuario(self,nombre,email):
        usuario=Usuario(nombre,email)
        self.usuarios.append(usuario)
        usuario.enviar_correo('Bienvenido','Gracias por Registrarse')
        usuario.guardar_registro('Registro de Usuario')

gestor_usuarios=GestorUsuarios()
gestor_usuarios.agregar_usuario('Juan','juan@example.com')