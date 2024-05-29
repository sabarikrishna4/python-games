import customtkinter
from threading import Thread
import time
from PIL import Image


customtkinter.set_appearance_mode("dark")


class XOGAME(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("200x250")
        self.title("TIC-TAC GAME")
        self.resizable(width=0,height=0)
        self.check_list = [
            [0, 1, 2],
            [2, 1, 0],
            [3, 4, 5],
            [5, 4, 3],
            [6, 7, 8],
            [8, 7, 6],
            [0, 3, 6],
            [6, 3, 0],
            [1, 4, 7],
            [7, 4, 1],
            [2, 5, 8],
            [8, 5, 2],
            [0, 4, 8],
            [8, 4, 0],
            [2, 4, 6],
            [6, 4, 2],
        ]
        self.btns()
        Thread(
            target=self.tic_tac_logic,
        ).start()

    def btns(self):
        self.color_flag = True
        self.seleted_list = []
        self.str_list = [customtkinter.StringVar(self, "None") for _ in range(0, 9)]

        self.btn1 = customtkinter.CTkButton(
            self, width=60, height=60, text="", command=lambda: self.color_box(0)
        )
        self.btn1.place(x=5, y=0)
        self.btn2 = customtkinter.CTkButton(
            self, width=60, height=60, text="", command=lambda: self.color_box(1)
        )
        self.btn2.place(x=70, y=0)
        self.btn3 = customtkinter.CTkButton(
            self, width=60, height=60, text="", command=lambda: self.color_box(2)
        )
        self.btn3.place(x=135, y=0)
        self.btn4 = customtkinter.CTkButton(
            self, width=60, height=60, text="", command=lambda: self.color_box(3)
        )
        self.btn4.place(x=5, y=65)
        self.btn5 = customtkinter.CTkButton(
            self, width=60, height=60, text="", command=lambda: self.color_box(4)
        )
        self.btn5.place(x=70, y=65)
        self.btn6 = customtkinter.CTkButton(
            self, width=60, height=60, text="", command=lambda: self.color_box(5)
        )
        self.btn6.place(x=135, y=65)
        self.btn7 = customtkinter.CTkButton(
            self, width=60, height=60, text="", command=lambda: self.color_box(6)
        )
        self.btn7.place(x=5, y=130)
        self.btn8 = customtkinter.CTkButton(
            self, width=60, height=60, text="", command=lambda: self.color_box(7)
        )
        self.btn8.place(x=70, y=130)
        self.btn9 = customtkinter.CTkButton(
            self, width=60, height=60, text="", command=lambda: self.color_box(8)
        )
        self.btn9.place(x=135, y=130)

        self.btn_list = [
            self.btn1,
            self.btn2,
            self.btn3,
            self.btn4,
            self.btn5,
            self.btn6,
            self.btn7,
            self.btn8,
            self.btn9,
        ]

        self.txt_label = customtkinter.CTkLabel(
            self,
            text="Let's Start..!",
            fg_color="#242424",
            width=122,
            height=40,
            text_color="white",
            font=("Bold", 18),
            bg_color="#242424",
        )
        self.txt_label.place(x=10, y=200)

        self.retry_img = customtkinter.CTkImage(Image.open("retry.png"), size=(30, 30))

        self.retry_btn = customtkinter.CTkButton(
            self,
            text="",
            command=self.reset_game,
            height=40,
            width=40,
            image=self.retry_img,
            fg_color="yellow",
        )
        self.retry_btn.place(x=145, y=200)

    def reset_game(self):
        for i in self.btn_list:
            i.destroy()
        self.txt_label.destroy()
        self.btns()

    def color_box(self, i):
        if i not in self.seleted_list:
            if self.color_flag is True:
                self.btn_list[i].configure(
                    fg_color="red", hover_color="dark red", text="x", font=("bold", 48)
                )
                self.str_list[i].set(0)
                self.color_flag = False
                self.seleted_list.append(i)
                self.txt_label.configure(
                    text="O - Turn!",
                    fg_color="#242424",
                )
            else:
                self.btn_list[i].configure(
                    fg_color="green",
                    hover_color="dark green",
                    text="o",
                    font=("bold", 48),
                )
                self.str_list[i].set(1)
                self.color_flag = True
                self.seleted_list.append(i)
                self.txt_label.configure(
                    text="X - Turn!",
                    fg_color="#242424",
                )

    def tic_tac_logic(self):
        while True:
            str_lists = []
            draw_flag = True
            for i in self.check_list:
                c_list = [self.str_list[j].get() for j in i]
                str_lists.append(c_list)

            for i in str_lists:
                for j in i:
                    if j == "None":
                        draw_flag = False

            if ["1", "1", "1"] in str_lists or ["0", "0", "0"] in str_lists:
                if ["1", "1", "1"] in str_lists:
                    winner = "O"
                else:
                    winner = "X"
                print("win")
                for i in range(0, 9):
                    self.str_list[i].set("None")
                for i in self.btn_list:
                    i.configure(state="disabled")
                self.txt_label.configure(
                    text=f"{winner} - winner..!", fg_color="#242424"
                )
            elif draw_flag is True:
                self.txt_label.configure(text="Draw..!", fg_color="#242424")
            else:
                time.sleep(0.1)


if __name__ == "__main__":
    obj = XOGAME()
    obj.mainloop()
