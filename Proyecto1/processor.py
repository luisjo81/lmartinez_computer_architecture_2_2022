from random import randint
import numpy as np

class Processor:
    def __init__(self, num_processor):
        self.num_processor = num_processor
        pass
    
    #Function to generate a random instruction
    def instruction_generator(self):
        #Variable to store the created instruction
        self.instruction = ""

        #Adding the processor to the instruction
        if self.num_processor == 0:
            self.instruction = "P0: "
        if self.num_processor == 1:
            self.instruction = "P1: "
        if self.num_processor == 2:
            self.instruction = "P2: "
        if self.num_processor == 3:
            self.instruction = "P3: "

        #Adding the type of instruction
        operation = self.poisson(1)
        #READ
        if operation == 0:
            self.instruction = self.instruction + "READ "
            self.instruction = self.instruction + self.address_generator()
            return self.instruction
        #WRITE
        if operation == 1:
            self.instruction = self.instruction + "WRITE "
            self.instruction = self.instruction + self.address_generator() 
            self.instruction = self.instruction + ";" + self.value_generator()
            return self.instruction
        #CALC
        if operation == 2:
            self.instruction = self.instruction + "CALC"
            return self.instruction

    """ 
        Function to calculate a random number using Poisson probability distribution
                     x
        P(X <= x) =  E  [(lambda^n) / n!] e^(-lambda)
                    n=0     

        params:
            - l: int lambda value
    """
    def poisson(self, l):
        e = np.exp(-l)
        n = 0
        u = np.random.uniform(0,1)
        p = e
        fact = 1
        pow = 1
        while u > p:
            n = n + 1
            fact = n * fact
            pow = l * pow 
            p = p + (pow / fact) *e
            if n == 2:
                break 
        return n 
    
    #Function to create a random address
    def address_generator(self):
        int_address = randint(0, 7)
        bin_address = str(f'{int_address:03b}')
        return bin_address

    #Function to create a random value
    def value_generator(self):
        int_value = randint(0, 65535)
        hex_value = str(f'{int_value:0x}')
        size = len(hex_value)
        while(size < 4):
            hex_value = "0" + hex_value
            size += 1
        return hex_value