import sys

from UsuarioDAO import UsuarioDAO
from Usuario import Usuario
from logger_base import log

opcion = None

while opcion !=5:
    print(f'Opciones: ')
    print('1. Listar Usuarios')
    print('2. Agregar Usuario')
    print('3. Modificar Usuario')
    print('4. Borrar usuario')
    print('5. Salir')
    print('')
    opcion = int(input('Seleccione una opción (1-5): '))
    if opcion==1:
        usuarios = UsuarioDAO.seleccionar()
        for usuario in usuarios:
            print(usuario)
        print('')
    elif opcion==2:
        usuario1 = Usuario(username=input('Ingrese el username: '), password=input('Ingrese el password: '))
        usuario_insertado = UsuarioDAO.insertar(usuario1)
        print(f'Usuario insertado: {usuario_insertado}')
        print('')
    elif opcion==3:
        usuario1 = Usuario(int(input('Ingrese el id del usuario: ')), input('Ingrese el nuevo username: '), input('Ingrese el nuevo password: '))
        usuario_actualizado = UsuarioDAO.actualizar(usuario1)
        print(f'Usuarios Actualizados: {usuario_actualizado}')
        print('')
    elif opcion==4:
        usuario1 = Usuario(id_usuario=int(input('Ingrese el id del usuario a borrar: ')))
        usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
        print(f'Usuarios eliminadas: {usuarios_eliminados}')
        print('')
else:
    log.info('Salimos de la aplicación.')
