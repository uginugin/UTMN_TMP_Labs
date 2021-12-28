from abc import ABC, abstractmethod

class Creator(ABC):  # интерфейс фабрики

    @abstractmethod
    def factory_method(self):
        pass


    def activity(self):
        generated = self.factory_method()
        return f"Класс создателя получил новый объект \"{generated.operation()}\" через фабричный метод"


class Product(ABC):  # интерфейс продукта
    @abstractmethod
    def operation(self):
        pass

class Sausage(Product):
    def operation(self):
        return "Обернутая сосиска"

class Bread(Product):
    def operation(self):
        return "Нарезанный хлеб"

class SausageCreator(Creator):
    def factory_method(self):
        print("Оборачиваем сосиску в пленку...")
        return Sausage()

class BreadCreator(Creator):
    def factory_method(self):
        print("Нарезаем хлеб...")
        return Bread()


def client_code(creator: Creator):
    print(f"Client: Я не знаю родительский класс, но процесс успешно работает!\n"
          f"{creator.activity()}", end="")

if __name__=="__main__":
    print("Идем в цех сосисок!")
    client_code(SausageCreator())
    print('\n')
    print("Идем в хлебный цех!")
    client_code(BreadCreator())