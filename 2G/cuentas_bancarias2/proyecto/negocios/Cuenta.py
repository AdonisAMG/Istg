from examen.datos.cuenta_bancaria import *
class Cuenta:
    def consulta_saldo(self, cta_numero,cta_saldo):
        self.numero_cuenta=cta_numero()
        self.saldo=cta_saldo()
        if not consulta.consulta_saldo(cta_numero):
            return False

consulta=Cuenta()
print(consulta.consulta_saldo(any))
