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
    def change_state(self, processor, current_state, action, address, value):
        if current_state == "I":
            if action == "WRITE":
                print("Processor " + str(processor) + ": Write Miss")
                memory.write_to_cache(address, processor, value)
                print("Processor " + str(processor) + " State: Changing from I to M")
                memory.change_cache_block_state(processor, address)

                
                