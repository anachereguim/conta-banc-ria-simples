class Cliente:
    def __init__(self, nome, tel, end):
        self._nome = nome
        self._telefone = tel
        self._endereco = end
    
    def get_nome(self):
        return self._nome

    def set_nome(self, nome):
        self._nome = nome

    def get_telefone(self):
        return self._telefone

    def set_telefone(self, tel):
        self._telefone = tel

    def get_endereco(self):
        return self._endereco

    def set_endereco(self, end):
        self._endereco = end

    
