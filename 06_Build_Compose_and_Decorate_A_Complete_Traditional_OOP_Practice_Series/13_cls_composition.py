
# 13. Composition Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the
# Car class during initialization. Access a method of the Engine class via the Car class.




class Engine:

    def start(self):
        return "Engine Started"
        
    def stop(self):
        return "Engine Stoped"

class Car:
    def __init__(self, engine):
        self.engine = engine

    def started(self):
        return self.engine.start()

    def stoped(self):
        return self.engine.stop()



engine = Engine()

car = Car(engine)

print(car.started())

print(car.stoped())