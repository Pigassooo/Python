class Accident(Exception):
    def __init__(self, message):
        self.message = message
    def handle(self):
        print("accident occured. Take detour")


try:
    raise Accident('crash between two cars')
except Accident as e:
    e.handle()