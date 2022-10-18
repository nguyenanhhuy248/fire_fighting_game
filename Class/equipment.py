

class Equipment:
    
    def __init__(self, name):
        self.name = name

    def display(self):
        return (f'Item: {self.name}')    
    

class Extinguisher (Equipment):
    
    def __init__(self, name, power):
        super().__init__(name)
        self.power = power

    def display(self):
        return (f'Item: {self.name}, Power: {self.power}')


class Mask (Equipment):
    
    def __init__(self, name):
        super().__init__(name)


if __name__ == '__main__':
    item = Mask('oxygen mask')
    print(item.display())

    item = Extinguisher('Dry powder extinguisher',5)
    print(item.display())