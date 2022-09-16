from cmath import inf
import tkinter as tk
import tkinter.font as font

class Gui:
    def __init__(self):
        
        """------------------------------------------Window-------------------------------------------"""
        window = tk.Tk()
        window.title("Visualizador")
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        window.geometry("%dx%d" % (width, height))
        window.resizable(0, 0)
        window.configure(bg = 'gray')    

        """-------------------------------------------Areas-------------------------------------------"""
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

        #Processor 0 Area
        p0_area = tk.Canvas(window, width = 257, height = 290)
        p0_area.configure(bg = 'deep sky blue')
        p0_area.place(x = 840, y = 50)

        #Processor 1 Area
        p1_area = tk.Canvas(window, width = 257, height = 290)
        p1_area.configure(bg = 'deep sky blue')
        p1_area.place(x = 1132, y = 50)

        #Processor 2 Area
        p2_area = tk.Canvas(window, width = 257, height = 290)
        p2_area.configure(bg = 'deep sky blue')
        p2_area.place(x = 840, y = 380)

        #Processor 3 Area
        p3_area = tk.Canvas(window, width = 257, height = 290)
        p3_area.configure(bg = 'deep sky blue')
        p3_area.place(x = 1132, y = 380)

        """------------------------------------------Labels-------------------------------------------"""
        #Memory Space 0
        mem0_label = tk.Label(window, text = "0x0", width = 17, height = 2)
        mem0_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        mem0_label.place(x = 510, y = 20)

        #Memory Space 1
        mem1_label = tk.Label(window, text = "0x1", width = 17, height = 2)
        mem1_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        mem1_label.place(x = 510, y = 110)

        #Memory Space 2
        mem2_label = tk.Label(window, text = "0x2", width = 17, height = 2)
        mem2_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        mem2_label.place(x = 510, y = 200)

        #Memory Space 3
        mem3_label = tk.Label(window, text = "0x3", width = 17, height = 2)
        mem3_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        mem3_label.place(x = 510, y = 290)

        #Memory Space 4
        mem4_label = tk.Label(window, text = "0x4", width = 17, height = 2)
        mem4_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        mem4_label.place(x = 510, y = 380)

        #Memory Space 5
        mem5_label = tk.Label(window, text = "0x5", width = 17, height = 2)
        mem5_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        mem5_label.place(x = 510, y = 470)

        #Memory Space 6
        mem6_label = tk.Label(window, text = "0x6", width = 17, height = 2)
        mem6_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        mem6_label.place(x = 510, y = 560)

        #Memory Space 7
        mem7_label = tk.Label(window, text = "0x7", width = 17, height = 2)
        mem7_label.configure(bg = 'purple3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        mem7_label.place(x = 510, y = 650)

        #Processor 0 Tag
        p0_tag = tk.Label(window, text = "P0", width = 15, height = 2)
        p0_tag.configure(bg = 'navy', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p0_tag.place(x = 840, y = 50)

        #Processor 0 Cache Space 1
        p0_cache1 = tk.Label(window, text = "1", width = 15, height = 1)
        p0_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p0_cache1.place(x = 840, y = 140)

        #Processor 0 Cache Space 2
        p0_cache2 = tk.Label(window, text = "2", width = 15, height = 1)
        p0_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p0_cache2.place(x = 840, y = 190)

        #Processor 0 Cache Space 3
        p0_cache3 = tk.Label(window, text = "3", width = 15, height = 1)
        p0_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p0_cache3.place(x = 840, y = 240)

        #Processor 0 Cache Space 4
        p0_cache4 = tk.Label(window, text = "4", width = 15, height = 1)
        p0_cache4.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p0_cache4.place(x = 840, y = 290)

        #Processor 1 Tag
        p1_tag = tk.Label(window, text = "P1", width = 15, height = 2)
        p1_tag.configure(bg = 'navy', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p1_tag.place(x = 1132, y = 50)

        #Processor 1 Cache Space 1
        p1_cache1 = tk.Label(window, text = "1", width = 15, height = 1)
        p1_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p1_cache1.place(x = 1132, y = 140)

        #Processor 1 Cache Space 2
        p1_cache2 = tk.Label(window, text = "2", width = 15, height = 1)
        p1_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p1_cache2.place(x = 1132, y = 190)

        #Processor 1 Cache Space 3
        p1_cache3 = tk.Label(window, text = "3", width = 15, height = 1)
        p1_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p1_cache3.place(x = 1132, y = 240)

        #Processor 1 Cache Space 4
        p1_cache4 = tk.Label(window, text = "4", width = 15, height = 1)
        p1_cache4.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p1_cache4.place(x = 1132, y = 290)

        #Processor 2 Tag
        p2_tag = tk.Label(window, text = "P2", width = 15, height = 2)
        p2_tag.configure(bg = 'navy', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p2_tag.place(x = 840, y = 380)

        #Processor 2 Cache Space 1
        p2_cache1 = tk.Label(window, text = "1", width = 15, height = 1)
        p2_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p2_cache1.place(x = 840, y = 470)

        #Processor 2 Cache Space 2
        p2_cache2 = tk.Label(window, text = "2", width = 15, height = 1)
        p2_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p2_cache2.place(x = 840, y = 520)

        #Processor 2 Cache Space 3
        p2_cache3 = tk.Label(window, text = "3", width = 15, height = 1)
        p2_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p2_cache3.place(x = 840, y = 570)

        #Processor 2 Cache Space 4
        p2_cache4 = tk.Label(window, text = "4", width = 15, height = 1)
        p2_cache4.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p2_cache4.place(x = 840, y = 620)

        #Processor 3 Tag
        p3_tag = tk.Label(window, text = "P3", width = 15, height = 2)
        p3_tag.configure(bg = 'navy', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p3_tag.place(x = 1132, y = 380)

        #Processor 3 Cache Space 1
        p3_cache1 = tk.Label(window, text = "1", width = 15, height = 1)
        p3_cache1.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p3_cache1.place(x = 1132, y = 470)

        #Processor 3 Cache Space 2
        p3_cache2 = tk.Label(window, text = "2", width = 15, height = 1)
        p3_cache2.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p3_cache2.place(x = 1132, y = 520)

        #Processor 3 Cache Space 3
        p3_cache3 = tk.Label(window, text = "3", width = 15, height = 1)
        p3_cache3.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p3_cache3.place(x = 1132, y = 570)

        #Processor 3 Cache Space 4
        p3_cache4 = tk.Label(window, text = "4", width = 15, height = 1)
        p3_cache4.configure(bg = 'blue3', fg = 'white', font = font.Font(family ='Helvetica', size = 20, weight = 'bold'))
        p3_cache4.place(x = 1132, y = 620)

        """------------------------------------------Buttons------------------------------------------"""
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

        """-------------------------------------------Inputs------------------------------------------"""
        #Instruction Input
        instruction_input = tk.Entry(width = 20, font = font.Font(family = "Helvetica", size = 15))
        instruction_input.place(x = 60, y = 553)

        
        
        window.mainloop()
