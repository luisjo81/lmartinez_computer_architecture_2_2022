from ctypes import alignment
from threading import Thread, Lock
import time
import tkinter as tk
import tkinter.font as font
from memory import Memory
from processor import Processor

class Controller:
    def __init__(self):
        self.wait_time = 3
        self.memory_delay = 2
        self.mem = Memory()
        self.proce0 = Processor(0)
        self.proce1 = Processor(1)
        self.proce2 = Processor(2)
        self.proce3 = Processor(3)
        self.lock = Lock()
       
        while True:
            window.update()

            self.p0_thread = Thread(target = self.execute, args = (0,))
            self.p1_thread = Thread(target = self.execute, args = (1,))
            self.p2_thread = Thread(target = self.execute, args = (2,))
            self.p3_thread = Thread(target = self.execute, args = (3,))

            self.p0_thread.start()  
            self.p1_thread.start() 
            self.p2_thread.start() 
            self.p3_thread.start()

            self.p0_thread.join()
            self.p1_thread.join() 
            self.p2_thread.join() 
            self.p3_thread.join()   

            #-----------------------------GUI UPDATES-----------------------------#
            #Memory Space 0
            mem0_block = "000: 0x" + self.mem.read_from_memory("000")
            global mem0_label
            mem0_label = tk.Label(window, text = mem0_block, width = 17, height = 2)
            mem0_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            mem0_label.place(x = 510, y = 20)

            #Memory Space 1
            mem1_block = "001: 0x" + self.mem.read_from_memory("001")
            global mem1_label
            mem1_label = tk.Label(window, text = mem1_block, width = 17, height = 2)
            mem1_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            mem1_label.place(x = 510, y = 110)

            #Memory Space 2
            mem2_block = "010: 0x" + self.mem.read_from_memory("010")
            global mem2_label
            mem2_label = tk.Label(window, text = mem2_block, width = 17, height = 2)
            mem2_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            mem2_label.place(x = 510, y = 200)

            #Memory Space 3
            mem3_block = "011: 0x" + self.mem.read_from_memory("011")
            global mem3_label
            mem3_label = tk.Label(window, text = mem3_block, width = 17, height = 2)
            mem3_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            mem3_label.place(x = 510, y = 290)

            #Memory Space 4
            mem4_block = "100: 0x" + self.mem.read_from_memory("100")
            global mem4_label
            mem4_label = tk.Label(window, text = mem4_block, width = 17, height = 2)
            mem4_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            mem4_label.place(x = 510, y = 380)

            #Memory Space 5
            mem5_block = "101: 0x" + self.mem.read_from_memory("101")
            global mem5_label
            mem5_label = tk.Label(window, text = mem5_block, width = 17, height = 2)
            mem5_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            mem5_label.place(x = 510, y = 470)

            #Memory Space 6
            mem6_block = "110: 0x" + self.mem.read_from_memory("110")
            global mem6_label
            mem6_label = tk.Label(window, text = mem6_block, width = 17, height = 2)
            mem6_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            mem6_label.place(x = 510, y = 560)

            #Memory Space 7
            mem7_block = "111: 0x" + self.mem.read_from_memory("111")
            global mem7_label
            mem7_label = tk.Label(window, text = mem7_block, width = 17, height = 2)
            mem7_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            mem7_label.place(x = 510, y = 650)

            #Processor 0 Cache Space 0
            p0_cache0_block = "B0: " + self.mem.p0_cache[0][0]+ " " + self.mem.p0_cache[0][1] + " 0x" + self.mem.p0_cache[0][2]
            global p0_cache0
            p0_cache0 = tk.Label(window, text = p0_cache0_block, width = 15, height = 1)
            p0_cache0.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p0_cache0.place(x = 840, y = 140)

            #Processor 0 Cache Space 1
            p0_cache1_block = "B1: " + self.mem.p0_cache[1][0]+ " " + self.mem.p0_cache[1][1] + " 0x" + self.mem.p0_cache[1][2]
            global p0_cache1
            p0_cache1 = tk.Label(window, text = p0_cache1_block, width = 15, height = 1)
            p0_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p0_cache1.place(x = 840, y = 190)

            #Processor 0 Cache Space 2
            p0_cache2_block = "B2: " + self.mem.p0_cache[2][0]+ " " + self.mem.p0_cache[2][1] + " 0x" + self.mem.p0_cache[2][2]
            global p0_cache2
            p0_cache2 = tk.Label(window, text = p0_cache2_block, width = 15, height = 1)
            p0_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p0_cache2.place(x = 840, y = 240)

            #Processor 0 Cache Space 3
            p0_cache3_block = "B3: " + self.mem.p0_cache[3][0]+ " " + self.mem.p0_cache[3][1] + " 0x" + self.mem.p0_cache[3][2]
            global p0_cache3
            p0_cache3 = tk.Label(window, text = p0_cache3_block, width = 15, height = 1)
            p0_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p0_cache3.place(x = 840, y = 290)

            #Processor 1 Cache Space 0
            p1_cache0_block = "B0: " + self.mem.p1_cache[0][0]+ " " + self.mem.p1_cache[0][1] + " 0x" + self.mem.p1_cache[0][2]
            global p1_cache0
            p1_cache0 = tk.Label(window, text = p1_cache0_block, width = 15, height = 1)
            p1_cache0.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p1_cache0.place(x = 1132, y = 140)

            #Processor 1 Cache Space 1
            p1_cache1_block = "B1: " + self.mem.p1_cache[1][0]+ " " + self.mem.p1_cache[1][1] + " 0x" + self.mem.p1_cache[1][2]
            global p1_cache1
            p1_cache1 = tk.Label(window, text = p1_cache1_block, width = 15, height = 1)
            p1_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p1_cache1.place(x = 1132, y = 190)

            #Processor 1 Cache Space 2
            p1_cache2_block = "B2: " + self.mem.p1_cache[2][0]+ " " + self.mem.p1_cache[2][1] + " 0x" + self.mem.p1_cache[2][2]
            global p1_cache2
            p1_cache2 = tk.Label(window, text = p1_cache2_block, width = 15, height = 1)
            p1_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p1_cache2.place(x = 1132, y = 240)

            #Processor 1 Cache Space 3
            p1_cache3_block = "B3: " + self.mem.p1_cache[3][0]+ " " + self.mem.p1_cache[3][1] + " 0x" + self.mem.p1_cache[3][2]
            global p1_cache3
            p1_cache3 = tk.Label(window, text = p1_cache3_block, width = 15, height = 1)
            p1_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p1_cache3.place(x = 1132, y = 290)

            #Processor 2 Cache Space 0
            p2_cache0_block = "B0: " + self.mem.p2_cache[0][0]+ " " + self.mem.p2_cache[0][1] + " 0x" + self.mem.p2_cache[0][2]
            global p2_cache0
            p2_cache0 = tk.Label(window, text = p2_cache0_block, width = 15, height = 1)
            p2_cache0.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p2_cache0.place(x = 840, y = 470)

            #Processor 2 Cache Space 1
            p2_cache1_block = "B1: " + self.mem.p2_cache[1][0]+ " " + self.mem.p2_cache[1][1] + " 0x" + self.mem.p2_cache[1][2]
            global p2_cache1
            p2_cache1 = tk.Label(window, text = p2_cache1_block, width = 15, height = 1)
            p2_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p2_cache1.place(x = 840, y = 520)

            #Processor 2 Cache Space 2
            p2_cache2_block = "B2: " + self.mem.p2_cache[2][0]+ " " + self.mem.p2_cache[2][1] + " 0x" + self.mem.p2_cache[2][2]
            global p2_cache2
            p2_cache2 = tk.Label(window, text = p2_cache2_block, width = 15, height = 1)
            p2_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p2_cache2.place(x = 840, y = 570)

            #Processor 2 Cache Space 3
            p2_cache3_block = "B3: " + self.mem.p2_cache[3][0]+ " " + self.mem.p2_cache[3][1] + " 0x" + self.mem.p2_cache[3][2]
            global p2_cache3
            p2_cache3 = tk.Label(window, text = p2_cache3_block, width = 15, height = 1)
            p2_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p2_cache3.place(x = 840, y = 620)

            #Processor 3 Cache Space 0
            p3_cache0_block = "B0: " + self.mem.p3_cache[0][0]+ " " + self.mem.p3_cache[0][1] + " 0x" + self.mem.p3_cache[0][2]
            global p3_cache0
            p3_cache0 = tk.Label(window, text = p3_cache0_block, width = 15, height = 1)
            p3_cache0.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p3_cache0.place(x = 1132, y = 470)

            #Processor 3 Cache Space 1
            p3_cache1_block = "B1: " + self.mem.p3_cache[1][0]+ " " + self.mem.p3_cache[1][1] + " 0x" + self.mem.p3_cache[1][2]
            global p3_cache1
            p3_cache1 = tk.Label(window, text = p3_cache1_block, width = 15, height = 1)
            p3_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p3_cache1.place(x = 1132, y = 520)

            #Processor 3 Cache Space 2
            p3_cache2_block = "B2: " + self.mem.p3_cache[2][0]+ " " + self.mem.p3_cache[2][1] + " 0x" + self.mem.p3_cache[2][2]
            global p3_cache2
            p3_cache2 = tk.Label(window, text = p3_cache2_block, width = 15, height = 1)
            p3_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p3_cache2.place(x = 1132, y = 570)

            #Processor 3 Cache Space 3
            p3_cache3_block = "B3: " + self.mem.p3_cache[3][0]+ " " + self.mem.p3_cache[3][1] + " 0x" + self.mem.p3_cache[3][2]
            global p3_cache3
            p3_cache3 = tk.Label(window, text = p3_cache3_block, width = 15, height = 1)
            p3_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
            p3_cache3.place(x = 1132, y = 620)

            #Instructions
            global p0_instruction, p1_instruction, p2_instruction, p3_instruction
            global instruction, instructionP0, instructionP1, instructionP2, instructionP3
            p0_instruction = tk.Label(window, text = instructionP0, width = 25, height = 1, justify = tk.LEFT)
            p0_instruction.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
            p0_instruction.place(x = 30, y = 80)
            p1_instruction = tk.Label(window, text = instructionP1, width = 25, height = 1, justify = tk.LEFT)
            p1_instruction.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
            p1_instruction.place(x = 30, y = 100)
            p2_instruction = tk.Label(window, text = instructionP2, width = 25, height = 1, justify = tk.LEFT)
            p2_instruction.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
            p2_instruction.place(x = 30, y = 120)
            p3_instruction = tk.Label(window, text = instructionP3, width = 25, height = 1, justify = tk.LEFT)
            p3_instruction.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
            p3_instruction.place(x = 30, y = 140)

            #Alerts
            global alert0, alert1, alert2, alert3
            global alert_p0, alert_p1, alert_p2, alert_p3
            alert_p0 = tk.Label(window, text = "P0: " + alert0, width = 25, height = 1, justify = tk.LEFT)
            alert_p0.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
            alert_p0.place(x = 30, y = 200)
            alert_p1 = tk.Label(window, text = "P1: " + alert1, width = 25, height = 1, justify = tk.LEFT)
            alert_p1.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
            alert_p1.place(x = 30, y = 220)
            alert_p2 = tk.Label(window, text = "P2: " + alert2, width = 25, height = 1, justify = tk.LEFT)
            alert_p2.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
            alert_p2.place(x = 30, y = 240)
            alert_p3 = tk.Label(window, text = "P3: " + alert3, width = 25, height = 1, justify = tk.LEFT)
            alert_p3.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
            alert_p3.place(x = 30, y = 260)
        
    #Function to execute an instruction
    def execute(self, processor):
        self.lock.acquire()
        global instruction, instructionP0, instructionP1, instructionP2, instructionP3
        if processor == 0:
            instruction = self.proce0.instruction_generator()
            instructionP0 = instruction
        if processor == 1:
            instruction = self.proce1.instruction_generator()
            instructionP1 = instruction
        if processor == 2:
            instruction = self.proce2.instruction_generator()
            instructionP2 = instruction
        if processor == 3:
            instruction = self.proce3.instruction_generator()
            instructionP3 = instruction
        print("Instruction generated ---> " + instruction)
        instruction_list = self.separate_instruction(instruction)
        print(instruction_list)
        instruction_processor = instruction_list[0]
        if instruction_list[1] != "CALC": 
            instruction_state = self.mem.get_cache_block_state(int(instruction_processor), self.mem.get_cache_index(instruction_list[2]))
            instruction_operation = instruction_list[1]
            instruction_address = instruction_list[2]
            instruction_value = instruction_list[3]
            self.change_state(int(instruction_processor), instruction_state, instruction_address, instruction_value, instruction_operation)
            self.mem.print_cache()
            self.mem.print_memory()
        else:
            print("CALC Executed")
        
        self.lock.release()
        time.sleep(3)

    #Function to change state in cache block
    def change_state(self, processor, current_state, address, value, action):
        global alert0, alert1, alert2, alert3
        block = self.mem.get_cache_index(address)
               
        if current_state == "M":
            if action == "READ":
                if self.mem.is_address_in_cache(processor, address) == True:
                    print("P" + str(processor) + " Cache Read Hit")
                    if processor == 0:
                        alert0 = " Cache Read Hit"
                    if processor == 1:
                        alert1 = " Cache Read Hit"
                    if processor == 2:
                        alert2 = " Cache Read Hit"
                    if processor == 3:
                        alert3 = " Cache Read Hit"
                else:
                    print("P" + str(processor) + " Cache Read Miss")
                    if processor == 0:
                        alert0 = " Cache Read Miss"
                    if processor == 1:
                        alert1 = " Cache Read Miss"
                    if processor == 2:
                        alert2 = " Cache Read Miss"
                    if processor == 3:
                        alert3 = " Cache Read Miss"
                    read_value = self.mem.read_from_other_cache(processor, address)
                    
            if action == "WRITE":
                print("P" + str(processor) + " Cache Write Hit")
                if processor == 0:
                    alert0 = " Cache Write Hit"
                if processor == 1:
                    alert1 = " Cache Write Hit"
                if processor == 2:
                    alert2 = " Cache Write Hit"
                if processor == 3:
                    alert3 = " Cache Write Hit"
                self.mem.write_to_cache(address, processor, value)

        if current_state == "E":
            if action == "READ":
                print("P" + str(processor) + " Cache Read Hit")
                if processor == 0:
                    alert0 = " Cache Read Hit"
                if processor == 1:
                    alert1 = " Cache Read Hit"
                if processor == 2:
                    alert2 = " Cache Read Hit"
                if processor == 3:
                    alert3 = " Cache Read Hit"
            if action == "WRITE":
                print("P" + str(processor) + " Cache Write Hit")
                if processor == 0:
                    alert0 = " Cache Write Hit"
                if processor == 1:
                    alert1 = " Cache Write Hit"
                if processor == 2:
                    alert2 = " Cache Write Hit"
                if processor == 3:
                    alert3 = " Cache Write Hit"
                self.mem.write_to_cache(address, processor, value)
                print("P" + str(processor) + ":B" + str(block) + " Changed to M")
                self.mem.change_cache_block_state(processor, address, "M")

        if current_state == "S":
            if action == "READ":
                if self.mem.is_address_in_cache(processor, address) == True:
                    print("P" + str(processor) + " Cache Read Hit")
                    if processor == 0:
                        alert0 = " Cache Read Hit"
                    if processor == 1:
                        alert1 = " Cache Read Hit"
                    if processor == 2:
                        alert2 = " Cache Read Hit"
                    if processor == 3:
                        alert3 = " Cache Read Hit"
                else:
                    print("P" + str(processor) + " Cache Read Miss")
                    if processor == 0:
                        alert0 = " Cache Read Miss"
                    if processor == 1:
                        alert1 = " Cache Read Miss"
                    if processor == 2:
                        alert2 = " Cache Read Miss"
                    if processor == 3:
                        alert3 = " Cache Read Miss"
            if action == "WRITE":
                print("P" + str(processor) + " Cache Write Hit")
                if processor == 0:
                    alert0 = " Cache Write Hit"
                if processor == 1:
                    alert1 = " Cache Write Hit"
                if processor == 2:
                    alert2 = " Cache Write Hit"
                if processor == 3:
                    alert3 = " Cache Write Hit"
                self.mem.write_to_cache(address, processor, value)
                print("P" + str(processor) + ":B" + str(block) + " Changed to M")
                self.mem.change_cache_block_state(processor, address, "M")

        if current_state == "I":
            if action == "READ":
                if self.mem.is_address_in_cache(processor, address) == False:
                    print("P" + str(processor) + " Cache Read Miss")
                    if processor == 0:
                        alert0 = " Cache Read Miss"
                    if processor == 1:
                        alert1 = " Cache Read Miss"
                    if processor == 2:
                        alert2 = " Cache Read Miss"
                    if processor == 3:
                        alert3 = " Cache Read Miss"
                    read_value = self.mem.read_from_other_cache(processor, address)
                    if self.mem.is_latest_value_in_memory(address, read_value) == True:
                        print("P" + str(processor) + ":B" + str(block) + " Changed to E")
                        self.mem.change_cache_block_state(processor, address, "E")
                    else:
                        print("P" + str(processor) + ":B" + str(block) + " Changed to S")
                        self.mem.change_cache_block_state(processor, address, "S")
            if action == "WRITE":
                print("P" + str(processor) + " Cache Write Hit")
                if processor == 0:
                    alert0 = " Cache Write Hit"
                if processor == 1:
                    alert1 = " Cache Write Hit"
                if processor == 2:
                    alert2 = " Cache Write Hit"
                if processor == 3:
                    alert3 = " Cache Write Hit"
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

