class Memory:
    def __init__(self):
        """
            Main Memory = [[B0 address, B0 value],
                           [B1 address, B1 value],
                           [B2 address, B2 value],
                           [B3 address, B3 value],
                           [B4 address, B4 value],
                           [B5 address, B5 value],
                           [B6 address, B6 value],
                           [B7 address, B7 value]]
        """
        self.main_memory = [['000','0000'], ['001', '0000'], ['010', '0000'], ['011', '0000'], ['100', '0000'], ['101', '0000'], ['110', '0000'], ['111', '0000']] 

        """ 
            Processor Cache = [[B0 state, B0 address, B0 value],
                               [B1 state, B1 address, B1 value],
                               [B2 state, B2 address, B2 value],
                               [B3 state, B3 address, B3 value]]
        """
        self.p0_Cache = [['I', '0000', '0000'], ['I', '0000', '0000'], ['I', '0000', '0000'], ['I', '0000', '0000']]
        self.p1_Cache = [['I', '0000', '0000'], ['I', '0000', '0000'], ['I', '0000', '0000'], ['I', '0000', '0000']]
        self.p2_Cache = [['I', '0000', '0000'], ['I', '0000', '0000'], ['I', '0000', '0000'], ['I', '0000', '0000']]
        self.p3_Cache = [['I', '0000', '0000'], ['I', '0000', '0000'], ['I', '0000', '0000'], ['I', '0000', '0000']]

    def read_from_cache(self):
        pass

    def read_from_memory(self):
        pass

    def write_to_memory(self):
        pass

    """
        Function for transitioning between states
        params
            - cache: int (0, 1, 2, 3)
            - block: int (0, 1, 2, 3)
            - action: string ("read", "write", "see")
    """  
    def state_machine(self, cache, block, action):
        
        #Variables
        actual_state = ''
        new_state = ''

        #Getting the actual state of the cache block
        if cache == 0:
            actual_state = self.p0_Cache[block][0]
        if cache == 1:
            actual_state = self.p1_Cache[block][0]
        if cache == 2:
            actual_state = self.p2_Cache[block][0]
        if cache == 3:
            actual_state = self.p3_Cache[block][0]
        
        #Changing state based on the action
    

o = Memory()
o.state_machine(0, 1, 0)
