#! /usr/bin/env python
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter.ttk import *
import tkinter.ttk as ttk
# import PyTkinter as pytk
# import Adaptive


g_default_theme = "dark"
# g_default_theme = "default"

class PyButton(tk.Button):
    '''
    Button
    '''
    def __init__(self, master, theme=g_default_theme, **kv):
        self.theme = theme
        self.kv = kv
        self.temp = dict()
        self.choose_theme()
        tk.Button.__init__(self, master, self.temp)

    def choose_theme(self):
        if self.theme == "dark":
            dark_theme_dict = {
                                "activebackground": "#00B2EE",
                                "activeforeground": "#E0EEEE",
                                "bg": "#008B8B",
                                "fg": "#FFFFFF"
                              }
            for key,value in dark_theme_dict.items():
                self.temp[key] = value

            for key,value in self.kv.items():
                self.temp[key] = value

class PyLabel(tk.Label):
    '''
    Label
    '''
    def __init__(self, master, theme=g_default_theme, **kv):
        self.theme = theme
        self.kv = kv
        self.temp = dict()
        self.choose_theme()
        tk.Label.__init__(self, master, self.temp)

    def choose_theme(self):
        if self.theme == "dark":
            dark_theme_dict = {
                                "bg": "#292929",
                                "fg": "#E0EEEE"
                              }
            for key,value in dark_theme_dict.items():
                self.temp[key] = value

            for key,value in self.kv.items():
                self.temp[key] = value

class PyLabelFrame(tk.LabelFrame):
    '''
    Frame
    '''
    def __init__(self, master, theme=g_default_theme, **kv):
        self.theme = theme
        self.kv = kv
        self.temp = dict()
        self.choose_theme()
        tk.LabelFrame.__init__(self, master, self.temp)

    def choose_theme(self):
        if self.theme == "dark":
            dark_theme_dict = {
                                "bg": "#292929",
                                "fg": "#1E90FF"
                              }
            for key,value in dark_theme_dict.items():
                self.temp[key] = value

            for key,value in self.kv.items():
                self.temp[key] = value

class PyListbox(tk.Listbox):
    '''
    Listbox
    '''
    def __init__(self, master, theme=g_default_theme, **kv):
        self.theme = theme
        self.kv = kv
        self.temp = dict()
        self.choose_theme()
        tk.Listbox.__init__(self, master, self.temp)

    def choose_theme(self):
        if self.theme == "dark":
            dark_theme_dict = {
                                "bg": "#292929",
                                "fg": "#1E90FF",
                                "selectbackground": "#00B2EE"
                              }
            for key,value in dark_theme_dict.items():
                self.temp[key] = value

            for key,value in self.kv.items():
                self.temp[key] = value

class PyText(tk.Text):
    '''
    Text
    '''
    def __init__(self, master, theme=g_default_theme, **kv):
        self.theme = theme
        self.kv = kv
        self.temp = dict()
        self.choose_theme()
        tk.Text.__init__(self, master, self.temp)

    def choose_theme(self):
        if self.theme == "dark":
            dark_theme_dict = {
                                "bg": "#292929",
                                "fg": "#1E90FF"
                              }
            for key,value in dark_theme_dict.items():
                self.temp[key] = value

            for key,value in self.kv.items():
                self.temp[key] = value

class PyCheckbutton(tk.Checkbutton):
    '''
    Checkbutton
    '''
    def __init__(self, master, theme=g_default_theme, **kv):
        self.theme = theme
        self.kv = kv
        self.temp = dict()
        self.choose_theme()
        tk.Checkbutton.__init__(self, master, self.temp)

    def choose_theme(self):
        if self.theme == "dark":
            dark_theme_dict = {
                                "bg": "#292929",
                                "fg": "#FFFFFF",
                                "activebackground": "#292929",
                                "activeforeground": "#FFFFFF",
                                "selectcolor": "#292929"
                              }
            for key,value in dark_theme_dict.items():
                self.temp[key] = value

            for key,value in self.kv.items():
                self.temp[key] = value

