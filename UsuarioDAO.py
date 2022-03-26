from Cursor import CursorDelPool
from Usuario import Usuario
from logger_base import log


class UsuarioDAO:
    '''
    DAO (DATA ACCESS OBJECT)
    CRUD(CREATE-READ-UPDATE-DELETE)
    '''
    _SELECCIONAR = 'SELECT * FROM Usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO Usuario(username,password) VALUES(%s,%s)'
    _ACTUALIZAR = 'UPDATE Usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM Usuario WHERE id_usuario=%s'

    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            usuarios=[]
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios


    @classmethod
    def insertar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password)
            cursor.execute(cls._INSERTAR, valores)
            log.debug(f'Usuario agregado: {usuario}')
            return cursor.rowcount


    @classmethod
    def actualizar(cls,usuario):
        with CursorDelPool() as cursor:
            valores = (usuario.username, usuario.password, usuario.id_usuario)
            cursor.execute(cls._ACTUALIZAR, valores)
            log.debug(f'Usuario actualizado: {usuario}')
            return cursor.rowcount


    @classmethod
    def eliminar(cls,usuario):
        with CursorDelPool() as cursor:
                valores = (usuario.id_usuario,)
                cursor.execute(cls._ELIMINAR, valores)
                log.debug(f'Usuario eliminado: {usuario}')
                return cursor.rowcount


if __name__ == '__main__':
    # INSERTAR OBJETO
    # usuario1 = Usuario(username='niicopvp', password='niconico14')
    # usuario_insertado = UsuarioDAO.insertar(usuario1)
    # log.debug(f'Usuario insertado: {usuario_insertado}')

    #ACTUALIZAR UNA PERSONA
    usuario1 = Usuario(4, 'Niicopvp', 'nico1414')
    usuario_insertado = UsuarioDAO.actualizar(usuario1)
    log.debug(f'Usuarios Actualizados: {usuario_insertado}')

    #BORRAR PERSONA
    # usuario1= Usuario(id_usuario=2)
    # usuarios_eliminados = UsuarioDAO.eliminar(usuario1)
    # log.debug(f'Usuarios eliminadas: {usuarios_eliminados}')

    #SELECCIONAR OBJETO
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
