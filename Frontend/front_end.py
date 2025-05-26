import tkinter as tk
from tkinter import ttk
import customtkinter
from datetime import date
import subprocess
import os
import webbrowser
import time

today = date.today()
today_str = today.isoformat()

def Mainapp():
    def run_server():
        app_path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Wampserver64\Wampserver64.lnk'
        subprocess.Popen(app_path, shell=True)
        time.sleep(15)
        webbrowser.open(f"http://tenderhunt/home.html")

    global c
    c = True

    def toggle_mode():
        global c
        if c:
            customtkinter.set_appearance_mode("light")
            customtkinter.set_default_color_theme("dark-blue")
            app.mode = "light"
            text_widget2.configure(bg="white", fg="black")
            c = False
        else:
            customtkinter.set_appearance_mode("dark")
            customtkinter.set_default_color_theme("dark-blue")
            app.mode = "dark"
            text_widget2.configure(bg="#1b1b1b", fg="white")
            c = True

    def update_data():
        update_text_text = update_text.get()
        pathgever(update_text_text)

    def pathgever(selected_value):
        path_selected = selected_value
        if path_selected == 'Tender found':
            text_file_path = "FIND_T_path"
        elif path_selected == 'ND Tender':
            text_file_path = "ND_FIND_T_path"
        elif path_selected == 'Log':
            text_file_path = "log_path"
        file_contents = load_file(text_file_path)
        text_widget2.configure(state="normal")
        text_widget2.delete("1.0", "end")
        text_widget2.insert("1.0", file_contents)
        text_widget2.configure(state="disabled")

    def load_file(file_path):
        return f"Displaying content from: {file_path}"

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("dark-blue")
    app = customtkinter.CTk()
    app.title("Auto Tender Finder")
    app.resizable(False, False)

    app_frame1 = customtkinter.CTkFrame(master=app)
    app_frame1.grid(row=0, column=0, padx=20, pady=20, sticky="we")

    # Website and Product Dropdowns
    Name_list = ['readData()']
    SearchKeywords_list = ["SearchKeywords()"]

    web_product = customtkinter.CTkFrame(master=app_frame1)
    web_product.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

    web_lab = customtkinter.CTkLabel(web_product, text="WEBSITE", fg_color="transparent")
    web_lab.grid(row=0, column=0, pady=(10, 0))
    website = customtkinter.CTkOptionMenu(web_product, values=Name_list, width=250)
    website.grid(row=1, column=0, padx=20, pady=(0, 10), sticky="ew")
    website.set(Name_list[0])

    prou_labe = customtkinter.CTkLabel(web_product, text="PRODUCT", fg_color="transparent")
    prou_labe.grid(row=0, column=1, pady=(10, 0))
    product = customtkinter.CTkOptionMenu(web_product, values=SearchKeywords_list, width=250)
    product.grid(row=1, column=1, padx=20, pady=(0, 10), sticky="ew")
    product.set(SearchKeywords_list[0])

    # Buttons
    but_con = customtkinter.CTkFrame(master=app_frame1)
    but_con.grid(row=0, column=1, padx=(0, 20), pady=20, sticky="ew")

    browser_oppen = customtkinter.CTkButton(but_con, text="Browser", command=run_server, width=150)
    browser_oppen.grid(row=0, column=0, padx=(5, 0), pady=10, sticky="w")

    toggle_button = customtkinter.CTkButton(but_con, text="Toggle", command=toggle_mode, width=150)
    toggle_button.grid(row=0, column=1, padx=(5, 0), pady=10, sticky="e")

    su_bu = customtkinter.CTkButton(but_con, text="Search", width=305)
    su_bu.grid(row=1, column=0, columnspan=2, pady=(0, 10), padx=5, sticky="ew")

    # Bottom Frame (Text + Treeview)
    app_frame3 = customtkinter.CTkFrame(master=app)
    app_frame3.grid(row=2, column=0, padx=20, pady=(0, 20), sticky="nsew")

    # Top controls for file loading
    update_button = customtkinter.CTkButton(app_frame3, text="Update Data", command=update_data, width=130)
    update_button.grid(row=0, column=1, padx=10, pady=(20, 0), sticky="e")

    update_text = customtkinter.CTkOptionMenu(app_frame3, values=['Tender found', 'ND Tender', 'Log'],
                                              width=190, command=pathgever)
    update_text.grid(row=0, column=0, padx=20, pady=(20, 0), sticky="w")

    # Text widget
    text_widget2 = tk.Text(app_frame3, wrap=tk.WORD, height=10, width=140)
    text_widget2.grid(row=1, column=0, columnspan=2, padx=20, pady=(10, 10), sticky="ew")

    text_file_path = "FIND_T_path"
    file_contents = load_file(text_file_path)
    text_widget2.configure(bg="#1b1b1b", fg="white")
    text_widget2.insert("1.0", file_contents)
    text_widget2.configure(state="disabled")

    # Table with scrollbars
    columns = [
        "id", "date_of_search", "tender_id", "element_put", "item_description",
        "qty", "start_date", "end_date", "end_time", "day_left_formula",
        "emd_amount", "tender_value", "item_category", "consignee_reporting",
        "address", "ministry", "department", "branch", "matches", "matched_products"
    ]


    tree_scroll_y = tk.Scrollbar(app_frame3, orient="vertical")
    tree_scroll_y.grid(row=2, column=2, sticky="ns", pady=(0, 20))

    tree_scroll_x = tk.Scrollbar(app_frame3, orient="horizontal")
    tree_scroll_x.grid(row=3, column=0, columnspan=2, sticky="ew", padx=20)

    tree = ttk.Treeview(app_frame3, columns=columns, show="headings",
                        yscrollcommand=tree_scroll_y.set,
                        xscrollcommand=tree_scroll_x.set)
    tree.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew")

    tree_scroll_y.config(command=tree.yview)
    tree_scroll_x.config(command=tree.xview)

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=20, anchor="w")












    for row in sample_data:
        tree.insert("", "end", values=row)

    toggle_mode()
    app.mainloop()

Mainapp()


