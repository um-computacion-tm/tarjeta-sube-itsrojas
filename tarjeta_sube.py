import unittest

PRECIO_TICKET = 70
DESACTIVADO = 'desactivado'
ACTIVADO = 'activado'
PRIMARIO = 'primario'
SECUNDARIO = 'secundario'
UNIVERSITARIO = 'universitario'
JUBILADO = 'jubilado'
DESCUENTOS = {
    'primario': 50,
    'secundario': 40,
    'universitario': 30,
    'jubilado': 25
}

class NoHaySaldoException(Exception):
    pass

class UsuarioDesactivadoException(Exception):
    pass

class EstadoNoExistenteException(Exception):
    pass

class Sube:
    def __init__ (self):
        self.saldo = 0
        self.grupo_beneficiario = None
        self.estado = ACTIVADO
        self.precio_ticket = 0

    def obtener_precio_ticket(self):
        if self.grupo_beneficiario in DESCUENTOS:
            self.precio_ticket = PRECIO_TICKET - DESCUENTOS[self.grupo_beneficiario]
        else:
            self.precio_ticket = PRECIO_TICKET
        return self.precio_ticket
        
    def pagar_pasaje(self):
        self.obtener_precio_ticket() 
        if self.saldo < self.precio_ticket:
            raise NoHaySaldoException("No hay saldo suficiente para pagar el pasaje.")
        if self.estado == DESACTIVADO:
            raise UsuarioDesactivadoException("El usuario está desactivado. No se puede pagar el pasaje.")
        self.saldo -= self.precio_ticket
        return self.saldo
    
    def cambiar_estado(self, estado):
        if estado == DESACTIVADO:  
            self.estado = DESACTIVADO
        elif estado == ACTIVADO:  
            self.estado = ACTIVADO
        else:
            raise EstadoNoExistenteException('Hay un problema en el estado del usuario')
        return self.estado

    
    def agregar_saldo(self):
        if self.saldo <= PRECIO_TICKET:
            self.saldo += 500
        return self.saldo
    
    
if __name__ == '__main__':
    unittest.main()
