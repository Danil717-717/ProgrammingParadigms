class Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

logger1 = Logger()
logger2 = Logger()

print(logger1 is logger2) # Вывод: True
print(logger1)
print(logger2)