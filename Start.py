from tkinter import *
import customtkinter as ctk
from PIL import ImageTk, Image
from forosh import Forosh
from Anbar_forosh import AnbarForosh
from Anbar import Anbar
from panel_admin import Admin


class Start(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("%dx%d+%d+%d" % (915, 603, 250, 50))
        self.resizable(False, False)
        self.iconbitmap("icons\\3643769-building-home-house-main-menu-start_113416.ico")
        self.title("منوی شروع")
        
        # -------------------------------- Frame1 --------------------------------
        self.frame1 = ctk.CTkFrame(self, fg_color="white", width=900, border_width=5,
                                   border_color="gray")
        self.frame1.pack(padx=5, pady=5)
        
        self.img1 = Image.open("pictures\pic.png")
        self.img1 = self.img1.resize((500, 100))
        self.photoImg1 = ImageTk.PhotoImage(self.img1)
        
        self.label1 = Label(self.frame1, image=self.photoImg1, width=500, height=100, bg="white")
        self.label1.place(x=200, y=5)
        
        self.label2 = ctk.CTkLabel(self.frame1, text="فروشگاه کفش", font=("b nazanin", 40, "bold"))
        self.label2.place(x=350, y=110)
        
        # -------------------------------- Frame2 --------------------------------
        self.frame2 = ctk.CTkFrame(self, fg_color="white", width=900,
                                   height=400, border_width=5, border_color="gray")
        self.frame2.pack(padx=5, pady=5)
        
        self.img2 = Image.open("pictures\فروشگاه-کفش-و-کتونی-زیتون-1536x864.jpg")
        self.img2 = self.img2.resize((700, 365))
        self.photoImg2 = ImageTk.PhotoImage(self.img2)
        
        self.label1 = Label(self.frame2, image=self.photoImg2, width=700, height=365, bg="white")
        self.label1.place(x=7, y=7)
        
        self.btn1 = ctk.CTkButton(self.frame2, text="بخش فروش", width=165, height=40, fg_color="#3498eb",
                                       text_color="white", font=("b nazanin", 18, "bold"), border_width=4,
                                       border_color="#0d426e", command=self.btn_1)
        self.btn1.place(x=720, y=10)
        
        self.btn2 = ctk.CTkButton(self.frame2, text="بخش انبار", width=165, height=40, fg_color="#3498eb",
                                       text_color="white", font=("b nazanin", 18, "bold"), border_width=4,
                                       border_color="#0d426e", command=self.btn_2)
        self.btn2.place(x=720, y=60)
        
        self.btn3 = ctk.CTkButton(self.frame2, text="بخش انبار فروش", width=165, height=40, fg_color="#3498eb",
                                       text_color="white", font=("b nazanin", 18, "bold"), border_width=4,
                                       border_color="#0d426e", command=self.btn_3)
        self.btn3.place(x=720, y=110)
        
        self.btn4 = ctk.CTkButton(self.frame2, text="پنل ادمین", width=165, height=40, fg_color="#3498eb",
                                       text_color="white", font=("b nazanin", 18, "bold"), border_width=4,
                                       border_color="#0d426e", command=self.btn_4)
        self.btn4.place(x=720, y=160)
        
        self.btn5 = ctk.CTkButton(self.frame2, text="خروج", width=165, height=40, fg_color="#e6051b",
                                       text_color="white", font=("b nazanin", 18, "bold"), border_width=4,
                                       border_color="#47050a", command=self.btn_5)
        self.btn5.place(x=720, y=330)

    def btn_1(self):
        self.destroy()
        app = Forosh()
        app.mainloop()
    
    def btn_2(self):
        self.destroy()
        app = Anbar()
        app.mainloop()
    
    def btn_3(self):
        self.destroy()
        app = AnbarForosh()
        app.mainloop()
    
    def btn_4(self):
        self.destroy()
        app = Admin()
        app.mainloop()
    
    def btn_5(self):
        self.destroy()

def main():
    app = Start()
    app.mainloop()

if __name__ == "__main__":
    main()