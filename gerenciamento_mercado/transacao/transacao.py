from datetime import datetime

class Transacao:
    def __init__(self, cliente, produto, quantidade):
        self.data = datetime.now()
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade

    def __str__(self):
        return f"Data: {self.data} - Cliente: {self.cliente.nome} - Produto: {self.produto.nome} - Quantidade: {self.quantidade}"
