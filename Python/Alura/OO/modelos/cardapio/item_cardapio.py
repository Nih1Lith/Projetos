from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self,nome,preco):
        self._nome = nome
        self._preco = preco

    #O decorador @abstractmethod é usado em conjunto com a classe abstrata (que usa ABC, a partir do módulo abc) para definir métodos que devem ser implementados pelas subclasses. Ele força que subclasses implementem um método específico, garantindo que o contrato de implementação seja seguido.
    # Funcionamento:
    # Classes abstratas são classes que não podem ser instanciadas diretamente, servem como um modelo ou esqueleto para outras classes.
    # Os métodos marcados com @abstractmethod precisam ser obrigatoriamente implementados nas subclasses.
    @abstractmethod
    def aplicar_desconto(self):
        pass