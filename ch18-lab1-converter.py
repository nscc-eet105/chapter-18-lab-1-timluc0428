# Timothy Lucas
# Lab 18-1
# 2025-07-29

import tkinter as tk

class FeetAndInchesConverterGui:
    def __init__(self):
        
        self.main_window = tk.Tk()
        self.main_window.title("Feet and Inches to Inches Converter")

        self.top_frame = tk.Frame()
        self.entries_frame = tk.Frame()
        self.output_frame = tk.Frame()
        self.button_frame = tk.Frame()

        self.title_label = tk.Label(self.top_frame, 
                                    text="Feet and Inches Converter")
        
        self.title_label.pack(side="left")

        self.prompt_label1 = tk.Label(self.entries_frame,
                                      text="Feet:")
    
        self.feet_entry = tk.Entry(self.entries_frame,
                                   width=3)

        self.prompt_label2 = tk.Label(self.entries_frame,
                                     text="Inches:")
        self.inches = tk.StringVar
        self.inches_entry = tk.Entry(self.entries_frame,
                                     width=3)
        
        self.prompt_label1.pack(side="left")
        self.feet_entry.pack(side="left")
        self.prompt_label2.pack(side="left")
        self.inches_entry.pack(side="left")

        self.output_description_label = tk.Label(self.output_frame,
                                     text="Inches: ")
        
        self.output_inches = tk.StringVar()

        self.output_inches_label = tk.Label(self.output_frame, 
                                            textvariable=self.output_inches)
        
        self.output_description_label.pack(side="left")
        self.output_inches_label.pack(side="left")

        self.convert_button = tk.Button(self.button_frame,
                                        text="Convert",
                                        command=self.convert)
        
        self.quit_button = tk.Button(self.button_frame,
                                     text="Exit",
                                     command=self.main_window.destroy)

        self.convert_button.pack(side="left")
        self.quit_button.pack(side="left")


        self.top_frame.pack()
        self.entries_frame.pack()
        self.output_frame.pack()
        self.button_frame.pack()        

        tk.mainloop()
    
    def convert(self):
        feet = float(self.feet_entry.get())
        inches = float(self.inches_entry.get())
        inches = (feet * 12) + inches

        self.output_inches.set(inches)

if __name__ == '__main__':
    feet_conv = FeetAndInchesConverterGui()