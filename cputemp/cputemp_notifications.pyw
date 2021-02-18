import wmi, ctypes, sys
from win10toast import ToastNotifier
import time

print("1")

time.sleep(5)

print("2")
w = wmi.WMI(namespace="root\wmi")

while True:
    temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
    print("3")
    temperature_info2 = round(temperature_info.CurrentTemperature / 10 - 273.15)
    print(4)
    #temperature_info2 = 51

    if 50 < temperature_info2:
        print(5)
        toaster = ToastNotifier()
        toaster.show_toast("The laptop is getting hot!",
        str("PC temperature is " + str(temperature_info2)),
        duration=5)


    time.sleep(5)

    print(6)
