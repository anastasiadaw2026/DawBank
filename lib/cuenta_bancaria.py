from lib.constantes import Constantes
import re

class CuentaBancaria:
    def __init__(self, iban: str, titular: str):
        self._iban: str = self._comprobar_iban(iban)
        self._titular: str = self._comprobar_titular(titular)
        self._saldo: float = 0.0
        self._movimientos: list[float] = []

    @property
    def iban(self):
        return self._iban

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def movimientos(self):
        return self._movimientos

    def _comprobar_iban(self, valor):
        patron = re.compile(r'^[A-Z]{2}\d{22}$')
        valor1 = valor.replace(' ', '')
        if patron.match(valor1):
            return valor
        else:
            return ''

    def _comprobar_titular(self, valor):
        patron = re.compile(r'^[A-ZÉÍÁÓÚ][a-zñáéíóú]+[ ]['
                            r'A-Za-zÁÉÍÓÚÑáéíóúñ^\s]+$')
        if patron.match(valor):
            return valor
        else:
            return ''

    # cambios en el saldo y registro en los movimientos
    def _aniadir_movimiento(self, movimiento):
        if len(self._movimientos) > Constantes.MAXIMO_MOVIMIENTOS:
            self._movimientos = []
        self._movimientos += [movimiento]

    def introducir_ingreso(self, ingreso):
        if ingreso > 0 and isinstance(ingreso, float):
            self._saldo += ingreso
            if ingreso > Constantes.INGRESO_MAXIMO:
                print("AVISO: Notificar a hacienda.")
            self._aniadir_movimiento(ingreso)
            return True
        return False

    def introducir_retirada(self, retirada):
        if retirada > 0 and isinstance(retirada, float):
            self._saldo -= retirada
            if self._saldo <= Constantes.SALDO_MINIMO:
                print("AVISO: Saldo negativo.")
            self._aniadir_movimiento(-retirada)
            return True
        return False
