import threading
import time

class Controller:
    def __init__(self):
        self.wait_time = 3

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
