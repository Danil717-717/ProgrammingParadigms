from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):

    def draw(self):
        return "Рисуем круг"

class Square(Shape):

    def draw(self):
        return "Рисуем квадрат"

class ShapeFactory:

    @staticmethod
    def create_shape(shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            raise ValueError(f"Неизвестный тип фигуры: {shape_type}")


circle = ShapeFactory.create_shape("circle")
square = ShapeFactory.create_shape("square")

print(circle.draw())
print(square.draw())

