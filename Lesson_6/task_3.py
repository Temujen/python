class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        print(f"Full name is {self.surname} {self.name}")

    def get_total_income(self):
        print(f"Total income = {sum(self._income.values())}")


person = Position("Вася", "Иванов", "менеджер", 50000, 12000)
person.get_full_name()
person.get_total_income()
