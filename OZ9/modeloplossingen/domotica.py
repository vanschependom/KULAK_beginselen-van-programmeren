import psutil
import time

class HomeController():
    
    def __init__(self):
        self._apparaten = []
        self._sensoren = []
        self._boottime = psutil.boot_time()
    
    def get_uptime(self):
        return time.time()-self._boottime
    
    def get_boottime(self):
        return self._boottime
    
    def print_info(self):
        for apparaat in self._apparaten:
            apparaat.print_info()

class Apparaat():
    
    def __init__(self, naam, sn, verbruik, status):
        self._verbruik = verbruik
        self._naam = naam
        self._serienummer = sn
        self._verbruik = verbruik
        self._status = status
    
    def set_status(self, status):
        self._status = status
    
    def get_status(self):
        return self._status
    
    def get_verbruik(self):
        return self._verbruik
    
    def print_info(self):
        print(f"Apparaat: {self._naam}\t sn: {self._serienummer}\t status: {self._status}")
    
class Sensor(Apparaat):
    def __init__(self, naam, sn, ip):
        super().__init__(naam, sn, None, None)
        self._ip = ip
    
    def get_naam(self):
        return self._naam
    
    def get_sn(self):
        return self._serienummer
    
    def get_ip(self):
        return self._ip

class Thermostaat(Sensor):
    
    def __init__(self, naam, sn, ip, binnen_temp, buiten_temp):
        super().__init__(naam, sn, ip)
        self._binnen_temp = binnen_temp
        self._buiten_temp = buiten_temp

    def get_binnen_temperatuur(self):
        return self._buiten_temp
    
    def get_buiten_temperatuur(self):
        return self._buiten_temp
    
    