import sys
import pathlib

sys.path.insert(1, f"{pathlib.Path().resolve()}")
import modbus_protocols
import connection
from time import *
from tkinter import messagebox

messagebox.showinfo(title="INFO", message="Connecting!")
while True:
    try:
        connection.connection_plc()  # calling function connection_plc
        modbus_protocols.write_modbus()  # calling function write_modbus
        modbus_protocols.read_modbus()  # calling function read_modbus
        modbus_protocols.is_raining()  # calling function is_raining
        print("The information was sent!")  # print
    except OSError("Invalid data!") as e:
        messagebox.showerror("Error", str(e))
        raise ValueError("Invalid data!")  # raise an exception
    sleep(15)  # sleep
