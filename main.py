from abc import ABC, abstractmethod

# ----------------------------------------
# 1. Die Observer-Schnittstelle (Abstract Base Class)
# ----------------------------------------

class Observer(ABC):
    """Definiert die Aktualisierungsschnittstelle für Objekte, die benachrichtigt werden sollen."""

    @abstractmethod
    def update(self, subject):
        pass

# ----------------------------------------
# 2. Das Subject (Observable)
# ----------------------------------------

class NewsFeed:
    """Das Subjekt: Hält den Zustand (den neuesten Beitrag) und verwaltet Observer."""
    def __init__(self):
        self._observers = []
        self._latest_post = None

    def attach(self, observer: Observer):
        """Fügt einen Observer hinzu."""
        if observer not in self._observers:
            self._observers.append(observer)
        print(f"[INFO]: Observer {observer.name} abonniert.")

    def detach(self, observer: Observer):
        """Entfernt einen Observer."""
        try:
            self._observers.remove(observer)
            print(f"[INFO]: Observer {observer.name} abgemeldet.")
        except ValueError:
            pass

    def _notify(self):
        """Benachrichtigt alle abonnierten Observer über die Änderung."""
        print(f"\n[NOTIZ]: Benachrichtige {len(self._observers)} Observer...")
        for observer in self._observers:
            observer.update(self)

    # Die Methode, die eine Zustandsänderung auslöst und benachrichtigt
    def publish_post(self, post: str):
        """Veröffentlicht einen neuen Beitrag und löst die Benachrichtigung aus."""
        self._latest_post = post
        print(f"\n[NEUER BEITRAG] Der Newsfeed hat einen neuen Beitrag: '{post}'")
        self._notify()

    # Getter für den Zustand (wird von den Observern aufgerufen)
    @property
    def latest_post(self):
        return self._latest_post

# ----------------------------------------
# 3. Der Konkrete Observer
# ----------------------------------------

class Subscriber(Observer):
    """Der konkrete Beobachter, der den NewsFeed abonniert."""
    def __init__(self, name):
        self.name = name
        self.received_post = None

    def update(self, subject: NewsFeed):
        """Implementiert die Reaktion auf die Benachrichtigung."""
        self.received_post = subject.latest_post
        print(f"-> {self.name} hat einen Update erhalten. Neuer Beitrag: '{self.received_post}'")


# ----------------------------------------
# ANWENDUNG
# ----------------------------------------

# 1. Erstellung des Subjects
news_feed = NewsFeed()

# 2. Erstellung der Observer
user_hans = Subscriber("Hans")
user_lisa = Subscriber("Lisa")
user_max = Subscriber("Max")

# 3. Observer abonnieren das Subject (Attach)
news_feed.attach(user_hans)
news_feed.attach(user_lisa)
news_feed.attach(user_max)

print("\n" + "="*50)

# 4. Das Subject ändert seinen Zustand (Publish/Notify)
news_feed.publish_post("Python ist großartig!")

print("\n" + "="*50)

# 5. Ein Observer meldet sich ab
news_feed.detach(user_lisa)

print("\n" + "="*50)

# 6. Das Subject ändert seinen Zustand erneut
news_feed.publish_post("Design Patterns sind wichtig.")