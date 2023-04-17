

class Vehicle:
    @staticmethod
    def drive():
        print("drive")


class BaseCar(Vehicle):
    speed = 300


class MixinLada:
    def drive(self):
        print("mixin is worked")
        super().drive()


class Car(MixinLada, BaseCar):
    pass


if __name__ == '__main__':
    car = Car()
    print(Car.__mro__)