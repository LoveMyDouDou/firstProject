


class Hello:
    def __init__(self,name):
        self.name=name

    def sayHello(self):
        print ("Hello Python {0}".format(self.name))

h=Hello("Newer")
h.sayHello()


class Hi(Hello):
    def __init__(self,name):
        Hello.__init__(self,name)
    def sayHi(self):
        print ("Hi {0}".format(self.name))

h1=Hi("Newer")
h1.sayHi()