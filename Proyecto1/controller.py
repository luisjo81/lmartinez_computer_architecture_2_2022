import Memory
import Processor
import Gui

import threading
import time

class Controller:
    def __init__(self):
        self.wait_time = 3
        memory = Memory()

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
    def change_state(self, processor, block, current_state, address, value, action):
        if current_state == "M":
            if action == "READ":
                if memory.is_address_in_cache(processor, address) == True:
                    print("P" + processor + " Cache Read Hit")
                    #DISPLAY IN GUI
                else:
                    print("P" + processor + " Cache Read Miss")
                    read_value = memory.read_from_other_cache(processor, address)
                    #DISPLAY IN GUI
            if action == "WRITE":
                print("P" + processor + " Cache Write Hit")
                memory.write_to_cache(address, processor, value)

        if current_state == "E":
            if action == "READ":
                print("P" + processor + " Cache Read Hit")
            if action == "WRITE":
                print("P" + processor + " Cache Write Hit")
                memory.write_to_cache(address, processor, value)
                print("P" + processor + ": B" + block + " Changed to M")
                memory.change_cache_block_state(processor, address, "M")

        if current_state == "S":
            if action == "READ":
                if memory.is_address_in_cache(processor, address) == True:
                    print("P" + processor + " Cache Read Hit")
                else:
                    print("P" + processor + " Cache Read Miss")
            if action == "WRITE":
                print("P" + processor + " Cache Write Hit")
                memory.write_to_cache(address, processor, value)
                print("P" + processor + ": B" + block + " Changed to M")
                memory.change_cache_block_state(processor, address, "M")

        if current_state == "I":
            if action == "READ":
                if memory.is_address_in_cache(processor, address) == False:
                    print("P" + processor + " Cache Read Miss")
                    read_value = memory.read_from_other_cache(processor, address)
                    if memory.is_latest_value_in_memory(address, read_value) == True:
                        print("P" + processor + ": B" + block + " Changed to E")
                        memory.change_cache_block_state(processor, address, "E")
                    else:
                        print("P" + processor + ": B" + block + " Changed to S")
                        memory.change_cache_block_state(processor, address, "S")
            if action == "WRITE":
                print("P" + processor + " Cache Write Hit")
                memory.write_to_cache(address, processor, value)
                print("P" + processor + ": B" + block + " Changed to M")
                memory.change_cache_block_state(processor, address, "M")

    #Function to separete the elements from an instruction
    def separate_instruction(self, instruction):
        # [processor, operation, address, value]
        instruction_parts = []
        instruction_parts = instruction_parts + [instruction[1]]
        if instruction[4] == "C":
            instruction_parts = instruction_parts + ["CALC"]
            return instruction_parts
        if instruction[4] == "R":
            instruction_parts = instruction_parts + ["READ"] + [instruction[9:]]
            return instruction_parts
        if instruction[4] == "W":
            instruction_parts = instruction_parts + ["WRITE"] + [instruction[10:13]] + [instruction[14:]]
            return instruction_parts