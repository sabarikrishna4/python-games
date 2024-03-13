import customtkinter
from threading import Thread
import time

customtkinter.set_appearance_mode("dark")

class XOGAME(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("200x250")
        self.title("TIC-TAC GAME")
        self.color_flag = True
        self.seleted_list = []
        self.str_list = [customtkinter.StringVar(self,"None") for _ in range(0,9)]

        self.btn1 = customtkinter.CTkButton(self,width=60, height=60,text="", command=lambda: self.color_box(0))
        self.btn1.place(x=5,y=0)
        self.btn2 = customtkinter.CTkButton(self,width=60, height=60,text="", command=lambda: self.color_box(1))
        self.btn2.place(x=70,y=0)
        self.btn3 = customtkinter.CTkButton(self,width=60, height=60,text="", command=lambda: self.color_box(2))
        self.btn3.place(x=135,y=0)
        self.btn4 = customtkinter.CTkButton(self,width=60, height=60,text="", command=lambda: self.color_box(3))
        self.btn4.place(x=5,y=65)
        self.btn5 = customtkinter.CTkButton(self,width=60, height=60,text="", command=lambda: self.color_box(4))
        self.btn5.place(x=70,y=65)
        self.btn6 = customtkinter.CTkButton(self,width=60, height=60,text="", command=lambda: self.color_box(5))
        self.btn6.place(x=135,y=65)
        self.btn7 = customtkinter.CTkButton(self,width=60, height=60,text="", command=lambda: self.color_box(6))
        self.btn7.place(x=5,y=130)
        self.btn8 = customtkinter.CTkButton(self,width=60, height=60,text="", command=lambda: self.color_box(7))
        self.btn8.place(x=70,y=130)
        self.btn9 = customtkinter.CTkButton(self,width=60, height=60,text="", command=lambda: self.color_box(8))
        self.btn9.place(x=135,y=130)

        self.btn_list = [self.btn1, self.btn2, self.btn3,
                        self.btn4, self.btn5, self.btn6,
                        self.btn7, self.btn8, self.btn9]
        
        self.label = customtkinter.CTkLabel(self, text="", fg_color="yellow", corner_radius=10, width=120,
                                                 height=40)
        self.label.place(x=40, y=200)
        self.text_label = customtkinter.CTkLabel(self, text="Let's Start..!", fg_color="yellow", text_color="black",
                                                 font=("Bold",18),bg_color="yellow" )
        self.text_label.place(x=53, y=207)
        

    def color_box(self,i):
        if i not in self.seleted_list:
            if self.color_flag is True:
                self.btn_list[i].configure(fg_color="red", hover_color="dark red", text = "x", font=("bold",50))
                self.str_list[i].set(0)
                self.color_flag = False
                self.seleted_list.append(i)
                self.label.configure(fg_color="Green")
                self.text_label.configure(text="Green Turn!", fg_color="Green", bg_color="Green")
                self.text_label.place(x=51, y=207)
                Thread(target=self.tic_tac_logic,).start()
                
            else:
                self.btn_list[i].configure(fg_color="green", hover_color="dark green",text="o", font=("bold",50))
                self.str_list[i].set(1)
                self.color_flag = True
                self.seleted_list.append(i)
                self.label.configure(fg_color="Red")
                self.text_label.configure(text="Red Turn!", fg_color="Red", bg_color="Red")
                self.text_label.place(x=60, y=207)
                Thread(target=self.tic_tac_logic,).start()


    def tic_tac_logic(self):
        check_list = [ [0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6] ]
        str_lists = [self.str_list[i].get() for i in range(0,9) ]
        print(str_lists)
        for i in check_list:
            x_list = []
            o_list = []
            print(i)
            for j in i:
                value = str_lists[j]
                if value == '0':
                    x_list.append(0)
                elif value == '1':
                    o_list.append(1)
            if len(x_list) == 3 or len(o_list) == 3:
                print("winner")
                self.label.configure(fg_color="yellow")
                self.text_label.configure(text="winner..!", fg_color="yellow", bg_color="yellow")
                self.text_label.place(x=60, y=207)
                break

if __name__ == "__main__":
    obj = XOGAME()
    obj.mainloop()