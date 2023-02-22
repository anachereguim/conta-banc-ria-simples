class Conta:
    def __init__(self, tit, saldo, num):
        self._saldo = saldo
        self._numero = num
        self._titular = tit

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        if(saldo<0):
            print("O saldo não pode ser negativo")
        else:
            self._saldo = saldo
    def get_numero(self):
        return self._numero

    def set_numero(self, num):
        self._numero = num
    
    def get_titular(self):
        return self._titular

    def set_titular(self, tit):
        self._titular = tit

    def saque(self, valor):
        while self.saldo < valor and valor != 0:
            print("Saldo insuficiente")
            cont = input("Deseja sacar outro valor? S/N \n")
            if(cont == "s" or cont == "S" ):
                valor= float(input ("Digite o valor que deseja sacar: "))
            else:
                valor == 0 
        self.saldo-=valor
        print("Saque realizado com sucesso")
        
          

    def deposita(self, valor):
        self.saldo +=valor

    def extrato(self):
        print("Cliente: ",self._titular, "Saldo: ", self._saldo)