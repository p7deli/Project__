import customtkinter as ctk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import jdatetime


class Forosh(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("%dx%d+%d+%d" % (965, 700, 200, 10))
        self.title("بخش فروش")
        self.iconbitmap("icons\sale.ico")
        self.resizable(False, False)

        self.db = sqlite3.connect("Shoe_stores.db")
        self.my_cursor = self.db.cursor()

        # ------------------------------------------------------------ FORM 1 ---------------------------------------------------------

        self.frame1 = ctk.CTkFrame(self, width=950, height=70, fg_color="#a1b4f7")
        self.frame1.pack(pady=3)

        self.lbl_tarafHesab = ctk.CTkLabel(self.frame1, text=":طرف حساب", font=("b nazanin", 17, "bold"),
                                           text_color="black")
        self.lbl_tarafHesab.place(x=800, y=5)

        self.lbltarikh = ctk.CTkLabel(self.frame1, text=":تاریخ", font=("b nazanin", 17, "bold"), text_color="black")
        self.lbltarikh.place(x=600, y=5)

        options_tarikh = [
            ["متفرقه"],
            [str(num) for num in range(1, 32)],
            [str(num) for num in range(1, 13)],
            [str(num) for num in range(1402, 1450)]
        ]

        self.box_tarafhesab = ctk.CTkComboBox(self.frame1, width=200, font=("b nazanin", 15, "bold"),
                                              values=options_tarikh[0])
        self.box_tarafhesab.place(x=680, y=35)

        self.box_roz = ctk.CTkComboBox(self.frame1, width=60, font=("Arial", 15, "bold"), values=options_tarikh[1])
        self.box_roz.place(x=580, y=35)

        self.box_mah = ctk.CTkComboBox(self.frame1, width=100, font=("Arial", 15, "bold"), values=options_tarikh[2])
        self.box_mah.place(x=460, y=35)

        self.box_sal = ctk.CTkComboBox(self.frame1, width=100, font=("Arial", 15, "bold"), values=options_tarikh[3])
        self.box_sal.place(x=350, y=35)

        fa_date = str(jdatetime.date.today()).split("-")
        self.box_sal.set(str(int(fa_date[0])))
        self.box_mah.set(str(int(fa_date[1])))
        self.box_roz.set(str(int(fa_date[2])))

        # -----------------------------------------------------------------------------------------------------------------------------
        # ------------------------------------------------------------ FORM 2 ---------------------------------------------------------

        self.frame2 = ctk.CTkFrame(self, fg_color="#a1b4f7")
        self.frame2.pack(padx=10)

        self.frame2_1 = ctk.CTkFrame(self.frame2, height=50, width=950, fg_color="#a1b4f7")
        self.frame2_1.pack(pady=5, padx=5)

        self.search_entry_kala = ctk.CTkEntry(self.frame2_1, placeholder_text="کد کفش را وارد کنید",
                                              width=300, height=40, font=("Arial", 17, "bold"),
                                              justify=CENTER)
        self.search_entry_kala.place(x=400, y=5)

        self.search_btn_kala = ctk.CTkButton(self.frame2_1, text="جستجو", width=150, height=35,
                                             font=("Arial", 15, "bold"),
                                             fg_color="#645f66", bg_color="white", border_color="white", border_width=2,
                                             text_color="white", command=self.search_kala)
        self.search_btn_kala.place(x=240, y=8)

        self.scrollbar = Scrollbar(self.frame2, width=20)
        self.scrollbar.pack(side="right", fill="y")

        self.canvas = Canvas(self.frame2, yscrollcommand=self.scrollbar.set, width=950)
        self.canvas.pack(side="left", fill="both", expand=True)

        self.inner_frame = ctk.CTkFrame(self.canvas, width=950, height=2000, fg_color="white")
        self.scrollbar.config(command=self.canvas.yview)

        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.inner_frame.bind("<Configure>", lambda event: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        # -----------------------------------------------------------------------------------------------------------------------------
        # ------------------------------------------------------------ FORM 3 ---------------------------------------------------------

        self.frame3 = ctk.CTkFrame(self, width=950, height=110, fg_color="#a1b4f7")
        self.frame3.pack(padx=5, pady=5)

        self.table1 = ttk.Treeview(self.frame3, columns=("1", "2", "3", "4", "5", "6", "7", "8", "9"),
                                   show="headings", height=7)
        self.table1.pack(pady=5, padx=5)

        self.table1.column("# 1", width=110, anchor="center")
        self.table1.heading("# 1", text="قیمت کل با مالیات", anchor="center")

        self.table1.column("# 2", width=110, anchor="center")
        self.table1.heading("# 2", text="مالیات", anchor="center")

        self.table1.column("# 3", width=110, anchor="center")
        self.table1.heading("# 3", text="قیمت کل با تخفیف", anchor="center")

        self.table1.column("# 4", width=110, anchor="center")
        self.table1.heading("# 4", text="تخفیف", anchor="center")

        self.table1.column("# 5", width=110, anchor="center")
        self.table1.heading("# 5", text="قیمت کل", anchor="center")

        self.table1.column("# 6", width=110, anchor="center")
        self.table1.heading("# 6", text="قیمت", anchor="center")

        self.table1.column("# 7", width=110, anchor="center")
        self.table1.heading("# 7", text="تعداد", anchor="center")

        self.table1.column("# 8", width=80, anchor="center")
        self.table1.heading("# 8", text="id", anchor="center")

        self.table1.column("# 9", width=80, anchor="center")
        self.table1.heading("# 9", text="ردیف", anchor="center")

        # -----------------------------------------------------------------------------------------------------------------------------
        # ------------------------------------------------------------ FORM 4 ---------------------------------------------------------

        self.frame4 = ctk.CTkFrame(self, width=950, height=40, fg_color="#a1b4f7")
        self.frame4.pack(padx=5, pady=5)

        self.lbl_jamkol = ctk.CTkLabel(self.frame4, text="جمع کل", font=("b nazanin", 20, "bold"), text_color="white")
        self.lbl_jamkol.place(x=750, y=5)

        self.table2 = ttk.Treeview(self.frame4, columns=("1", "2", "3", "4", "5"),
                                   show="headings", height=0)
        self.table2.place(x=5, y=7)

        self.table2.column("# 1", width=110, anchor="center")
        self.table2.heading("# 1", text="0", anchor="center")

        self.table2.column("# 2", width=110, anchor="center")
        self.table2.heading("# 2", text="0", anchor="center")

        self.table2.column("# 3", width=110, anchor="center")
        self.table2.heading("# 3", text="0", anchor="center")

        self.table2.column("# 4", width=110, anchor="center")
        self.table2.heading("# 4", text="0", anchor="center")

        self.table2.column("# 5", width=110, anchor="center")
        self.table2.heading("# 5", text="0", anchor="center")

        # -----------------------------------------------------------------------------------------------------------------------------
        # ------------------------------------------------------------ FORM 5 ---------------------------------------------------------

        self.frame5 = ctk.CTkFrame(self, width=950, height=50, fg_color="#a1b4f7")
        self.frame5.pack()

        self.btn1 = ctk.CTkButton(self.frame5, text="حذف", width=120, height=30, font=("b nazanin", 15, "bold"),
                                  fg_color="#db2144", bg_color="white", border_color="white", border_width=3,
                                  command=self.delete_select)
        self.btn1.place(x=800, y=10)

        self.btn3 = ctk.CTkButton(self.frame5, text="ثبت نهایی", width=120, height=30, font=("b nazanin", 15, "bold"),
                                  fg_color="#458205", bg_color="white", border_color="white", border_width=3,
                                  command=self.end_sub)
        self.btn3.place(x=670, y=10)

        self.btn4 = ctk.CTkButton(self.frame5, text="بازگشت", width=120, height=30, font=("b nazanin", 15, "bold"),
                                  fg_color="#9e840e", bg_color="white", border_color="white", border_width=3,
                                  command=self.back, text_color="white")
        self.btn4.place(x=20, y=10)

        self.buttons = []

    def back(self):
        from Start import Start

        self.destroy()
        app = Start()
        app.mainloop()

    def search_kala(self):

        for button in self.buttons:
            button.destroy()

        s = self.search_entry_kala.get()
        x = 30
        y = 7
        count = 0

        self.my_cursor.execute(f"SELECT * FROM anbar WHERE code_kafsh = '{s}';")
        for item in self.my_cursor:

            self.btn = ctk.CTkButton(self.inner_frame, text=f"{str(item[1])} - {item[3]} - {item[2]} - {item[4]}",
                                     fg_color="#d06ffc"
                                     , text_color="white", border_width=2, border_color="#cf4bfa", height=50,
                                     font=("Arial", 20, "bold")
                                     , width=200, command=lambda x=item[0]: self.result(x))
            self.buttons.append(self.btn)
            self.btn.place(x=x, y=y)

            count += 1
            x += 220

            if count == 4:
                y += 65
                x = 30
                count = 0

    def result(self, x):

        price, count, Id = 0, 0, ""

        self.my_cursor.execute(f"SELECT * FROM anbar WHERE id = {int(x)};")
        for item in self.my_cursor:
            price, count, Id = item[6], item[5], item[0]

        def Sub():
            radif = len(self.table1.get_children()) + 1
            Id_ = Id
            countt = txt_count.get()
            pricee = price
            price_all = str(int(pricee) * int(countt))
            takhfif = txt_off.get()
            if takhfif == "":
                takhfif = 0
                price_all_by_takhfif = str(int(price_all) - 0)
            else:
                takhfif = txt_off.get()
                price_all_by_takhfif = str(int(price_all) - int(takhfif))

            mal = txt_mal.get()
            if mal == "":
                mal = 6
                price_all_by_mall = str(int(int(price_all_by_takhfif) - (int(price_all_by_takhfif) * 0.06)))
            else:
                mal = txt_mal.get()
                price_all_by_mall = str(int(int(price_all_by_takhfif) - (int(price_all_by_takhfif) * int(mal) / 100)))

            if int(countt) <= int(count):
                self.table1.insert('', "end", text="1", value=[f"{int(price_all_by_mall):,}", f"{int(mal):,}",
                                                               f"{int(price_all_by_takhfif):,}", f"{int(takhfif):,}",
                                                               f"{int(price_all):,}", f"{int(pricee):,}",
                                                               f"{int(countt):,}", Id_, f"{int(radif):,}"])
                v1, v2, v3, v4, v5 = 0, 0, 0, 0, 0
                for item1 in self.table1.get_children():
                    v1 += int(str(self.table1.item(item1)['values'][0]).replace(",", ""))
                    v2 += int(str(self.table1.item(item1)['values'][1]).replace(",", ""))
                    v3 += int(str(self.table1.item(item1)['values'][2]).replace(",", ""))
                    v4 += int(str(self.table1.item(item1)['values'][3]).replace(",", ""))
                    v5 += int(str(self.table1.item(item1)['values'][4]).replace(",", ""))

                self.table2.heading("# 1", text=f"{int(v1):,}", anchor="center")
                self.table2.heading("# 2", text=f"{int(v2):,}", anchor="center")
                self.table2.heading("# 3", text=f"{int(v3):,}", anchor="center")
                self.table2.heading("# 4", text=f"{int(v4):,}", anchor="center")
                self.table2.heading("# 5", text=f"{int(v5):,}", anchor="center")

                win.destroy()
            else:
                messagebox.showerror("Error", "تعداد داده شده بیشتر از موجودی است")

        win = ctk.CTk()
        win.geometry("%dx%d+%d+%d" % (320, 270, 450, 150))

        lblcount = ctk.CTkLabel(win, text=f"تعداد مجاز {count}", font=("b nazanin", 18, "bold"))
        lblcount.pack(pady=5)

        txt_count = ctk.CTkEntry(win, width=300, height=50, placeholder_text="تعداد", font=("b nazanin", 20, "bold"))
        txt_count.pack(pady=5)

        txt_off = ctk.CTkEntry(win, width=300, height=50, placeholder_text="تخفیف", font=("b nazanin", 20, "bold"))
        txt_off.pack(pady=5)

        txt_mal = ctk.CTkEntry(win, width=300, height=50, placeholder_text="مالیات: به صورت پیش فرض %6",
                               font=("b nazanin", 20, "bold"))
        txt_mal.pack(pady=5)

        btnsub = ctk.CTkButton(win, text="ثبت", width=300, height=50, font=("b nazanin", 20, "bold"),
                               fg_color="#085e1f", bg_color="white", border_color="white", border_width=3,
                               command=Sub)
        btnsub.pack(pady=5)

        win.mainloop()

    def delete_select(self):
        selection = self.table1.selection()

        if selection != ():
            qustion = messagebox.askyesno("سوال", "آیا از حذف شدن دیتا مطمئن هستید؟")
            if qustion:
                self.table1.delete(selection)

                radif = 0
                tbl = []
                for item in self.table1.get_children():
                    tbl.append(self.table1.item(item)['values'])

                for row in self.table1.get_children():
                    self.table1.delete(row)

                count = 1
                for i in tbl:
                    self.table1.insert('', "end", text="1",
                                       value=[i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], [count]])
                    count += 1

                v1, v2, v3, v4, v5 = 0, 0, 0, 0, 0
                for item1 in self.table1.get_children():
                    v1 += int(str(self.table1.item(item1)['values'][0]).replace(",", ""))
                    v2 += int(str(self.table1.item(item1)['values'][1]).replace(",", ""))
                    v3 += int(str(self.table1.item(item1)['values'][2]).replace(",", ""))
                    v4 += int(str(self.table1.item(item1)['values'][3]).replace(",", ""))
                    v5 += int(str(self.table1.item(item1)['values'][4]).replace(",", ""))

                self.table2.heading("# 1", text=f"{int(v1):,}", anchor="center")
                self.table2.heading("# 2", text=f"{int(v2):,}", anchor="center")
                self.table2.heading("# 3", text=f"{int(v3):,}", anchor="center")
                self.table2.heading("# 4", text=f"{int(v4):,}", anchor="center")
                self.table2.heading("# 5", text=f"{int(v5):,}", anchor="center")

                messagebox.showinfo("حذف", "دیتا حذف شد")
        else:
            messagebox.showerror("Error", "لطفا یک مورد را سلکت کنید")

    def end_sub(self):
        Dic_ = {}
        price = 0

        if self.table1.get_children() != ():

            for item in self.table1.get_children():
                Dic_[self.table1.item(item)['values'][7]] = self.table1.item(item)['values'][6]
                price += int(str(self.table1.item(item)['values'][0]).replace(",", ""))

            count = 0
            for Id in Dic_.keys():
                self.my_cursor.execute(f"SELECT count FROM anbar WHERE id = {Id};")
                for i in self.my_cursor:
                    count = i[0]

                self.my_cursor.execute(f"UPDATE anbar SET count = {int(count) - int(Dic_[Id])} WHERE id = {Id};")
                self.db.commit()

            def close():
                for row in self.table1.get_children():
                    count = self.table1.item(row)['values'][6]
                    Id = self.table1.item(row)['values'][7]
                    self.my_cursor.execute(f"SELECT * FROM anbar WHERE id={Id};")
                    for kala in self.my_cursor:
                        sal = self.box_sal.get()
                        mah = self.box_mah.get()
                        roz = self.box_roz.get()
                        Date = f"{str(sal)}-{str(mah)}-{str(roz)}"
                        self.my_cursor.execute(
                            f'INSERT INTO forosh (code_kafsh, color, gender, size, count, price, Date_forosh) VALUES ("{kala[1]}", "{kala[2]}", "{kala[3]}", {kala[4]}, {int(count)}, {kala[6]}, "{Date}");')
                        self.db.commit()

                for row in self.table1.get_children():
                    self.table1.delete(row)

                self.table2.heading("# 1", text="0", anchor="center")
                self.table2.heading("# 2", text="0", anchor="center")
                self.table2.heading("# 3", text="0", anchor="center")
                self.table2.heading("# 4", text="0", anchor="center")
                self.table2.heading("# 5", text="0", anchor="center")
                win.destroy()

            win = ctk.CTk()
            win.geometry("%dx%d+%d+%d" % (370, 260, 450, 150))

            lblstart = ctk.CTkLabel(win, text="ثبت فروش", font=("b nazanin", 30, "bold"))
            lblstart.place(x=110, y=5)

            fram = ctk.CTkFrame(win, width=330, height=100)
            fram.place(x=20, y=70)

            lbltext1 = ctk.CTkLabel(fram, text=f"مبلغ کل", font=("b nazanin", 25, "bold"), text_color="red")
            lbltext1.place(x=245, y=5)

            lbltext2 = ctk.CTkLabel(fram, text=f"تاریخ", font=("b nazanin", 25, "bold"), text_color="blue")
            lbltext2.place(x=250, y=50)

            lblrial = ctk.CTkLabel(fram, text=f"ریال", font=("b nazanin", 25, "bold"), text_color="red")
            lblrial.place(x=5, y=5)

            lblpriceall = ctk.CTkLabel(fram, text=f"{price:,}", font=("b nazanin", 25, "bold"), text_color="red")
            lblpriceall.place(x=55, y=5)

            lbltarikh = ctk.CTkLabel(fram, text=f"{self.box_sal.get()}/{self.box_mah.get()}/{self.box_roz.get()}",
                                     font=("b nazanin", 25, "bold"), text_color="blue")
            lbltarikh.place(x=5, y=50)

            btnsub = ctk.CTkButton(win, text="ثبت", width=360, height=50, font=("b nazanin", 20, "bold"),
                                   fg_color="#085e1f", bg_color="white", border_color="white",
                                   border_width=3, command=close)
            btnsub.place(x=5, y=200)

            win.mainloop()
        else:
            messagebox.showerror("Error", "لطفا یک کالا انتخاب کنید")


def main():
    app = Forosh()
    app.mainloop()


if __name__ == "__main__":
    main()
