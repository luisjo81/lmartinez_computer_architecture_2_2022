from memory import Memory
from processor import Processor
#import Gui

import threading
import time

class Controller:
    def __init__(self):
        self.wait_time = 3
        self.mem = Memory()
        self.proce = Processor(0)
    """
    def threads_manager(self):
        p0_thread = threading.Thread(target = processor, args = ())
        p1_thread = threading.Thread(target = processor, args = ())
        p2_thread = threading.Thread(target = processor, args = ())
        p3_thread = threading.Thread(target = processor, args = ())
        
        while(True):
            p0_thread.start()  
            p1_thread.start() 
            p2_thread.start() 
            p3_thread.start()
    """

    #Function to change state in cache block
    def change_state(self, processor, current_state, address, value, action):
        block = self.mem.get_cache_index(address)
        if current_state == "M":
            if action == "READ":
                if self.mem.is_address_in_cache(processor, address) == True:
                    print("P" + str(processor) + " Cache Read Hit")
                    #DISPLAY IN GUI
                else:
                    print("P" + str(processor) + " Cache Read Miss")
                    read_value = self.mem.read_from_other_cache(processor, address)
                    #DISPLAY IN GUI
            if action == "WRITE":
                print("P" + str(processor) + " Cache Write Hit")
                self.mem.write_to_cache(address, processor, value)

        if current_state == "E":
            if action == "READ":
                print("P" + str(processor) + " Cache Read Hit")
            if action == "WRITE":
                print("P" + str(processor) + " Cache Write Hit")
                self.mem.write_to_cache(address, processor, value)
                print("P" + str(processor) + ":B" + str(block) + " Changed to M")
                self.mem.change_cache_block_state(processor, address, "M")

        if current_state == "S":
            if action == "READ":
                if self.mem.is_address_in_cache(processor, address) == True:
                    print("P" + str(processor) + " Cache Read Hit")
                else:
                    print("P" + str(processor) + " Cache Read Miss")
            if action == "WRITE":
                print("P" + str(processor) + " Cache Write Hit")
                self.mem.write_to_cache(address, processor, value)
                print("P" + str(processor) + ":B" + str(block) + " Changed to M")
                self.mem.change_cache_block_state(processor, address, "M")

        if current_state == "I":
            if action == "READ":
                if self.mem.is_address_in_cache(processor, address) == False:
                    print("P" + str(processor) + " Cache Read Miss")
                    read_value = self.mem.read_from_other_cache(processor, address)
                    if self.mem.is_latest_value_in_memory(address, read_value) == True:
                        print("P" + str(processor) + ":B" + str(block) + " Changed to E")
                        self.mem.change_cache_block_state(processor, address, "E")
                    else:
                        print("P" + str(processor) + ":B" + str(block) + " Changed to S")
                        self.mem.change_cache_block_state(processor, address, "S")
            if action == "WRITE":
                print("P" + str(processor) + " Cache Write Hit")
                self.mem.write_to_cache(address, processor, value)
                print("P" + str(processor) + ":B" + str(block) + " Changed to M")
                self.mem.change_cache_block_state(processor, address, "M")

    #Function to separete the elements from an instruction
    def separate_instruction(self, instruction):
        # [processor, operation, address, value]
        instruction_parts = []
        instruction_parts = instruction_parts + [instruction[1]]
        if instruction[4] == "C":
            instruction_parts = instruction_parts + ["CALC"] + [""] + [""]
            return instruction_parts
        if instruction[4] == "R":
            instruction_parts = instruction_parts + ["READ"] + [instruction[9:]] + [""]
            return instruction_parts
        if instruction[4] == "W":
            instruction_parts = instruction_parts + ["WRITE"] + [instruction[10:13]] + [instruction[14:]]
            return instruction_parts
    
cont = Controller()
instruction = cont.proce.instruction_generator()
print("Instrucción: " + instruction)
instruction_list = cont.separate_instruction(instruction)
print(instruction_list)
instruction_processor = instruction_list[0]
if instruction_list[1] != "CALC": 
    instruction_state = cont.mem.get_cache_block_state(int(instruction_processor), cont.mem.get_cache_index(instruction_list[2]))
    instruction_operation = instruction_list[1]
    instruction_address = instruction_list[2]
    instruction_value = instruction_list[3]

    cont.change_state(int(instruction_processor), instruction_state, instruction_address, instruction_value, instruction_operation)
    cont.mem.print_cache()
    cont.mem.print_memory()

#print("Instrucción P0: WRITE 010;ABCD")
#cont.change_state(0, "I", "010", "ABCD", "WRITE")
#cont.mem.print_cache()
#cont.mem.print_memory()

#print("Instrucción P2: WRITE 111;01EC")
#cont.change_state(2, "I", "111", "01EC", "WRITE")
#cont.mem.print_cache()
#cont.mem.print_memory()

#print("Instrucción P1: WRITE 000;1010")
#cont.change_state(1, "I", "000", "1010", "WRITE")
#cont.mem.print_cache()
#cont.mem.print_memory()

#print("Instrucción P3: WRITE 000;CDEF")
#cont.change_state(3, "I", "000", "CDEF", "WRITE")
#cont.mem.print_cache()
#cont.mem.print_memory()

#print("Instrucción P2: READ 111")
#cont.change_state(2, "M", "111", "", "READ")
#cont.mem.print_cache()
#cont.mem.print_memory()