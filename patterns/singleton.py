class SingletonMeta(type):

    _instances = {}
    def __call__(cls, *args, **kwargs):  # вызывается, когда создается потомок
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):

    def display(self):
        print(f"Привет, я- {self}")


if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton('что - то другое')

    obj1.display()
    obj2.display()