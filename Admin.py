import customtkinter as ctk
from tkinter import messagebox, Label
import mysql.connector
from PIL import ImageTk, Image


class Admin(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("%dx%d+%d+%d" % (500, 448, 400, 50))
        self.iconbitmap("icons\Login_37128.ico")
        self.title("بخش ورود")
        
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="froshgahkafsh"
        )
        self.my_cursor = self.db.cursor()
        
        self.frame1 = ctk.CTkFrame(self, width=490, height=60, fg_color="#534b61")
        self.frame1.pack(padx=5, pady=5)
        
        self.lbl_f1 = ctk.CTkLabel(self.frame1, text="بخش ورود", font=("b nazanin", 30, "bold"), width=480, height=50,
                                   text_color="white", fg_color="#534b61")
        self.lbl_f1.pack(padx=5, pady=5)
        
        # ---------------------------------------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------
        
        self.frame2 = ctk.CTkFrame(self, width=150, height=110)
        self.frame2.pack(padx=5, pady=5)
        
        self.img1 = Image.open("pictuer\login_icon_176905.png")
        self.img1 = self.img1.resize((150, 110), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(self.img1)
        
        self.label1 = Label(self.frame2, image=self.photoImg1, width=500, height=100)
        self.label1.pack()
    
        # ---------------------------------------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------
        
        self.frame3 = ctk.CTkFrame(self, width=490, height=250, fg_color="#534b61")
        self.frame3.pack(padx=5, pady=5)
        
        self.lbl_username = ctk.CTkLabel(self.frame3, text="نام کاربری", font=("b nazanin", 30, "bold"),
                                         text_color="white")
        self.lbl_username.place(x=350, y=30)
        
        self.lbl_password = ctk.CTkLabel(self.frame3, text="پسوورد", font=("b nazanin", 30, "bold"),
                                         text_color="white")
        self.lbl_password.place(x=370, y=100)
        
        self.txt_username = ctk.CTkEntry(self.frame3, width=300, height=40, font=("Arial", 17, "bold"),
                                              justify="center", border_width=3, border_color="#27242b")
        self.txt_username.place(x=15, y=40)
        
        self.txt_password = ctk.CTkEntry(self.frame3, width=300, height=40, font=("Arial", 17, "bold"),
                                              justify="center", border_width=3, border_color="#27242b")
        self.txt_password.place(x=15, y=100)
        
        self.check_box = ctk.CTkCheckBox(self.frame3, text="Hide Password", command=self.Hide_pass,
                                         text_color="white", border_width=2, border_color="white")
        self.check_box.place(x=100, y=160)
        
        self.btn_sub = ctk.CTkButton(self.frame3, text="ورود", font=("b nazanin", 20, "bold"), width=300,
                                     fg_color="#b330f0", border_width=3, border_color="#27242b", command=self.sub,
                                     text_color="white")
        self.btn_sub.place(x=15, y=200)
        
        
    def Hide_pass(self):
        if self.check_box.get():
            self.txt_password.configure(show="*")
        else:
            self.txt_password.configure(show="")
    
    def check(self, username, password):
        self.my_cursor.execute(f"SELECT * FROM admin_user;")
        for item in self.my_cursor:
            if item[1] == username and item[2] == password:
                return True
        return False

    def back(self):
        from Start import Start
        
        self.destroy()
        app = Start()
        app.mainloop()
    
    def sub(self):
        
        username = self.txt_username.get()
        password = self.txt_password.get()
        
        if self.check(username, password):
            self.back()
        else:
            messagebox.showerror("Error", "نام کاربری و پسورد اشتباه است")


def main():
    app = Admin()
    app.mainloop()

if __name__ == "__main__":
    main()