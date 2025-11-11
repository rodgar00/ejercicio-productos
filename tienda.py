import random
import secrets


class Product:
    def __init__(self, name, price):
        self.is_valid_text(name)
        self.is_valid_price(price)

        self.__name = name
        self.__price = price

    @staticmethod
    def is_valid_text(name):
        if name.isnumeric():
            raise ValueError("El nombre del producto no puede ser un número")
        if name is None:
            raise ValueError("El nombre del producto no puede estar vacío")
        if len(name) < 3:
            raise ValueError("El nombre del producto debe tener 3 caracteres")

    @staticmethod
    def is_valid_price(price):
        if not price.isnumeric():
            raise ValueError("Precio debe ser un número")
        if price is None:
            raise ValueError("El precio no puede estar vacío")
        if float(price) < 0:
            raise ValueError("El precio debe ser mayor que 0")

    @property
    def stockRandom(self):
        return random.randint(0,1)

    @property
    def codeUnico(self):
        return secrets.token_hex(15)

    @property
    def isActive(self):
        if self.stockRandom > 0:
            return True
        else:
            return False


    def __str__(self):
        return f"[{self.codeUnico}] {self.__name} -> Precio {self.__price}€ (stock: [{self.stockRandom}])"
