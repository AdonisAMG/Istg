from proyecto.datos.conexion_db_cuentas import Conexion

class Movimiento:
    def crear_movimiento(self,mov_fecha,
                                mov_monto,
                                mov_saldo,
                                mov_estado,
                                cta_id):

        self.fecha=mov_fecha
        self.monto=mov_monto
        self.saldo=mov_saldo
        self.estado=mov_estado
        self.cta_id=cta_id

        consulta=Conexion()

        return consulta.mov_crear_movimientos(self.fecha,
        self.monto,
        self.saldo,
        self.estado,
        self.cta_id)

