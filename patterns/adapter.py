class European:  # adaptee
    def spec_request(self):
        return "This is European-type socket"


class American:  # target
    def request(self):
        return "This is American-type socket"
    

class Adapter(European, American):  # переходник с европейской на американскую вилку
    def request(self):
        return f"{self.spec_request()} + adapter EU to US"
    
def client_code(target: "American"):  # Условная розетка, куда нужно вставить нашу вилку
    print(target.request())
    print("Зарядка идет!")
    

if __name__=="__main__":
    print("Мы приехали в Америку и нам нужно зарядить ноутбук. Он скоро сядет, ведь мы играли весь полет играли в Солитера на ультрах :)\n")

    target = American()
    print("Подключаем ноутбук американской вилкой: ")
    client_code(target)
    print()

    adaptee = European()
    print("Пытаемся вставить Европейскую вилку: ")
    try:
        client_code(adaptee).request()
    except:
        print("Ошибка. Розетки не подходят! Ноутбук вот-вот сядет!")
    print()
    
    adapter = Adapter()
    print("Подключаем переходник к нашей европейской вилке: ")
    client_code(adapter)