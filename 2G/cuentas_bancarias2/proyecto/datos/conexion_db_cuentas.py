import mysql.connector

class Conexion:

    #constructor para realizar la conexion con la base de datos
    def __init__(self):
        self.cnn=mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            passwd="root",
            database="cajero_electronico")

    #########################################################################################
    ## TABLA CLIENTES
    #########################################################################################
    #REGISTRA DATOS DE USUARIO
    ####################
    def cli_registra_datos(self,correo,celular,cedula,nombres,apellidos,fecha_nacimiento):
        sql="""insert into clientes(cli_correo,cli_celular,cli_cedula,
        cli_nombres,cli_apellidos,cli_fecha_nac)
        values('{}','{}','{}','{}','{}','{}')""".format(correo,celular,cedula,nombres,apellidos,fecha_nacimiento)
        #print(sql)

        cursor=self.cnn.cursor()
        cursor.execute(sql)
        n=cursor.rowcount
        self.cnn.commit()

        if not n:
            return False

        sql="select LAST_INSERT_ID()"
        cursor.execute(sql)
        datos=cursor.fetchall()
        if not len(datos):
            return False

        id_cliente = datos[0][0]
        return id_cliente


    #VERIFICAR SI USUARIO EXISTE
    def cli_verificar_usuario(self,usuario):
        sql="""SELECT 'X'
        FROM clientes 
        WHERE usuario ='{}' 
        AND cli_estado={}""".format(usuario,True)
        #print(sql)

        cursor=self.cnn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()
        cursor.close()

        if len(datos)==0:
            return True

        return False


    ###########################################################
    # VERIFICAR CREDENCIALES DE CLIENTE
    ###########################################################
    def cli_verificar_credenciales(self, usuario, passwd):
        sql = """select cli_id
              from clientes
              where (usuario='{}' or cli_correo='{}')
              and clave='{}'
              and cli_estado={}""".format(usuario, usuario, passwd, True)
        # print(sql)

        cursor = self.cnn.cursor()
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()

        if not len(datos):
            return False

        return datos[0][0]

    ###########################################################
    # CONSULTA DATOS DE REGISTRO POR CLIENTE
    ###########################################################
    def cli_consulta_datos_registro_by_cli(self, cliente):
        sql = """SELECT cli_correo, cli_cedula, cli_celular
           from clientes
           WHERE cli_id = {}
           AND cli_estado = {}""".format(cliente, True)
        #print(sql)
        cursor = self.cnn.cursor()
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()

        if not len(datos):
            return False

        lista_cli = []
        for registro in datos[0]:
            lista_cli.append(registro)

        # print(lista_cli)
        return lista_cli

    ###########################################################
    # CONSULTA SI UN CLIENTE YA SE ENCUENTRA REGISTRADO EN LA TABLA CLIENTES
    # DEVUELVE: TRUE SI NO SE ENCUENTRA REGISTRADO EL CLIENTE
    #           FALSE SI EL CLIENTE ESTA REGISTRADO
    ###########################################################
    def verificar_registro_ahora(self,correo,celular,cedula):
        sql="""SELECT 'x' 
        FROM clientes 
        WHERE CLI_CORREO ='{}' 
        OR CLI_cedula = '{}' 
        OR cli_celular='{}'
        AND cli_estado={}""".format(correo,cedula,celular,True)
        #print(sql)

        cursor=self.cnn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()
        cursor.close()

        if len(datos)==0:
            return True

        return False


    #########################################################################################
    ## TABLA CUENTAS
    #########################################################################################
    def cta_generar_numero(self):
        sql="""SELECT IFNULL(MAX(cta_numero)+1,90000) 
        FROM cuentas_bancarias"""
        # print(sql)

        cursor=self.cnn.cursor()
        cursor.execute(sql)
        datos=cursor.fetchall()
        cursor.close()

        if not len(datos):
            return False

        return datos[0][0]

    ###########################################################
    # SALDO DISPONIBLE POR CLIENTE
    ###########################################################
    def cta_saldo_disponible_by_cli(self, cliente):
        sql = """SELECT cta_id,CTA_NUMERO,CTA_SALDO 
     FROM cuentas_bancarias
    WHERE CLI_ID={}
      AND CTA_ESTADO={}""".format(cliente, True)
        #print(sql)

        cursor = self.cnn.cursor()
        cursor.execute(sql)
        datos = cursor.fetchall()
        cursor.close()

        if not len(datos):
            return -1

        lista_cta = []
        for registro in datos[0]:
            lista_cta.append(registro)

        return lista_cta

    ###########################################################
    # DEPOSITAR POR CUENTA BANCARIO
    ###########################################################
    def cta_depositar_by_cta(self,numero_cta,saldo):
        sql="""   
UPDATE cuentas_bancarias
set cta_saldo={}
WHERE cta_numero=   '{}'
AND cta_estado={};""".format(saldo,numero_cta,True)
        #print(sql)
        cursor=self.cnn.cursor()
        cursor.execute(sql)
        n=cursor.rowcount
        print(f"datos ingresados(deposito): {n}")
        self.cnn.commit()
        cursor.close()

        if not n:
            return False

        return True

    #crear una cuenta para un cliente
    def cta_crear_cuenta(self, cliente,numero_cta,
        saldo,tipo_cta,clave,estado):

        sql="""insert into cuentas_bancarias
        (cli_id,cta_numero,cta_saldo,cta_tipo,cta_clave,cta_estado)
        values({},'{}',{},'{}','{}',{})""".format(cliente,numero_cta,
        saldo,tipo_cta,clave,estado)
        #print(sql)

        cursor=self.cnn.cursor()
        cursor.execute(sql)
        n=cursor.rowcount
        self.cnn.commit()

        if not n:
            return False

        return True

    #########################################################
    ## TABLA MOVIMIENTOS
    #########################################################
    def mov_crear_movimientos(self,mov_fecha,mov_monto,mov_saldo,mov_estado,cta_id):
        sql = """insert into movimientos
               (mov_fecha,mov_monto,mov_saldo,mov_estado,cta_id)
               values('{}',{},{},{},{})""".format(mov_fecha,mov_monto,mov_saldo,mov_estado,cta_id)
        print(sql)

        cursor = self.cnn.cursor()
        cursor.execute(sql)
        n = cursor.rowcount
        self.cnn.commit()

        if not n:
            return False

        return True

    #########################################################
    ## TABLA CLIENTES
    #########################################################
    # def cta_consulta_datos_by_cli(self,cliente):
    #     sql="""SELECT cta_id,cta_numero,cta_saldo,cta_tipo
    #     FROM cuentas_bancarias
    #     WHERE cli_id={}
    #     AND cta_estado={}""".format(cliente,True)
    #     print(sql)
    #
    #     cursor = self.cnn.cursor()
    #     cursor.execute(sql)
    #     datos = cursor.fetchall()
    #     cursor.close()
    #
    #     if not len(datos):
    #         return False
    #
    #     lista_cta = []
    #     for registro in datos[0]:
    #         lista_cta.append(registro)
    #
    #     #print(lista_cta)
    #     return lista_cta
    #
    #
    #
    # def cta_crear_cuenta(self,numero_cta,saldo,tipo_cta,clave,estado):
    #     sql="""insert into cuentas_bancarias(numero_cuenta,saldo,tipo,clave,estado)
    #     values('{}',{},'{}',{},{})""".format(numero_cta,saldo,tipo_cta,clave,estado)
    #     print(sql)
    #
    #     cursor=self.cnn.cursor()
    #     cursor.execute(sql)
    #     n = cursor.rowcount
    #     print(f"datos ingresados: {n}")
    #     self.cnn.commit()
    #
    # def cta_saldo_disponible(self,numero_cta):
    #     sql="""SELECT saldo
    #     from cuentas_bancarias WHERE
    #     numero_cuenta = '{}'""".format(numero_cta)
    #     print(sql)
    #
    #     cursor=self.cnn.cursor()
    #     cursor.execute(sql)
    #     datos=cursor.fetchall()
    #     print(datos)
    #     cursor.close()
    #     return datos[0][0]





# consulta = Conexion()
# consulta.mov_crear_movimientos('2022-04-11 17:51',100,1000,True,5)
# consulta.cta_crear_cuenta(5,"0902",0,"A","1234",True)


# print(consulta.cta_generar_numero())
# print(consulta.cli_registra_datos("juan12345@gmail.com.ec","0990154547","0919653532",
#                             "juan fernando","jimenez calderon","2022/04/05"))

#print(cuenta.verificar_registro_ahora("juan@ccc.com","7878","787878"))
# # print(cuenta.cli_verificar_credenciales("juan","1234"))
#
# print(cuenta.cli_consulta_datos_registro_by_cli(5))
# print(cuenta.cta_saldo_disponible_by_cli(5))
#print(str(cuenta.cta_depositar_by_cta("0900",1)))