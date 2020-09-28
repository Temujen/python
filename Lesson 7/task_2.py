from abc import ABC, abstractmethod


class Clothes(ABC):
    sum_clothes = 0

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def tissue_for_clothes(self):
        pass


class Coast(Clothes):
    def __init__(self, name, size):
        super().__init__(name)
        self.v = size

    @property
    def tissue_for_clothes(self):
        if self.v > 0:
            result = self.v / 0.65 + 0.5
            Clothes.sum_clothes += result
            return round(result, 3)
        else:
            print("Enter only positive numbers")


class Costume(Clothes):
    def __init__(self, name, growth):
        super().__init__(name)
        self.h = growth

    @property
    def tissue_for_clothes(self):
        if self.h > 0:
            result = 2 * self.h + 0.3
            Clothes.sum_clothes += result
            return round(result, 3)
        else:
            print("Enter only positive numbers")


coast = Coast('coast', 3)
print(f"Used {coast.tissue_for_clothes} tissue for {coast.name}")
costume = Costume('suit', 5)
print(f"Used {costume.tissue_for_clothes} tissue for {costume.name}")
print(f"Total used tissue {round(costume.sum_clothes, 3)}")
cloak = Coast("Плащ", 2)
print(f"Used {cloak.tissue_for_clothes} tissue for {cloak.name}")

