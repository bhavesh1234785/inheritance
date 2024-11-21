#parent class
class bird:
    def __init__(self):
        print("bird is ready")
    def whoisthis(self):
        print("bird")
    def swim(self):
        print("swim faster")
#child class
class penguin(bird):
    def __init__(self):
        #call super() function
        super().__init__()
        print("penguin is ready")
    def whoisthis(self):
        print("penguin")
    def run(self):
        print("run faster")
peggy=penguin()
peggy.whoisthis()
peggy.swim()
peggy.run()