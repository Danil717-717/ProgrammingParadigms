class NotificationSystem:

    def update(self, message):
        pass

class ConcreteNotificationSystem(NotificationSystem):
    def update(self, message):
        print("Received message:", message)

class Subject:
    _notificationSystem = []

    def attach(self, notificationSystem):
        self._notificationSystem.append(notificationSystem)

    def notify(self, message):
        for notificationSystem in self._notificationSystem:
            notificationSystem.update(message)

# Создаем экземпляр наблюдаемого объекта (подлежащего изменениям)
subject = Subject()

# Создаем экземпляры наблюдателей
notificationSystem1 = ConcreteNotificationSystem()
notificationSystem2 = ConcreteNotificationSystem()

# Присоединяем наблюдателей к наблюдаемому объекту
subject.attach(notificationSystem1)
subject.attach(notificationSystem2)

# Уведомляем наблюдателей о событии
subject.notify("Hello, observers!") # Вывод: "Received message: Hello, observers!"