window = tk.Tk()
window.title("Visualizador")
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))
window.resizable(0, 0)
window.configure(bg = 'gray')   

#Information Area
info_area = tk.Canvas(window, width = 450, height = 600)
info_area.configure(bg = 'azure2')
info_area.place(x = 20, y = 20)

#Button Area
button_area = tk.Canvas(window, width = 450, height = 140)
button_area.configure(bg = 'black')
button_area.place(x = 20, y = 660)

#Memory Area
memory_area = tk.Canvas(window, width = 290, height = 690)
memory_area.configure(bg = 'medium orchid')
memory_area.place(x = 510, y = 20)

#Memory Space 0
mem0_label = tk.Label(window, text = "000: 0x0000", width = 17, height = 2)
mem0_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
mem0_label.place(x = 510, y = 20)

#Memory Space 1
mem1_label = tk.Label(window, text = "001: 0x0000", width = 17, height = 2)
mem1_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
mem1_label.place(x = 510, y = 110)

#Memory Space 2
mem2_label = tk.Label(window, text = "010: 0x0000", width = 17, height = 2)
mem2_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
mem2_label.place(x = 510, y = 200)

#Memory Space 3
mem3_label = tk.Label(window, text = "011: 0x0000", width = 17, height = 2)
mem3_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
mem3_label.place(x = 510, y = 290)

