import customtkinter as ctk
from tkinter import ttk
from tkinter import Scrollbar
import tkinter.messagebox
import mysql.connector



class Anbar(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="froshgahkafsh"
        )
        self.my_cursor = self.db.cursor()
        
        self.geometry("%dx%d+%d+%d" % (1000, 700, 150, 5))
        self.title("انبار کالا")
        self.iconbitmap("icons\loading_delivery_package_cargo_courier_icon_187257.ico")
        
        # --------------------------------------------------- FRAME 1 ---------------------------------------------------
        self.Frame1 = ctk.CTkFrame(self, fg_color="#3283a8")
        self.Frame1.pack(padx=5, pady=5)
        
        self.LabelHeader = ctk.CTkLabel(self.Frame1, text="بخش انبار", font=("b nazanin", 30, "bold"),
                                        width=980, height=50, fg_color="#3283a8", text_color="white")
        self.LabelHeader.pack(pady=5, padx=5)

        # --------------------------------------------------- FRAME 2 ---------------------------------------------------
        self.Frame2 = ctk.CTkFrame(self, fg_color="#3283a8")
        self.Frame2.pack()
        
        # --------- Frame 2(1) ---------
        self.Frame2_1 = ctk.CTkFrame(self.Frame2, width=480, height=200, fg_color="#6ec7f0")
        self.Frame2_1.grid(row=0, column=0, padx=7, pady=7)
        
        self.LabelMoshakhasat = ctk.CTkLabel(self.Frame2_1, text="افزودن به انبار", font=("b nazanin", 25, "bold"),
                                        width=480, height=40, fg_color="#6ec7f0", text_color="white")
        self.LabelMoshakhasat.place(x=0, y=0)
        
        self.txtbox_Id = ctk.CTkEntry(self.Frame2_1, placeholder_text="کد را وارد کنید",
                                      justify="right", font=("b nazanin", 18), width=200, height=30)
        self.txtbox_Id.place(x=265, y=45)
        
        self.txtbox_color = ctk.CTkEntry(self.Frame2_1, placeholder_text="رنگ را وارد کنید",
                                      justify="right", font=("b nazanin", 18), width=200, height=30)
        self.txtbox_color.place(x=265, y=83)
        
        self.txtbox_gender = ctk.CTkComboBox(self.Frame2_1, values=['زنانه', 'مردانه'],
                                      font=("b nazanin", 18), width=200, height=30)
        self.txtbox_gender.place(x=265, y=120)
        
        self.txtbox_size = ctk.CTkEntry(self.Frame2_1, placeholder_text="سایز را وارد کنید",
                                      justify="left", font=("b nazanin", 18), width=200, height=30)
        self.txtbox_size.place(x=20, y=45)
        
        self.txtbox_count = ctk.CTkEntry(self.Frame2_1, placeholder_text="تعداد را وارد کنید",
                                      justify="left", font=("b nazanin", 18), width=200, height=30)
        self.txtbox_count.place(x=20, y=83)
        
        self.txtbox_price = ctk.CTkEntry(self.Frame2_1, placeholder_text="قیمت را وارد کنید",
                                      justify="left", font=("b nazanin", 18), width=200, height=30)
        self.txtbox_price.place(x=20, y=120)
        
        self.btnEdit = ctk.CTkButton(self.Frame2_1, text="ویرایش", width=150, height=30, fg_color="#205a75",
                                       text_color="white", font=("b nazanin", 15, "bold"), border_width=2,
                                       border_color="white", state='disable', command=self.Edit)
        self.btnEdit.place(x=5, y=160)
        
        self.clear_btn = ctk.CTkButton(self.Frame2_1, text="حذف موارد تکست باکس", width=150, height=30, fg_color="#205a75",
                                       text_color="white", font=("b nazanin", 15, "bold"), border_width=2,
                                       border_color="white", command=self.Cleartxt)
        self.clear_btn.place(x=163, y=160)
        
        self.btnSubmt = ctk.CTkButton(self.Frame2_1, text="ثبت درانبار", width=150, height=30, fg_color="#205a75",
                                       text_color="white", font=("b nazanin", 15, "bold"), border_width=2,
                                       border_color="white", command=self.Submit)
        self.btnSubmt.place(x=320, y=160)
        
        # --------- Frame 2(2) ---------
        self.Frame2_2 = ctk.CTkFrame(self.Frame2, width=480, height=200, fg_color="#6ec7f0")
        self.Frame2_2.grid(row=0, column=1, padx=7, pady=7)
        
        self.LabelMoshakhasat = ctk.CTkLabel(self.Frame2_2, text="جستجو", font=("b nazanin", 25, "bold"),
                                        width=480, height=40, fg_color="#6ec7f0", text_color="white")
        self.LabelMoshakhasat.place(x=0, y=0)
        
        self.lblcode = ctk.CTkLabel(self.Frame2_2, text=" :کد کفش", font=("b nazanin", 20),
                                    text_color="white")
        self.lblcode.place(x=350, y=40)
        
        self.txtcode = ctk.CTkEntry(self.Frame2_2, width=200, height=20, font=("b nazanin", 15, "bold"), justify="right")
        self.txtcode.place(x=100, y=45)
        
        self.lblcolor = ctk.CTkLabel(self.Frame2_2, text=" :رنگ کفش", font=("b nazanin", 20),
                                    text_color="white")
        self.lblcolor.place(x=350, y=77)
        
        self.txtcolor = ctk.CTkEntry(self.Frame2_2, width=200, height=20, font=("b nazanin", 15, "bold"), justify="right")
        self.txtcolor.place(x=100, y=82)
        
        self.lblgender = ctk.CTkLabel(self.Frame2_2, text=" :Gender", font=("b nazanin", 20),
                                    text_color="white")
        self.lblgender.place(x=350, y=120)
        
        self.txtgender = ctk.CTkEntry(self.Frame2_2, width=200, height=20, font=("b nazanin", 15, "bold"), justify="right")
        self.txtgender.place(x=100, y=120)
        
        self.btnsearch = ctk.CTkButton(self.Frame2_2, text="جستجو", width=200, height=35, fg_color="#205a75",
                                       text_color="white", font=("b nazanin", 18, "bold"), border_width=2,
                                       border_color="white", command=self.search_data)
        self.btnsearch.place(x=100, y=155)
        
        # ---------------------------------------------------------------------------------------------------------------
        
        self.Frame3 = ctk.CTkFrame(self, width=1000, height=60, fg_color="#3283a8")
        self.Frame3.pack(padx=5, pady=5)
        
        self.btn_Delete = ctk.CTkButton(self.Frame3, text="حذف محصول", width=250, height=35, fg_color="#fc9132",
                                       text_color="white", font=("b nazanin", 18, "bold"), border_width=2,
                                       border_color="white", state='disabled', command=self.Delete)
        self.btn_Delete.place(x=40, y=8)
        
        self.Anbar_all = ctk.CTkButton(self.Frame3, text="نمایش همه موارد", width=250, height=35, fg_color="#fc9132",
                                       text_color="white", font=("b nazanin", 18, "bold"), border_width=2,
                                       border_color="white", command=self.Anbar)
        self.Anbar_all.place(x=370, y=8)
        
        self.btn_back = ctk.CTkButton(self.Frame3, text="بازگشت", width=250, height=35, fg_color="#fc9132",
                                       text_color="white", font=("b nazanin", 18, "bold"), border_width=2,
                                       border_color="white", command=self.back)
        self.btn_back.place(x=700, y=8)
        
        # --------------------------------------------------- FRAME 3 ---------------------------------------------------
        self.Frame4 = ctk.CTkFrame(self, fg_color="#3283a8")
        self.Frame4.pack(padx=5, pady=5)
        
        self.scrolbar = Scrollbar(self.Frame4)
        self.scrolbar.pack(side="right", fill="y")
        
        self.table = ttk.Treeview(self.Frame4, columns=("1", "2", "3", "4", "5", "6"),
                                  show="headings", height=15, yscrollcommand=self.scrolbar.set)
        self.table.pack(side='right', fill='y', padx=5, pady=5)
        
        self.scrolbar.config(command=self.table.yview)

        self.table.column("# 1", width=160, anchor="center")
        self.table.heading("# 1", text="قیمت", anchor="center")

        self.table.column("# 2", width=160, anchor="center")
        self.table.heading("# 2", text="تعداد", anchor="center")
        
        self.table.column("# 3", width=160, anchor="center")
        self.table.heading("# 3", text="سایز", anchor="center")

        self.table.column("# 4", width=160, anchor="center")
        self.table.heading("# 4", text="Gender", anchor="center")

        self.table.column("# 5", width=160, anchor="center")
        self.table.heading("# 5", text="رنگ", anchor="center")
        
        self.table.column("# 6", width=160, anchor="center")
        self.table.heading("# 6", text="کد کالا", anchor="center")
        
        self.table.bind("<Button-1>", self.GetSelection)
    
    
    def back(self):
        from Start import Start
        
        self.destroy()
        app = Start()
        app.mainloop()
    
    def GetSelection(self, event):
        self.Cleartxt()
        self.btn_Delete.configure(state='normal')
        selection_row = self.table.selection()
        
        if selection_row != ():
            
            self.btnEdit.configure(state='normal')
        
            code_kafsh = self.table.item(selection_row)["values"][5]
            color = self.table.item(selection_row)["values"][4]
            gender = self.table.item(selection_row)["values"][3]
            size = self.table.item(selection_row)["values"][2]
            count = self.table.item(selection_row)["values"][1]
            price = self.table.item(selection_row)["values"][0]
        
            self.txtbox_Id.insert(0, code_kafsh)
            self.txtbox_color.insert(0, color)
            self.txtbox_gender.set(gender)
            self.txtbox_size.insert(0, size)
            self.txtbox_count.insert(0, count)
            self.txtbox_price.insert(0, price)
    
    def Edit(self):
        selection_row = self.table.selection()
        
        code_kafsh = self.table.item(selection_row)["values"][5]
        color = self.table.item(selection_row)["values"][4]
        gender = self.table.item(selection_row)["values"][3]
        size = self.table.item(selection_row)["values"][2]
        count = self.table.item(selection_row)["values"][1]
        price = self.table.item(selection_row)["values"][0]
        
        self.my_cursor.execute(f"SELECT * FROM anbar WHERE code_kafsh = '{code_kafsh}' AND color = '{color}' AND gender = '{gender}' AND size = {size} AND count = {count} AND price = {price};")
        Id = 0
        for i in self.my_cursor:
            Id = i[0]
        
        
        new_code_kafsh, new_color, new_gender, new_size, new_count, new_price = self.txtbox_Id.get(), self.txtbox_color.get(), self.txtbox_gender.get(), self.txtbox_size.get(), self.txtbox_count.get(), self.txtbox_price.get()
    
        self.my_cursor.execute(f"UPDATE Anbar SET code_kafsh = '{new_code_kafsh}' , color = '{new_color}' , gender = '{new_gender}' , size = {new_size} , count = {new_count} , price = {new_price} WHERE id = {Id};")
        self.db.commit()
        self.Cleartxt()
        self.Anbar()
        
        self.btn_Delete.configure(state='disable')
        self.btnEdit.configure(state='disable')
        tkinter.messagebox.showinfo("SUBMIT", "دیتا با موفقیت ویرایش شد")
        
        self.txtbox_Id.configure(placeholder_text="کد را وارد کنید")
        self.txtbox_color.configure(placeholder_text="رنگ را وارد کنید")
        self.txtbox_size.configure(placeholder_text="سایز را وارد کنید")
        self.txtbox_count.configure(placeholder_text="تعداد را وارد کنید")
        self.txtbox_price.configure(placeholder_text="قیمت را وارد کنید")
    
    def search_data(self):
        code_kafsh = self.txtcode.get()
        color = self.txtcolor.get()
        gender = self.txtgender.get()
        
        if code_kafsh == "" and color == "" and gender == "":
            tkinter.messagebox.showerror("Error", "لطفا یکی از باکس هارا پر کنید")
        else:
            if code_kafsh != "" and color == "" and gender == "":
                self.my_cursor.execute(f"SELECT * FROM anbar WHERE code_kafsh = '{code_kafsh}';")
            elif code_kafsh != "" and color != "" and gender == "":
                self.my_cursor.execute(f"SELECT * FROM anbar WHERE code_kafsh = '{code_kafsh}' AND color = '{color}';")
            elif code_kafsh != "" and color == "" and gender != "":
                self.my_cursor.execute(f"SELECT * FROM anbar WHERE code_kafsh = '{code_kafsh}' AND gender = '{gender}';")
            elif code_kafsh != "" and color != "" and gender != "":
                self.my_cursor.execute(f"SELECT * FROM anbar WHERE code_kafsh = '{code_kafsh}' AND color = '{color}' AND gender = '{gender}';")
            elif code_kafsh == "" and color != "" and gender == "":
                self.my_cursor.execute(f"SELECT * FROM anbar WHERE color = '{color}';")
            elif code_kafsh == "" and color != "" and gender != "":
                self.my_cursor.execute(f"SELECT * FROM anbar WHERE color = '{color}' AND gender = '{gender}';")
            elif code_kafsh == "" and color == "" and gender != "":
                self.my_cursor.execute(f"SELECT * FROM anbar WHERE gender = '{gender}';")
            
            self.ClearTabel()
            
            count = 0
            for i in self.my_cursor:
                code_kafsh, color, gender, size, count, price = i[1], i[2], i[3], i[4], i[5], i[6]
                self.table.insert('', "end", text="1", value=[price, count, size, gender, color, code_kafsh])
                count += 1
            
            if count == 0:
                tkinter.messagebox.showerror("ERROR", "این مورد وجود ندارد")
            else:
                self.txtcode.delete(0, ctk.END)
                self.txtcolor.delete(0, ctk.END)
                self.txtgender.delete(0, ctk.END)
        
        
    def Cleartxt(self):
        for item in [self.txtbox_Id, self.txtbox_color, self.txtbox_size, self.txtbox_count, self.txtbox_price]:
            item.delete(0, ctk.END)
        self.txtbox_Id.focus_set()
        
        self.btnEdit.configure(state='disable')
        
        self.txtbox_Id.configure(placeholder_text="کد را وارد کنید")
        self.txtbox_color.configure(placeholder_text="رنگ را وارد کنید")
        self.txtbox_size.configure(placeholder_text="سایز را وارد کنید")
        self.txtbox_count.configure(placeholder_text="تعداد را وارد کنید")
        self.txtbox_price.configure(placeholder_text="قیمت را وارد کنید")
    
    def ClearTabel(self):
        for row in self.table.get_children():
            self.table.delete(row)
    
    def Check(self, id, color, gender, size, count, price):
        if id == "" or color == "" or gender == "" or size == "" or count == "" or price == "":
            return False
        return True
    
    def Anbar(self):
        self.ClearTabel()
        self.my_cursor.execute("SELECT * FROM anbar")
        for i in self.my_cursor:
            code_kafsh, color, gender, size, count, price = i[1], i[2], i[3], i[4], i[5], i[6]
            self.table.insert('', "end", text="1", value=[price, count, size, gender, color, code_kafsh])
    
    def Submit(self):
        code_kafsh, color, gender, size, count, price = self.txtbox_Id.get(), self.txtbox_color.get(), self.txtbox_gender.get(), self.txtbox_size.get(), self.txtbox_count.get(), self.txtbox_price.get()
        if self.Check(id, color, gender, size, count, price):
            self.my_cursor.execute(f"INSERT INTO anbar (code_kafsh, color, gender, size, count, price) VALUES ('{code_kafsh}', '{color}', '{gender}', {size}, {count}, {price});")
            self.db.commit()
            tkinter.messagebox.showinfo("Submit", "محصول با موفقیت اضافه شد")
            self.Cleartxt()
            self.Anbar()
        else:
            tkinter.messagebox.showerror("Error", "لطفا باکس مربوط را پر کنید")
        
    def Delete(self):
        qustion = tkinter.messagebox.askyesno("سوال", "آیا از حذف شدن دیتا مطمئن هستید؟")
        if qustion:
            selection_row = self.table.selection()
            if selection_row != ():
                
                code_kafsh = self.table.item(selection_row)["values"][5]
                color = self.table.item(selection_row)["values"][4]
                gender = self.table.item(selection_row)["values"][3]
                
                self.my_cursor.execute(f"DELETE FROM anbar WHERE code_kafsh = '{code_kafsh}' AND color = '{color}' AND gender = '{gender}';")
                self.db.commit()
                tkinter.messagebox.showinfo("Delete", "محصول با موفقیت حذف شد")
                self.btn_Delete.configure(state='disable')
                self.Anbar()
                self.Cleartxt()
                self.txtbox_Id.configure(placeholder_text="کد را وارد کنید")
                self.txtbox_color.configure(placeholder_text="رنگ را وارد کنید")
                self.txtbox_size.configure(placeholder_text="سایز را وارد کنید")
                self.txtbox_count.configure(placeholder_text="تعداد را وارد کنید")
                self.txtbox_price.configure(placeholder_text="قیمت را وارد کنید")
            else:
                tkinter.messagebox.showerror("Error", "لطفا یکی از موارد تیبل را سلکت کنید")
        