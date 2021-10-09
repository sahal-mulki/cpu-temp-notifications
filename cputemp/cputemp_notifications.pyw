import wmi, ctypes, sys
from win10toast import ToastNotifier

time.sleep(5)

w = wmi.WMI(namespace="root\wmi")

while True:

    temperature_info = w.MSAcpi_ThermalZoneTemperature()[0]
    temperature_info2 = round(temperature_info.CurrentTemperature / 10 - 273.15)
    
    if 50 < temperature_info2:
        toaster = ToastNotifier()
        toaster.show_toast("The PC is getting hot!",
        str("PC temperature is " + str(temperature_info2)),
        duration=5)

    time.sleep(5)
