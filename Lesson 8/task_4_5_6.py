class Store:
    def __init__(self):
        self.storage = {}
        self.transferred = {}

    def accept_storage(self, name, number):
        try:
            if int(number) < 0:
                raise ValueError
            else:
                if self.storage.get(name):
                    self.storage[name] += int(number)
                else:
                    self.storage[name] = int(number)
        except ValueError:
            print(f"Only integer positive number for {name}")

    def list_status(self):
        return f"Storage {self.storage}", f" Transferred to department {self.transferred}"

    def transfer_to_dept(self, name, number, dept):
        if self.storage.get(name):
            if self.storage[name] >= number:
                self.transferred[dept] = {name: number}
                self.storage[name] -= number
                self.storage.pop(name) if self.storage.get(name) == 0 else True
            else:
                print(f"We have only {self.storage[name]} {name}")

        else:
            print(f"We don't have {name} model in Store")


class Equipment:
    def __init__(self, vendor, model):
        self.vendor = vendor
        self.model = model


class Printer(Equipment):
    def __init__(self, vendor, model, speed_print, type):
        super().__init__(vendor, model)
        self.speed_print = speed_print
        self.type = type


class Scanner(Equipment):
    def __init__(self, vendor, model, dpi):
        super().__init__(vendor, model)
        self.dpi = dpi


class Copier(Equipment):
    def __init__(self, vendor, model, format):
        super().__init__(vendor, model)
        self.format = format


store_1 = Store()
printer1 = Printer('Canon', 'LX-35', '50p/m', 'jet')
scanner1 = Scanner('Epson', 'sg', '1200')
copier1 = Copier('Xerox', 'QA', 'A4')

store_1.accept_storage(printer1.vendor, 2)
store_1.accept_storage(scanner1.vendor, 4)
store_1.accept_storage(copier1.vendor, 2)
print(store_1.list_status())
store_1.transfer_to_dept(printer1.vendor, 2, 'accountant')
store_1.transfer_to_dept(scanner1.vendor, 4, 'IT')
print(store_1.list_status())

