class Car:

    def __init__(self, manufacturer, model, engine, colour, seats):
        self.manufacturer = manufacturer
        self.model = model
        self.engine = engine
        self.colour = colour
        self.seats = seats
        # self.extra_options = extra_options

    def owner_manual(self):
        print(f'''
        This is the owner\'s manual for {self.manufacturer} {self.model}:
        Car engine for this model is {self.engine}.
        The car colour is {self.colour}.
        The car has {self.seats} seats.
        ''')



car1 = Car('Mercedes-Benz', 'SLK', 2700, 'black', 2)
car2 = Car('Volvo', 'XC60', 'hybrid', 'grey', 6)
car3 = Car('Dacia', 'Duster', 'bi-fuel', 'Desert Orange metallic', 5)

car1.owner_manual()
