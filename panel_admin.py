import customtkinter as ctk
from tkinter import messagebox, Label, END
import mysql.connector
from PIL import ImageTk, Image


class Admin(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("%dx%d+%d+%d" % (500, 510, 400, 50))
        self.iconbitmap("icons\\admin_man_person_user_icon_127232.ico")
        self.title("پنل ادمین")
        
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="froshgahkafsh"
        )
        self.my_cursor = self.db.cursor()
        
        self.frame1 = ctk.CTkFrame(self, width=490, height=60, fg_color="#1aad89")
        self.frame1.pack(padx=5, pady=5)
        
        self.lbl_f1 = ctk.CTkLabel(self.frame1, text="Admin", font=("b nazanin", 30, "bold"), width=480, height=50,
                                   text_color="white", fg_color="#1aad89")
        self.lbl_f1.pack(padx=5, pady=5, ipady=5)
    
        # ---------------------------------------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------
        
        
        self.frame2 = ctk.CTkFrame(self, width=150, height=110)
        self.frame2.pack(padx=5, pady=5)
        
        self.img1 = Image.open("pictuer\\admin_person_user_man_2839.png")
        self.img1 = self.img1.resize((150, 110), Image.ANTIALIAS)
        self.photoImg1 = ImageTk.PhotoImage(self.img1)
        
        self.label1 = Label(self.frame2, image=self.photoImg1, width=500, height=100)
        self.label1.pack()
    
        # ---------------------------------------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------
        
        self.frame3 = ctk.CTkFrame(self, width=490, height=50, fg_color="#fa712d")
        self.frame3.pack(padx=5, pady=5)
        
        self.lbl_f2 = ctk.CTkLabel(self.frame3, text="تذکر: این پنل مخصوص آپدیت کردن نام کاربری و پسوورد برای ورود به برنامه است در انتخاب این موارد دقت کنید", font=("b nazanin", 14),
                                   text_color="white")
        self.lbl_f2.pack(padx=5, pady=5, ipady=5)
        
        # ---------------------------------------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------
        
        self.frame4 = ctk.CTkFrame(self, width=490, height=250, fg_color="#1aad89")
        self.frame4.pack(padx=5, pady=5)
        
        self.lbl_username = ctk.CTkLabel(self.frame4, text="نام کاربری", font=("b nazanin", 30, "bold"),
                                         text_color="white")
        self.lbl_username.place(x=350, y=30)
        
        self.lbl_password = ctk.CTkLabel(self.frame4, text="پسوورد", font=("b nazanin", 30, "bold"),
                                         text_color="white")
        self.lbl_password.place(x=370, y=100)
        
        self.txt_username = ctk.CTkEntry(self.frame4, width=300, height=40, font=("Arial", 17, "bold"),
                                              justify="center")
        self.txt_username.place(x=15, y=40)
        
        self.txt_password = ctk.CTkEntry(self.frame4, width=300, height=40, font=("Arial", 17, "bold"),
                                              justify="center")
        self.txt_password.place(x=15, y=100)
        
        self.check_box = ctk.CTkCheckBox(self.frame4, text="Hide Password", command=self.Hide_pass, text_color="white")
        self.check_box.place(x=100, y=160)
        
        self.btn_sub = ctk.CTkButton(self.frame4, text="ثبت", font=("b nazanin", 20, "bold"), width=250,
                                     fg_color="#0c8556", border_width=3, border_color="white", command=self.sub)
        self.btn_sub.place(x=15, y=200)
        
        self.btn_back = ctk.CTkButton(self.frame4, text="بازگشت", font=("b nazanin", 20), width=150,
                                     fg_color="#f05c07", border_width=3, border_color="white", 
                                     text_color="white", command=self.back)
        self.btn_back.place(x=300, y=202)
    
    
    def back(self):
        from Start import Start
        
        self.destroy()
        app = Start()
        app.mainloop()
        
    def Hide_pass(self):
        if self.check_box.get():
            self.txt_password.configure(show="*")
        else:
            self.txt_password.configure(show="")
    
    def sub(self):
        
        username = self.txt_username.get()
        password = self.txt_password.get()
        
        if username != "" and password != "":
            self.my_cursor.execute(f"UPDATE admin_user SET username_ = '{username}', password_ = '{password}' WHERE user_id = 1;")
            self.db.commit()
            for txt in [self.txt_password, self.txt_username]:
                txt.delete(0, END)
            self.txt_username.focus_set()
            messagebox.showinfo("Sub", "نام کاربری و پسوورد با موفقیت ثبت شد")
        else:
            messagebox.showerror("Error", "لطفا باکس هارا خالی نذارید")
