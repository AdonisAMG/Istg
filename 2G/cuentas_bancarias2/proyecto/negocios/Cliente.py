from proyecto.datos.conexion_db_cuentas import Conexion

class Cliente:
    def validar_login(self,usuario,clave):
        consulta=Conexion()
        return consulta.cli_verificar_credenciales(usuario,clave)

    def consulta_datos_registro_by_cli(self,cliente):
        consulta = Conexion()
        return consulta.cli_consulta_datos_registro_by_cli(cliente)

    def consulta_registro_ahora(self,correo,celular,cedula):
        consulta=Conexion()
        return consulta.verificar_registro_ahora(correo,celular,cedula)

    def consulta_usuario(self,usuario):
        consulta=Conexion()
        return consulta.cli_verificar_usuario(usuario)


    def ingresar_cliente(self,correo,celular,cedula,
                         nombres,apellidos,fecha_nacimiento,
                         nombres_contacto,tlf_contacto,calle_princ,
                         numeracion,usuario,passwd):
        #0123456789
        #05/04/2022

        dia  = fecha_nacimiento[0:2]
        mes  = fecha_nacimiento[3:5]
        anio = fecha_nacimiento[6:10]
        #print("dia: ",dia,"   mes: ",mes,"   anio: ",anio)
        fecha_nac = anio + "/" + mes + "/" + dia
        #print("fecha_nacimiento: ",fecha_nac)

        consulta = Conexion()
        return consulta.cli_registra_datos(correo,celular,cedula,nombres,
                                           apellidos,fecha_nac,nombres_contacto,
                                           tlf_contacto,calle_princ,numeracion,
                                           usuario,passwd)


# clientes=Cliente()
# clientes.ingresar_cliente("juan12345@gmail.com.ec","0990154547","0919653532",
#                             "juan fernando","jimenez calderon","05/04/2022")
# clientes.validar_login("juan","1234