class PyRadiobutton(tk.Radiobutton):
    '''
    Radiobutton
    '''
    def __init__(self, master, theme=g_default_theme, **kv):
        self.theme = theme
        self.kv = kv
        self.temp = dict()
        self.choose_theme()
        tk.Radiobutton.__init__(self, master, self.temp) 

    def choose_theme(self):
        if self.theme == "dark":
            dark_theme_dict = {
                                "bg": "#292929",
                                "fg": "#FFFFFF",
                                "activebackground": "#292929",
                                "selectcolor": "#292929"
                              }
            for key,value in dark_theme_dict.items():
                self.temp[key] = value

            for key,value in self.kv.items():
                self.temp[key] = value


class PyEntry(tk.Entry):
    '''
    Entry
    '''
    def __init__(self, master, theme=g_default_theme, **kv):
        self.theme = theme
        self.kv = kv
        self.temp = dict()
        self.choose_theme()
        tk.Entry.__init__(self, master, self.temp)

    def choose_theme(self):
        if self.theme == "dark":
            dark_theme_dict = {
                                "bg": "#292929",
                                "fg": "#E0EEEE",
                                "insertbackground": "#E0EEEE"
                              }
            for key,value in dark_theme_dict.items():
                self.temp[key] = value

            for key,value in self.kv.items():
                self.temp[key] = value


# font = Adaptive.monaco_font
# size_dict = Adaptive.size_dict
g_default_theme = g_default_theme

font = ('Monaco', 12)
size_dict = {   "list_box_height": 13,      \
                "send_text_height": 12,     \
                "receive_text_height": 15,  \
                "reset_label_width": 7,     \
                "clear_label_width": 5      \
            }

