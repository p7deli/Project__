import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3


class AnbarForosh(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry("%dx%d+%d+%d" % (965, 700, 200, 10))
        self.iconbitmap("icons\warehouse.ico")
        self.title("انبار فروش")
        self.resizable(False, False)
        
        self.db = sqlite3.connect("Shoe_stores.db")
        self.my_cursor = self.db.cursor()
        
        self.frame1 = ctk.CTkFrame(self, width=950, height=60, fg_color="#5d9476")
        self.frame1.pack(padx=5, pady=5)
        
        self.lbl_f1 = ctk.CTkLabel(self.frame1, text="انبار فروش", font=("b nazanin", 30, "bold"), width=940, height=50,
                                   text_color="white", fg_color="#5d9476")
        self.lbl_f1.pack(padx=5, pady=5)
        
        # ---------------------------------------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------
        
        self.frame2 = ctk.CTkFrame(self, width=950, height=150, fg_color="#5d9476")
        self.frame2.pack(padx=5, pady=5)
        
        self.lbltarikh1 = ctk.CTkLabel(self.frame2, text=":از تاریخ", font=("b nazanin", 20, "bold"), text_color="white")
        self.lbltarikh1.place(x=750, y=5)

        options_tarikh = [
            [str(num) for num in range(1, 32)],
            [str(num) for num in range(1, 13)],
            [str(num) for num in range(1402, 1450)]
        ]
        
        self.box_roz1 = ctk.CTkComboBox(self.frame2, width=60, font=("b nazanin", 15, "bold"), values=options_tarikh[0])
        self.box_roz1.place(x=750, y=40)
        
        self.box_mah1 = ctk.CTkComboBox(self.frame2, width=100, font=("b nazanin", 15, "bold"), values=options_tarikh[1])
        self.box_mah1.place(x=630, y=40)
        
        self.box_sal1 = ctk.CTkComboBox(self.frame2, width=100, font=("b nazanin", 15, "bold"), values=options_tarikh[2])
        self.box_sal1.place(x=520, y=40)
        
        
        self.lbltarikh2 = ctk.CTkLabel(self.frame2, text=":تا تاریخ", font=("b nazanin", 20, "bold"), text_color="white")
        self.lbltarikh2.place(x=350, y=5)
        
        self.box_roz2 = ctk.CTkComboBox(self.frame2, width=60, font=("b nazanin", 15, "bold"), values=options_tarikh[0])
        self.box_roz2.place(x=350, y=40)
        
        self.box_mah2 = ctk.CTkComboBox(self.frame2, width=100, font=("b nazanin", 15, "bold"), values=options_tarikh[1])
        self.box_mah2.place(x=230, y=40)
        
        self.box_sal2 = ctk.CTkComboBox(self.frame2, width=100, font=("b nazanin", 15, "bold"), values=options_tarikh[2])
        self.box_sal2.place(x=120, y=40)
        
        self.btn_search = ctk.CTkButton(self.frame2, text="جستجو", font=("b nazanin", 20, "bold"), width=290,
                                  fg_color="#6b6967", border_color="white", border_width=3, command=self.Anbar,
                                  text_color="white")
        self.btn_search.place(x=310, y=90)

        # ---------------------------------------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------
        
        self.frame3 = ctk.CTkFrame(self, width=950, height=900, fg_color="#5d9476")
        self.frame3.pack(padx=5, pady=5)
        
        self.scrolbar = Scrollbar(self.frame3)
        self.scrolbar.pack(side="right", fill="y")
        
        self.table = ttk.Treeview(self.frame3, columns=("1", "2", "3", "4", "5", "6", "7"),
                                  show="headings", height=15, yscrollcommand=self.scrolbar.set)
        self.table.pack(side='right', fill='y', padx=6, pady=6)
        
        self.scrolbar.config(command=self.table.yview)
        
        self.table.column("# 1", width=130, anchor="center")
        self.table.heading("# 1", text="تاریخ", anchor="center")

        self.table.column("# 2", width=130, anchor="center")
        self.table.heading("# 2", text="قیمت", anchor="center")

        self.table.column("# 3", width=130, anchor="center")
        self.table.heading("# 3", text="تعداد", anchor="center")
        
        self.table.column("# 4", width=130, anchor="center")
        self.table.heading("# 4", text="سایز", anchor="center")

        self.table.column("# 5", width=130, anchor="center")
        self.table.heading("# 5", text="Gender", anchor="center")

        self.table.column("# 6", width=130, anchor="center")
        self.table.heading("# 6", text="رنگ", anchor="center")
        
        self.table.column("# 7", width=130, anchor="center")
        self.table.heading("# 7", text="کد کالا", anchor="center")
        
        self.table.bind("<Button-1>", self.GetSelection)
        
        # ---------------------------------------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------
    
        self.frame4 = ctk.CTkFrame(self, width=940, height=50, fg_color="#5d9476")
        self.frame4.pack(padx=5, pady=5)
        
        self.lbl_jamkol = ctk.CTkLabel(self.frame4, text="جمع کل", font=("b nazanin", 20, "bold"), text_color="white")
        self.lbl_jamkol.place(x=750, y=5)
        
        self.table2 = ttk.Treeview(self.frame4, columns=("1"),
                                  show="headings", height=0)
        self.table2.place(x=10, y=10)

        self.table2.column("# 1", width=200, anchor="center")
        self.table2.heading("# 1", text="0", anchor="center")
    
        # ---------------------------------------------------------------------------------------------------------------------------
        # ---------------------------------------------------------------------------------------------------------------------------
    
        self.frame5 = ctk.CTkFrame(self, width=940, height=50, fg_color="#5d9476")
        self.frame5.pack(padx=5, pady=5)
        
        self.lbl_f5 = ctk.CTkLabel(self.frame5, text="تذکر: برای استفاده از این بخش ابتدا تاریخ را درست وارد کنید در صورت نبودن کالا در اون روز اررور میدهد", font=("b nazanin", 15, "bold"), width=940, height=50,
                                   text_color="red", fg_color="white")
        self.lbl_f5.pack(padx=5, pady=5)
        
        self.btn_back = ctk.CTkButton(self.frame5, text="بازگشت", font=("b nazanin", 17, "bold"), width=150,
                                  fg_color="#c78534", border_color="#5d9476", border_width=2, height=25, 
                                  text_color="white", command=self.back)
        self.btn_back.place(x=780, y=8)
        
    
    def GetSelection(self, event):
        selection_row = self.table.selection()
        if selection_row != ():
            Date = self.table.item(selection_row)['values'][0]
            price = self.table.item(selection_row)['values'][1]
            count = self.table.item(selection_row)['values'][2]
            size = self.table.item(selection_row)['values'][3]
            gender = self.table.item(selection_row)['values'][4]
            color = self.table.item(selection_row)['values'][5]
            code_kala = self.table.item(selection_row)['values'][6]
            
            
            def close():
                self.ClearTabel()
                self.Anbar()
                window.destroy()    
    
                
            window = ctk.CTk()
            window.geometry("%dx%d+%d+%d" % (400, 460, 500, 100))
            window.protocol("WM_DELETE_WINDOW", close)
            window.resizable(False, False)
            
            frame1 = ctk.CTkFrame(window, width=350, height=50)
            frame1.pack(padx=5, pady=5)
            
            lbl_1 = ctk.CTkLabel(frame1, text="فرم مشخصات", font=("b nazanin", 25, "bold"), width=350, height=40, 
                                    fg_color="#32a881", text_color="white")
            lbl_1.pack()
            
            frame2 = ctk.CTkFrame(window, width=350, height=350, 
                                    fg_color="#32a881")
            frame2.pack(padx=5, pady=5)
            
            lbl_count = ctk.CTkLabel(frame2, text="تعداد", font=("b nazanin", 20, "bold"), text_color="white")
            lbl_count.place(x=250, y=5)
            
            lbl_count1 = ctk.CTkLabel(frame2, text=f"{count}", font=("Arial", 20, "bold"), text_color="white")
            lbl_count1.place(x=50, y=5)
            
            lbl_1 = ctk.CTkLabel(frame2, text=f"{40*'-'}", font=("Arial", 20, "bold"), text_color="white")
            lbl_1.place(x=30, y=30)
            
            lbl_price = ctk.CTkLabel(frame2, text="قیمت", font=("b nazanin", 20, "bold"), text_color="white")
            lbl_price.place(x=250, y=50)
            
            lbl_price1 = ctk.CTkLabel(frame2, text=f"{price}", font=("Arial", 20, "bold"), text_color="white")
            lbl_price1.place(x=50, y=50)
            
            lbl_1 = ctk.CTkLabel(frame2, text=f"{40*'-'}", font=("Arial", 20, "bold"), text_color="white")
            lbl_1.place(x=30, y=75)
            
            lbl_date = ctk.CTkLabel(frame2, text="تاریخ", font=("b nazanin", 20, "bold"), text_color="white")
            lbl_date.place(x=250, y=100)
            
            lbl_date1 = ctk.CTkLabel(frame2, text=f"{Date}", font=("Arial", 20, "bold"), text_color="white")
            lbl_date1.place(x=50, y=100)
            
            lbl_1 = ctk.CTkLabel(frame2, text=f"{40*'-'}", font=("Arial", 20, "bold"), text_color="white")
            lbl_1.place(x=30, y=125)
            
            lbl_color = ctk.CTkLabel(frame2, text="رنگ", font=("b nazanin", 20, "bold"), text_color="white")
            lbl_color.place(x=250, y=150)
            
            lbl_color1 = ctk.CTkLabel(frame2, text=f"{color}", font=("b nazanin", 20, "bold"), text_color="white")
            lbl_color1.place(x=50, y=150)
            
            lbl_1 = ctk.CTkLabel(frame2, text=f"{40*'-'}", font=("Arial", 20, "bold"), text_color="white")
            lbl_1.place(x=30, y=175)
            
            lbl_gender = ctk.CTkLabel(frame2, text="جنسیت", font=("b nazanin", 20, "bold"), text_color="white")
            lbl_gender.place(x=250, y=200)
            
            lbl_gender1 = ctk.CTkLabel(frame2, text=f"{gender}", font=("b nazanin", 20, "bold"), text_color="white")
            lbl_gender1.place(x=50, y=200)
            
            lbl_1 = ctk.CTkLabel(frame2, text=f"{40*'-'}", font=("Arial", 20, "bold"), text_color="white")
            lbl_1.place(x=30, y=225)
            
            lbl_code = ctk.CTkLabel(frame2, text="کد کالا", font=("b nazanin", 20, "bold"), text_color="white")
            lbl_code.place(x=250, y=250)
            
            lbl_code1 = ctk.CTkLabel(frame2, text=f"{code_kala}", font=("Arial", 20, "bold"), text_color="white")
            lbl_code1.place(x=50, y=250)
            
            lbl_1 = ctk.CTkLabel(frame2, text=f"{40*'-'}", font=("Arial", 20, "bold"), text_color="white")
            lbl_1.place(x=30, y=275)
            
            lbl_code = ctk.CTkLabel(frame2, text="جمع کل", font=("b nazanin", 20, "bold"), text_color="white")
            lbl_code.place(x=250, y=300)
            
            lbl_code1 = ctk.CTkLabel(frame2, text=f"{int(count)*int(str(price).replace(',', '')):,}", font=("Arial", 20, "bold"), text_color="white")
            lbl_code1.place(x=50, y=300)
            
            btn = ctk.CTkButton(window, text="بستن", font=("b nazanin", 20, "bold"), width=350, height=40, fg_color="#04472f",
                                command=close)
            btn.pack()
            
            window.mainloop()
                
    
    def back(self):
        from Start import Start
        
        self.destroy()
        app = Start()
        app.mainloop()
        
    def ClearTabel(self):
        for row in self.table.get_children():
            self.table.delete(row)
    
    def Anbar(self):
        self.ClearTabel()
        sal1, mah1, roz1 = self.box_sal1.get(), self.box_mah1.get(), self.box_roz1.get()
        sal2, mah2, roz2 = self.box_sal2.get(), self.box_mah2.get(), self.box_roz2.get()
        date1 = f"{sal1}-{mah1}-{roz1}"
        date2 = f"{sal2}-{mah2}-{roz2}"
        self.my_cursor.execute(f"SELECT * FROM forosh WHERE Date_forosh BETWEEN '{date1}' AND '{date2}';")
        
        List = []
        countt = 0
        for i in self.my_cursor:
            code_kafsh, color, gender, size, count, price, date = i[1], i[2], i[3], i[4], i[5], i[6], i[7]
            List.append(int(count)*int(price))
            self.table.insert('', "end", text="1", value=[date, f"{price:,}", count, size, gender, color, code_kafsh])
            countt += 1
        
        if countt == 0:
            messagebox.showerror("Error", "موردی یافت نشد")

        self.table2.heading("# 1", text=f"{sum(List):,}", anchor="center")


def main():
    app = AnbarForosh()
    app.mainloop()


if __name__ == "__main__":
    main()