#Memory Space 4
mem4_label = tk.Label(window, text = "100: 0x0000", width = 17, height = 2)
mem4_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
mem4_label.place(x = 510, y = 380)

#Memory Space 5
mem5_label = tk.Label(window, text = "101: 0x0000", width = 17, height = 2)
mem5_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
mem5_label.place(x = 510, y = 470)

#Memory Space 6
mem6_label = tk.Label(window, text = "110: 0x0000", width = 17, height = 2)
mem6_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
mem6_label.place(x = 510, y = 560)

#Memory Space 7
mem7_label = tk.Label(window, text = "111: 0x0000", width = 17, height = 2)
mem7_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
mem7_label.place(x = 510, y = 650)

#Processor 0 Area
p0_area = tk.Canvas(window, width = 257, height = 290)
p0_area.configure(bg = 'deep sky blue')
p0_area.place(x = 840, y = 50)

#Processor 0 Area
p1_area = tk.Canvas(window, width = 257, height = 290)
p1_area.configure(bg = 'deep sky blue')
p1_area.place(x = 1132, y = 50)

#Processor 1 Area
p2_area = tk.Canvas(window, width = 257, height = 290)
p2_area.configure(bg = 'deep sky blue')
p2_area.place(x = 840, y = 380)

#Processor 2 Area
p3_area = tk.Canvas(window, width = 257, height = 290)
p3_area.configure(bg = 'deep sky blue')
p3_area.place(x = 1132, y = 380)

