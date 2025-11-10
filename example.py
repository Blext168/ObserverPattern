import random
import time

# --- Subject (Beobachtetes Objekt) ---
class TemperatureSensor:
    def __init__(self):
        self._observers = []      # Liste der Beobachter
        self._temperature = 0.0

    def attach(self, observer):
        """Fügt einen Beobachter hinzu"""
        # TODO: Beobachter zur Liste hinzufügen
        pass

    def detach(self, observer):
        """Entfernt einen Beobachter"""
        # TODO: Beobachter aus der Liste entfernen
        pass

    def notify(self):
        """Benachrichtigt alle Beobachter"""
        # TODO: Alle Beobachter über die neue Temperatur informieren
        pass

    def set_temperature(self, new_temp):
        """Setzt eine neue Temperatur und informiert Beobachter"""
        print(f"\n[Sensor] Neue Temperatur: {new_temp:.1f}°C")
        self._temperature = new_temp
        self.notify()


# --- Observer (Beobachter) ---
class TemperatureDisplay:
    def update(self, temperature):
        """Zeigt die aktuelle Temperatur an"""
        # TODO: Gib die Temperatur auf der Konsole aus
        pass


class TemperatureAlarm:
    def __init__(self, threshold=30.0):
        self.threshold = threshold

    def update(self, temperature):
        """Warnt, wenn die Temperatur zu hoch ist"""
        # TODO: Wenn Temperatur > threshold -> Warnung ausgeben
        pass


# --- Hauptprogramm ---
def main():
    sensor = TemperatureSensor()

    # Beobachter erstellen
    display = TemperatureDisplay()
    alarm = TemperatureAlarm(threshold=28.0)

    # Beobachter registrieren
    # TODO: display und alarm beim Sensor registrieren

    # Simulation: Temperatur ändert sich zufällig
    for _ in range(5):
        new_temp = random.uniform(20, 35)
        sensor.set_temperature(new_temp)
        time.sleep(1)


if __name__ == "__main__":
    main()