class SerialToolUI(object):
    def __init__(self, master=None):
        self.root = master
        self.create_frame()
        self.thresholdValue = 1

    def create_frame(self):
        '''
        新建窗口，分为上下2个部分，下半部分为状态栏
        '''
        self.frm = PyLabelFrame(self.root)
        self.frm_status = PyLabelFrame(self.root)

        self.frm.grid(row=0, column=0, sticky="wesn")
        self.frm_status.grid(row=1, column=0, sticky="wesn")

        self.create_frm()
        self.create_frm_status()

    def create_frm(self):
        '''
        上半部分窗口分为左右2个部分
        '''
        self.frm_left = PyLabelFrame(self.frm)
        self.frm_right = PyLabelFrame(self.frm)

        self.frm_left.grid(row=0, column=0, padx=5, pady=5, sticky="wesn")
        self.frm_right.grid(row=0, column=1, padx=5, pady=5, sticky="wesn")

        self.create_frm_left()
        self.create_frm_right()

    def create_frm_left(self):
        '''
        上半部分左边窗口：
        Listbox显示可用的COM口
        Button按钮点击连接设备
        '''
        self.frm_left_label = PyLabel(self.frm_left, 
                                           text="Serial Ports",
                                           font=font)
        self.frm_left_listbox = PyListbox(self.frm_left,
                                               height=size_dict["list_box_height"],
                                               font=font)
        self.frm_left_serial_set = PyLabelFrame(self.frm_left)
        self.frm_left_btn = PyButton(self.frm_left, 
                                          text="Open",
                                          font=font,
                                          command=self.Toggle)

        self.frm_left_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.frm_left_listbox.grid(row=1, column=0, padx=5, pady=5, sticky="wesn")
        self.frm_left_serial_set.grid(row=2, column=0, padx=5, pady=5, sticky="wesn")
        self.frm_left_btn.grid(row=3, column=0, padx=5, pady=5, sticky="wesn")

        self.frm_left_listbox.bind("<Double-Button-1>", self.Open)
        self.create_frm_left_serial_set()

    def create_frm_left_serial_set(self):
        '''
        串口配置，比如波特率，奇偶校验等
        '''
        setting_label_list = ["BaudRate :", "Parity :", "DataBit :", "StopBit :"]
        baudrate_list = ["1200", "2400", "4800", "9600", "14400", "19200", "38400", "43000", "57600", "76800", "115200", "12800"]
        # PARITY_NONE, PARITY_EVEN, PARITY_ODD PARITY_MARK, PARITY_SPACE
        parity_list = ["N", "E", "O", "M", "S"]
        bytesize_list = ["5", "6", "7", "8"]
        stopbits_list = ["1", "1.5", "2"]
        for index,item in enumerate(setting_label_list):
            frm_left_label_temp = PyLabel(self.frm_left_serial_set, 
                                               text=item,
                                               font=('Monaco', 10))
            frm_left_label_temp.grid(row=index, column=0, padx=1, pady=2, sticky="e")
        self.frm_left_combobox_baudrate = ttk.Combobox(self.frm_left_serial_set,
                                                       width=15,
                                                       values=baudrate_list)
        self.frm_left_combobox_parity = ttk.Combobox(self.frm_left_serial_set,
                                                       width=15,
                                                       values=parity_list)
        self.frm_left_combobox_databit = ttk.Combobox(self.frm_left_serial_set,
                                                       width=15,
                                                       values=bytesize_list)
        self.frm_left_combobox_stopbit = ttk.Combobox(self.frm_left_serial_set,
                                                       width=15,
                                                       values=stopbits_list)
        self.frm_left_combobox_baudrate.grid(row=0, column=1, padx=2, pady=2, sticky="e")
        self.frm_left_combobox_parity.grid(row=1, column=1, padx=2, pady=2, sticky="e")
        self.frm_left_combobox_databit.grid(row=2, column=1, padx=2, pady=2, sticky="e")
        self.frm_left_combobox_stopbit.grid(row=3, column=1, padx=2, pady=2, sticky="e")

        self.frm_left_combobox_baudrate.current(3)
        self.frm_left_combobox_parity.current(0)
        self.frm_left_combobox_databit.current(3)
        self.frm_left_combobox_stopbit.current(0)

    def create_frm_right(self):
        '''
        上半部分右边窗口：
        分为4个部分：
        1、Label显示和重置按钮和发送按钮
        2、Text显示（发送的数据）
        3、Label显示和十六进制选择显示和清除接收信息按钮
        4、Text显示接收到的信息
        '''
        self.frm_right_reset = PyLabelFrame(self.frm_right)
        self.frm_right_send = PyText(self.frm_right,
                                          width=50, 
                                          height=size_dict["send_text_height"],
                                          font=("Monaco", 9))
        self.frm_right_clear = PyLabelFrame(self.frm_right)
        self.frm_right_receive = PyText(self.frm_right,
                                             width=50, 
                                             height=size_dict["receive_text_height"],
                                             font=("Monaco", 9))

        self.frm_right_reset.grid(row=0, column=0, padx=1, sticky="wesn")
        self.frm_right_send.grid(row=1, column=0, padx=1, sticky="wesn")
        self.frm_right_clear.grid(row=2, column=0, padx=1, sticky="wesn")
        self.frm_right_receive.grid(row=3, column=0, padx=1, sticky="wesn")

        self.frm_right_receive.tag_config("green", foreground="#228B22")

        self.create_frm_right_reset()
        self.create_frm_right_clear()

    def create_frm_right_reset(self):
        '''
        1、Label显示和重置按钮和发送按钮
        '''
        self.frm_right_reset_label = PyLabel(self.frm_right_reset,
                                                  text="Data Send" + " "*size_dict["reset_label_width"],
                                                  font=font)
        self.new_line_cbtn_var = tk.IntVar()
        self.send_hex_cbtn_var = tk.IntVar()
        self.frm_right_reset_newLine_checkbtn = PyCheckbutton(self.frm_right_reset, text="New Line", variable=self.new_line_cbtn_var, font=font)
        self.frm_right_reset_hex_checkbtn = PyCheckbutton(self.frm_right_reset,   text="Hex",  variable=self.send_hex_cbtn_var,font=font)
        self.frm_right_reset_btn = PyButton(self.frm_right_reset, 
                                                 text="Reset",
                                                 width=10,
                                                 font=font,
                                                 command=self.Reset)
        self.frm_right_send_btn = PyButton(self.frm_right_reset, 
                                                text="Send",
                                                width=10,
                                                font=font,
                                                command=self.Send)

        self.frm_right_reset_label.grid(row=0, column=0, sticky="w")
        self.frm_right_reset_newLine_checkbtn.grid(row=0, column=1, sticky="wesn")
        self.frm_right_reset_hex_checkbtn.grid(row=0, column=2, sticky="wesn")
        self.frm_right_reset_btn.grid(row=0, column=3, padx=5, pady=5, sticky="wesn")
        self.frm_right_send_btn.grid(row=0, column=4, padx=5, pady=5, sticky="wesn")

    def create_frm_right_clear(self):
        '''
        3、Label显示和十六进制显示和清除接收信息按钮
        '''
        self.receive_hex_cbtn_var = tk.IntVar()
        self.frm_right_clear_label = PyLabel(self.frm_right_clear,
                                                  text="Data Received"+ " "*size_dict["clear_label_width"],
                                                  font=font)
        self.frm_right_threshold_label = PyLabel(self.frm_right_clear,
                                                      text="Threshold:",
                                                      font=font)
        self.thresholdStr = tk.StringVar()
        self.frm_right_threshold_entry = PyEntry(self.frm_right_clear,
                                                      textvariable=self.thresholdStr,
                                                      width=6,
                                                      font=font)
        self.frm_right_hex_checkbtn = PyCheckbutton(self.frm_right_clear,
                                                         text="Hex",
                                                         variable=self.receive_hex_cbtn_var,
                                                         relief="flat",
                                                         font=font)
        self.frm_right_clear_btn = PyButton(self.frm_right_clear, 
                                                 text="Clear",
                                                 width=10,
                                                 font=font,
                                                 command=self.Clear)

        self.frm_right_clear_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.frm_right_threshold_label.grid(row=0, column=1, padx=5, pady=5, sticky="wesn")
        self.frm_right_threshold_entry.grid(row=0, column=2, padx=5, pady=5, sticky="wesn")
        self.frm_right_hex_checkbtn.grid(row=0, column=3, padx=5, pady=5, sticky="wesn")
        self.frm_right_clear_btn.grid(row=0, column=4, padx=5, pady=5, sticky="wesn")

        self.thresholdStr.set(1)
        self.thresholdStr.trace('w', self.GetThresholdValue)

    def create_frm_status(self):
        '''
        下半部分状态栏窗口
        '''
        self.frm_status_label = PyLabel(self.frm_status, 
                                             text="Ready",
                                             font=font)
        self.frm_status_label.grid(row=0, column=0, padx=5, pady=5, sticky="wesn")

    def Toggle(self):
        pass

    def Open(self, event):
        pass

    def Reset(self):
        self.frm_right_send.delete("0.0", "end")

    def Send(self):
        pass

    def Clear(self):
        self.frm_right_receive.delete("0.0", "end")

    def GetThresholdValue(self, *args):
        try:
            self.thresholdValue = int(self.thresholdStr.get())
        except:
            pass


if __name__ == '__main__':
    '''
    main loop
    '''
    root = tk.Tk()
    if g_default_theme == "dark":
        root.configure(bg="#292929")
        combostyle = Style()
        combostyle.theme_use('alt')
        combostyle.configure("TCombobox", selectbackground="#292929", fieldbackground="#292929", background="#292929", foreground="#FFFFFF")
    root.title("Serial-Tool")
    SerialToolUI(master=root)
    root.resizable(False, False)
    root.mainloop()

###

