class smartphone:     #base class
    def __init__(self, brand, price, model, os):
        self.brand = brand
        self.price = price  
        self.model = model
        self._os = os  #  private attribute

    def get_model(self):
        return self.model  

    def get_os(self):
        return self._os

    def get_price(self):
        return self.price

class iphone(smartphone):
        def __init__(self, model, price, storage, color, os):
            super().__init__("Apple", price, model, os)
            self.storage = storage
            self.color = color

        def get_storage(self):
            return self.storage

        def get_color(self):
            return self.color

smartphones = [
    iphone("iPhone 14", 999, "128GB", "Black", "iOS 16"),
    iphone("iPhone 14 Pro", 1099, "256GB", "Gold", "iOS 16"),
    smartphone("Samsung Galaxy S21", 799, "Galaxy S21", "Android 11"),
]
for phone in smartphones:
      print(f"Model: {phone.get_model()}")
      print(f"OS: {phone.get_os()}")
      print(f"Price: {phone.get_price()}")
      if isinstance(phone, iphone):
          print(f"Storage: {phone.get_storage()}")
          print(f"Color: {phone.get_color()}")
      else:
          print(f"Brand: {phone.brand}")

      print()


class animal:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Dog(animal):
     def __init__(self, sound):
         super().__init__(sound)
     def make_sound(self):
         return "Woof! Woof!"

class Cat(animal):
     def __init__(self, sound):
         super().__init__(sound)
     def make_sound(self):
         return "Meow! Meow!"

Dog_sound = Dog("Woof")
Cat_sound = Cat("Meow")
print(f"DOG: {Dog_sound.make_sound()}")
print(f"CAT: {Cat_sound.make_sound()}")