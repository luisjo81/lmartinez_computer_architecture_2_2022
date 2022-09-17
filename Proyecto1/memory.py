class Memory:
    def __init__(self):
        """
            Main Memory = [[000 address, 000 value],
                           [001 address, 001 value],
                           [010 address, 010 value],
                           [011 address, 011 value],
                           [100 address, 100 value],
                           [101 address, 101 value],
                           [110 address, 110 value],
                           [111 address, 111 value]]
        """
        self.main_memory = [["000","0000"], ["001", "0000"], ["010", "0000"], ["011", "0000"], ["100", "0000"], ["101", "0000"], ["110", "0000"], ["111", "0000"]] 

        """ 
            Processor Cache = [[B0 state, B0 address, B0 value, B0 valid bit],
                               [B1 state, B1 address, B1 value, B1 valid bit],
                               [B2 state, B2 address, B2 value, B2 valid bit],
                               [B3 state, B3 address, B3 value, B3 valid bit]]
        """
        self.p0_Cache = [["I", "000", "0000", "0"], ["I", "000", "0000", "0"], ["I", "000", "0000", "0"], ["I", "000", "0000", "0"]]
        self.p1_Cache = [["I", "000", "0000", "0"], ["I", "000", "0000", "0"], ["I", "000", "0000", "0"], ["I", "000", "0000", "0"]]
        self.p2_Cache = [["I", "000", "0000", "0"], ["I", "000", "0000", "0"], ["I", "000", "0000", "0"], ["I", "000", "0000", "0"]]
        self.p3_Cache = [["I", "000", "0000", "0"], ["I", "000", "0000", "0"], ["I", "000", "0000", "0"], ["I", "000", "0000", "0"]]

    def read_from_memory(self, address):
        address_index = int(address, 2)
        return self.main_memory[address_index][1]

    def write_to_memory(self, address, value):
        address_index = int(address, 2)
        self.main_memory[address_index][1] = value

    def write_to_cache(self, mem_address, cache_num, value):
        cache_index = self.get_cache_index(mem_address)
        if cache_num == 0:
            self.p0_Cache[cache_index][1] = mem_address
            self.p0_Cache[cache_index][2] = value
        if cache_num == 1:
            self.p1_Cache[cache_index][1] = mem_address
            self.p1_Cache[cache_index][2] = value
        if cache_num == 2:
            self.p2_Cache[cache_index][1] = mem_address
            self.p2_Cache[cache_index][2] = value
        if cache_num == 3:
            self.p3_Cache[cache_index][1] = mem_address
            self.p3_Cache[cache_index][2] = value

    #Function to get cache index based on the one-way associativity
    def get_cache_index(mem_address):
        if (mem_address == "000") or (mem_address == "100"):
            return 0
        if (mem_address == "001") or (mem_address == "101"):
                return 1
        if (mem_address == "010") or (mem_address == "110"):
            return 2
        if (mem_address == "011") or (mem_address == "111"):
            return 3