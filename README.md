# 👀 Observer Pattern

## 🛠️ Funktionsweise

Die Grundidee des Musters, das mehrere Objekte informiert werden, sobald sich der Zustand eines bestimmten `Subjekts` sich ändert.
Das `Subjekt` ist Objekt, welches wir beobachten. Dabei gibt es ein `Subjekt`, welches eine Liste von Observern verwaltet. 
Observer-Objekte können ein `Subjekts` abonnieren. Bei Änderung der Daten im `Subjekts` werden alle zugehörigen Observer 
informiert und diese können dann ihre Daten aktualisieren.

---

## 📝 Definition
Das **Observer Pattern** ist ein **Verhaltensmuster** in der objektorientierten Programmierung.  
Es beschreibt eine **1:n-Beziehung** zwischen Objekten:  
Wenn sich der Zustand eines **Subjects** (Beobachteten) ändert, werden automatisch alle **Observer** (Beobachter) benachrichtigt und aktualisiert.

---

## 🔧 Problemstellung
- Mehrere Objekte (Observer) interessieren sich für Änderungen im Zustand eines anderen Objekts (Subject).
- Ohne Pattern müsste das Subject **hart codiert** wissen, welche Observer es benachrichtigen muss → enge Kopplung.
- Das macht die Architektur **unflexibel und schwer erweiterbar**.

👉 Beispiel: Eine Wetterstation misst Temperaturen, verschiedene Displays und Logger wollen informiert werden, wenn sich die Temperatur ändert.

---

## 💡 Lösung
- Das **Subject** verwaltet eine Liste von Observern.
- Observer registrieren oder deregistrieren sich beim Subject.
- Bei einer Zustandsänderung ruft das Subject die `Update()`-Methode aller registrierten Observer auf.
- Observer reagieren individuell auf die Benachrichtigung.

---

## 🏗️ Struktur

- **Subject (Observable)**: hält Zustand und Liste der Observer.
- **Observer**: Interface mit `Update()`-Methode.
- **ConcreteObservers**: reagieren auf Benachrichtigungen.
- **Client**: verbindet Subject und Observer.

---

## ✅ Vorteile

- **Lose Kopplung**: Subject kennt nur das Observer-Interface, nicht die konkrete Implementierung.
- **Flexibel:** Beliebig viele Observer können sich an- und abmelden.
- **Wiederverwendbar:** Observer und Subjects sind unabhängig voneinander nutzbar.

## ⚠️ Nachteile

- Kann zu **vielen Benachrichtigungen** führen (Performance-Thema).
- Die Reihenfolge der Benachrichtigung ist nicht garantiert.
- Gefahr von **Speicherlecks**, wenn Observer nicht deregistriert werden.

## 🤝 Anwendungsfälle

- GUI-Frameworks: Button-Klick → mehrere Listener.
- Wetterstation (wie im Beispiel).
- Event-Systeme (z. B. Logging, Monitoring).
- Datenmodelle, die Views automatisch aktualisieren sollen (MVC, MVVM).

## 👉 Merksatz:
Das Observer Pattern ist wie ein **Newsletter**:

Sobald neue Informationen erscheinen, werden alle **Abonnenten (Observer)** automatisch benachrichtigt.

