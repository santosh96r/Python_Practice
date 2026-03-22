import logging
logging.basicConfig( level=logging.DEBUG, filemode='a', filename="logs/demologs.log", format="%(asctime)s - %(levelname)s : %(message)s ", datefmt="%d/%m/%Y %I:%M:%S: %p ")

class DemoLogging:
    d = 50
    def __init__(self, a, b):
        self.a = a 
        self.b = b 
        self.c = 10

    def add_numbers(self):
        return self.a + self.b + DemoLogging.d + self.c
    
    def multiply_nums(self):
        return self.a * self.b 
    
obj1 = DemoLogging(10,13)
print(obj1.c)
print(DemoLogging.d)
# print(obj1.add_numbers())
result_add = obj1.add_numbers()
logging.debug("debug : addition of number is : {}".format(result_add))
logging.info("debug : addition of number is : {}".format(result_add))
logging.warning("debug : addition of number is : {}".format(result_add))

