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
        self.p0_cache = [["I", "XXX", "0000"], ["I", "XXX", "0000"], ["I", "XXX", "0000"], ["I", "XXX", "0000"]]
        self.p1_cache = [["I", "XXX", "0000"], ["I", "XXX", "0000"], ["I", "XXX", "0000"], ["I", "XXX", "0000"]]
        self.p2_cache = [["I", "XXX", "0000"], ["I", "XXX", "0000"], ["I", "XXX", "0000"], ["I", "XXX", "0000"]]
        self.p3_cache = [["I", "XXX", "0000"], ["I", "XXX", "0000"], ["I", "XXX", "0000"], ["I", "XXX", "0000"]]

    def read_from_memory(self, address):
        address_index = int(address, 2)
        return self.main_memory[address_index][1]

    def write_to_memory(self, address, value):
        address_index = int(address, 2)
        self.main_memory[address_index][1] = value

    def write_to_cache(self, mem_address, cache_num, value):
        cache_index = self.get_cache_index(mem_address)
        if cache_num == 0:
            print("Writing " + str(value) + " in address " + str(mem_address) + " at P" + str(cache_num) + ":B" + str(cache_index))
            self.p0_cache[cache_index][1] = mem_address
            self.p0_cache[cache_index][2] = value
            self.modify_watchers_write(cache_num, mem_address)
        if cache_num == 1:
            print("Writing " + str(value) + " in address " + str(mem_address) + " at P" + str(cache_num) + ":B" + str(cache_index))
            self.p1_cache[cache_index][1] = mem_address
            self.p1_cache[cache_index][2] = value
            self.modify_watchers_write(cache_num, mem_address)
        if cache_num == 2:
            print("Writing " + str(value) + " in address " + str(mem_address) + " at P" + str(cache_num) + ":B" + str(cache_index))
            self.p2_cache[cache_index][1] = mem_address
            self.p2_cache[cache_index][2] = value
            self.modify_watchers_write(cache_num, mem_address)
        if cache_num == 3:
            print("Writing " + str(value) + " in address " + str(mem_address) + " at P" + str(cache_num) + ":B" + str(cache_index))
            self.p3_cache[cache_index][1] = mem_address
            self.p3_cache[cache_index][2] = value
            self.modify_watchers_write(cache_num, mem_address)
    
    #Function to read an address from other cache in case of read miss
    #If address can't be found in caches, it will read from memory
    def read_from_other_cache(self, processor, address):
        if processor == 0:
            for i in self.p1_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P1")
                    self.modify_watchers_read(address)
                    return i[2]
            for i in self.p2_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P2")
                    self.modify_watchers_read(address)
                    return i[2]
            for i in self.p3_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P3")
                    self.modify_watchers_read(address)
                    return i[2]
            print("Address " + str(address) + " not nound on any cache. Retrieving value from memory")
            return self.read_from_memory(address)
        if processor == 1:
            for i in self.p0_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P0")
                    self.modify_watchers_read(address)
                    return i[2]
            for i in self.p2_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P2")
                    self.modify_watchers_read(address)
                    return i[2]
            for i in self.p3_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P3")
                    self.modify_watchers_read(address)
                    return i[2]
            print("Address " + str(address) + " not nound on any cache. Retrieving value from memory")
            return self.read_from_memory(address)
        if processor == 2:
            for i in self.p0_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P0")
                    self.modify_watchers_read(address)
                    return i[2]
            for i in self.p1_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P1")
                    self.modify_watchers_read(address)
                    return i[2]
            for i in self.p3_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P3")
                    self.modify_watchers_read(address)
                    return i[2]
            print("Address " + str(address) + " not nound on any cache. Retrieving value from memory")
            return self.read_from_memory(address)
        if processor == 3:
            for i in self.p0_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P0")
                    self.modify_watchers_read(address)
                    return i[2]
            for i in self.p1_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P1")
                    self.modify_watchers_read(address)
                    return i[2]
            for i in self.p2_cache:
                if i[1] == address:
                    print("Address " + str(address) + " found on cache from P2")
                    self.modify_watchers_read(address)
                    return i[2]
            print("Address " + str(address) + " not nound on any cache. Retrieving value from memory")
            return self.read_from_memory(address)
    
    #Function to get the actual state of a cache block
    def get_cache_block_state(self, processor, block):
        if processor == 0:
            return self.p0_cache[block][0]
        if processor == 1:
            return self.p1_cache[block][0]
        if processor == 2:
            return self.p2_cache[block][0]
        if processor == 3:
            return self.p3_cache[block][0]

    #Function to modify the state of blocks when an addressis being read in another cache
    def modify_watchers_read(self, processor, address):
        #processor: cache where the address is taken
        #address: address to check
        #state: state of the block being read
        if processor == 0:
            block = 0
            for i in self.p1_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + str(address))
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1
            block = 0
            for i in self.p2_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1
            block = 0
            for i in self.p3_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1
        if processor == 1:
            block = 0
            for i in self.p0_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + str(address))
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1
            block = 0
            for i in self.p2_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1
            block = 0
            for i in self.p3_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1
        if processor == 2:
            block = 0
            for i in self.p0_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1
            block = 0
            for i in self.p1_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1
            block = 0
            for i in self.p3_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1
        if processor == 3:
            block = 0
            for i in self.p0_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1
            block = 0
            for i in self.p1_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1
            block = 0
            for i in self.p2_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to S")
                        self.change_cache_block_state(processor, address, "S")
                block = block + 1

    #Function to modify the state of blocks when an addressis being written in another cache
    def modify_watchers_write(self, processor, address):
        #processor: cache where the address is taken
        #address: address to check
        #state: state of the block being written
        if processor == 0:
            block = 0
            for i in self.p1_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "S":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")

                block = block + 1
            block = 0
            for i in self.p2_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                block = block + 1
            block = 0
            for i in self.p3_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                block = block + 1
        if processor == 1:
            block = 0
            for i in self.p0_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                block = block + 1
            block = 0
            for i in self.p2_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                block = block + 1
            block = 0
            for i in self.p3_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                block = block + 1
        if processor == 2:
            block = 0
            for i in self.p0_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                block = block + 1
            block = 0
            for i in self.p1_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                block = block + 1
            block = 0
            for i in self.p3_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                block = block + 1
        if processor == 3:
            block = 0
            for i in self.p0_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                block = block + 1
            block = 0
            for i in self.p1_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                block = block + 1
            block = 0
            for i in self.p2_cache:
                if i[1] == address:
                    if i[0] == "M":
                        print("Write-back on Address " + address)
                        self.write_to_memory(address, i[2])
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                    if i[0] == "E":
                        print("P" + str(processor) + ": B" + str(block) + " Changed to I")
                        self.change_cache_block_state(processor, address, "I")
                block = block + 1
    
    #Function to change the state of a block in a cache
    def change_cache_block_state(self, processor, address, new_state):
        if processor == 0:
            for i in self.p0_cache:
                if (i[1] == address):
                    i[0] = new_state
        if processor == 1:
            for i in self.p1_cache:
                if (i[1] == address):
                    i[0] = new_state
        if processor == 2:
            for i in self.p2_cache:
                if (i[1] == address):
                    i[0] = new_state
        if processor == 3:
            for i in self.p3_cache:
                if (i[1] == address):
                    i[0] = new_state

    #Function to get cache index based on the one-way associativity
    def get_cache_index(self, mem_address):
        if (mem_address == "000") or (mem_address == "100"):
            return 0
        if (mem_address == "001") or (mem_address == "101"):
                return 1
        if (mem_address == "010") or (mem_address == "110"):
            return 2
        if (mem_address == "011") or (mem_address == "111"):
            return 3

    #Function to check data exclusivity in caches
    def check_exclusivity(self, processor, address):
        if processor == 0:
            for i in self.p1_cache:
                if i[1] == address:
                    return False
            for i in self.p2_cache:
                if i[1] == address:
                    return False
            for i in self.p3_cache:
                if i[1] == address:
                    return False
            return True
        if processor == 1:
            for i in self.p0_cache:
                if i[1] == address:
                    return False
            for i in self.p2_cache:
                if i[1] == address:
                    return False
            for i in self.p3_cache:
                if i[1] == address:
                    return False
            return True
        if processor == 2:
            for i in self.p0_cache:
                if i[1] == address:
                    return False
            for i in self.p1_cache:
                if i[1] == address:
                    return False
            for i in self.p3_cache:
                if i[1] == address:
                    return False
            return True
        if processor == 3:
            for i in self.p0_cache:
                if i[1] == address:
                    return False
            for i in self.p1_cache:
                if i[1] == address:
                    return False
            for i in self.p2_cache:
                if i[1] == address:
                    return False
            return True

    #Function to check if a address is in cache
    def is_address_in_cache(self, processor, address):
        if processor == 0:
            for i in self.p0_cache:
                if i[1] == address:
                    return True
            return False
        if processor == 1:
            for i in self.p1_cache:
                if i[1] == address:
                    return True
            return False
        if processor == 2:
            for i in self.p2_cache:
                if i[1] == address:
                    return True
            return False
        if processor == 3:
            for i in self.p3_cache:
                if i[1] == address:
                    return True
            return False

    #Function to check if a value in memory is the latest
    def is_latest_value_in_memory(self, address, value):
        mem_value = self.read_from_memory(address)
        if mem_value == value:
            return True
        else:
            return False
    
    #Function to print the memory
    def print_memory(self):
        print("--------------------------------------------------------------MEMORY--------------------------------------------------------------------")
        print(self.main_memory)
        print("----------------------------------------------------------------------------------------------------------------------------------------")

    #Function to print the caches
    def print_cache(self):
        print("--------------------------------------------------------------CACHE 0-------------------------------------------------------------------")
        print(self.p0_cache)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------CACHE 1-------------------------------------------------------------------")
        print(self.p1_cache)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------CACHE 2-------------------------------------------------------------------")
        print(self.p2_cache)
        print("----------------------------------------------------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------CACHE 3-------------------------------------------------------------------")
        print(self.p3_cache)
        print("----------------------------------------------------------------------------------------------------------------------------------------")