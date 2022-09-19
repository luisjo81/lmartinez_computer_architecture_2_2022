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
                else:
                    print("P" + processor + " Cache Read Miss")
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

        if current_state == "I":
            if action == "READ":
                if memory.is_address_in_cache(processor, address) == False:
                     print("P" + processor + " Cache Read Miss")

    def update_watchers(self, processor, )