#Processor 0 Tag
p0_tag = tk.Label(window, text = "P0", width = 15, height = 2)
p0_tag.configure(bg = 'navy', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p0_tag.place(x = 840, y = 50)

#Processor 0 Cache Space 0
p0_cache0 = tk.Label(window, text = "B0: I 000 0x0000", width = 15, height = 1)
p0_cache0.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p0_cache0.place(x = 840, y = 140)

#Processor 0 Cache Space 1
p0_cache1 = tk.Label(window, text = "B1: I 000 0x0000", width = 15, height = 1)
p0_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p0_cache1.place(x = 840, y = 190)

#Processor 0 Cache Space 2
p0_cache2 = tk.Label(window, text = "B2: I 000 0x0000", width = 15, height = 1)
p0_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p0_cache2.place(x = 840, y = 240)

#Processor 0 Cache Space 3
p0_cache3 = tk.Label(window, text = "B3: I 000 0x0000", width = 15, height = 1)
p0_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p0_cache3.place(x = 840, y = 290)

#Processor 1 Tag
p1_tag = tk.Label(window, text = "P1", width = 15, height = 2)
p1_tag.configure(bg = 'navy', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p1_tag.place(x = 1132, y = 50)

#Processor 1 Cache Space 0
p1_cache0 = tk.Label(window, text = "B0: I 000 0x0000", width = 15, height = 1)
p1_cache0.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p1_cache0.place(x = 1132, y = 140)

#Processor 1 Cache Space 1
p1_cache1 = tk.Label(window, text = "B1: I 000 0x0000", width = 15, height = 1)
p1_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p1_cache1.place(x = 1132, y = 190)

#Processor 1 Cache Space 2
p1_cache2 = tk.Label(window, text = "B2: I 000 0x0000", width = 15, height = 1)
p1_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p1_cache2.place(x = 1132, y = 240)

#Processor 1 Cache Space 3
p1_cache3 = tk.Label(window, text = "B3: I 000 0x0000", width = 15, height = 1)
p1_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p1_cache3.place(x = 1132, y = 290)

#Processor 2 Tag
p2_tag = tk.Label(window, text = "P2", width = 15, height = 2)
p2_tag.configure(bg = 'navy', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p2_tag.place(x = 840, y = 380)

#Processor 2 Cache Space 0
p2_cache0 = tk.Label(window, text = "B0: I 000 0x0000", width = 15, height = 1)
p2_cache0.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p2_cache0.place(x = 840, y = 470)

#Processor 2 Cache Space 1
p2_cache1 = tk.Label(window, text = "B1: I 000 0x0000", width = 15, height = 1)
p2_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p2_cache1.place(x = 840, y = 520)

#Processor 2 Cache Space 2
p2_cache2 = tk.Label(window, text = "B2: I 000 0x0000", width = 15, height = 1)
p2_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p2_cache2.place(x = 840, y = 570)

#Processor 2 Cache Space 3
p2_cache3 = tk.Label(window, text = "B3: I 000 0x0000", width = 15, height = 1)
p2_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p2_cache3.place(x = 840, y = 620)

#Processor 3 Tag
p3_tag = tk.Label(window, text = "P3", width = 15, height = 2)
p3_tag.configure(bg = 'navy', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p3_tag.place(x = 1132, y = 380)

#Processor 3 Cache Space 0
p3_cache0 = tk.Label(window, text = "B0: I 000 0x0000", width = 15, height = 1)
p3_cache0.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p3_cache0.place(x = 1132, y = 470)

#Processor 3 Cache Space 1
p3_cache1 = tk.Label(window, text = "B1: I 000 0x0000", width = 15, height = 1)
p3_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p3_cache1.place(x = 1132, y = 520)

#Processor 3 Cache Space 2
p3_cache2 = tk.Label(window, text = "B2: I 000 0x0000", width = 15, height = 1)
p3_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p3_cache2.place(x = 1132, y = 570)

#Processor 3 Cache Space 3
p3_cache3 = tk.Label(window, text = "B3: I 000 0x0000", width = 15, height = 1)
p3_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
p3_cache3.place(x = 1132, y = 620)

#Start Button
start_button = tk.Button(window, text = 'Iniciar', width = 12, height = 3, command = lambda: window.quit())
start_button.configure(bg = 'medium spring green')
start_button['font'] = font.Font(family ='Helvetica', size = 11, weight = 'bold')
start_button.place(x = 55, y = 700)

#Stop Button
stop_button = tk.Button(window, text = 'Detener', width = 12, height = 3, command = lambda: window.quit())
stop_button.configure(bg = 'light coral')
stop_button['font'] = font.Font(family ='Helvetica', size = 11, weight = 'bold')
stop_button.place(x = 190, y = 700)

#Next Button
next_button = tk.Button(window, text = 'Siguiente', width = 12, height = 3, command = lambda: window.quit())
next_button.configure(bg = 'light goldenrod')
next_button['font'] = font.Font(family ='Helvetica', size = 11, weight = 'bold')
next_button.place(x = 325, y = 700)

#Enter Button
enter_button = tk.Button(window, text = 'Ingresar', width = 12, height = 1, command = lambda: window.quit())
enter_button.configure(bg = 'snow4')
enter_button['font'] = font.Font(family ='Helvetica', size = 11, weight = 'bold')
enter_button.place(x = 325, y = 550)

#Display Information
latest_instructions = tk.Label(window, text = "Latest instructions", width = 25, height = 1, justify = tk.LEFT)
latest_instructions.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 15, weight = 'bold'))
latest_instructions.place(x = 30, y = 50)
p0_instruction = tk.Label(window, text = "P0: ", width = 25, height = 1, justify = tk.LEFT)
p0_instruction.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
p0_instruction.place(x = 30, y = 80)
p1_instruction = tk.Label(window, text = "P1: ", width = 25, height = 1, justify = tk.LEFT)
p1_instruction.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
p1_instruction.place(x = 30, y = 100)
p2_instruction = tk.Label(window, text = "P2: ", width = 25, height = 1, justify = tk.LEFT)
p2_instruction.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
p2_instruction.place(x = 30, y = 120)
p3_instruction = tk.Label(window, text = "P3: ", width = 25, height = 1, justify = tk.LEFT)
p3_instruction.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
p3_instruction.place(x = 30, y = 140)
alerts = tk.Label(window, text = "Alerts", width = 15, height = 1, justify = tk.LEFT)
alerts.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 15, weight = 'bold'))
alerts.place(x = 30, y = 170)
alert_p0 = tk.Label(window, text = "P0: ", width = 25, height = 1, justify = tk.LEFT)
alert_p0.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
alert_p0.place(x = 30, y = 200)
alert_p1 = tk.Label(window, text = "P1: ", width = 25, height = 1, justify = tk.LEFT)
alert_p1.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
alert_p1.place(x = 30, y = 220)
alert_p2 = tk.Label(window, text = "P2: ", width = 25, height = 1, justify = tk.LEFT)
alert_p2.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
alert_p2.place(x = 30, y = 240)
alert_p3 = tk.Label(window, text = "P3: ", width = 25, height = 1, justify = tk.LEFT)
alert_p3.configure(bg = 'azure2', fg = 'black', font = font.Font(family ='Helvetica', size = 12, weight = 'bold'))
alert_p3.place(x = 30, y = 260)

#Global variables
instructionP0 = ""
instructionP1 = ""
instructionP2 = ""
instructionP3 = ""
alert0 = ""
alert1 = ""
alert2 = ""
alert3 = ""

#Main instance
cont = Controller()

# print("Instrucción P0: WRITE 010;ABCD")
# cont.change_state(0, "I", "010", "ABCD", "WRITE")
# cont.mem.print_cache()
# cont.mem.print_memory()

# print("Instrucción P2: WRITE 010;0111")
# cont.change_state(2, "I", "010", "0111", "WRITE")
# cont.mem.print_cache()
# cont.mem.print_memory()

# print("Instrucción P1: READ 010")
# cont.change_state(1, "I", "010", "", "READ")
# cont.mem.print_cache()
# cont.mem.print_memory()

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