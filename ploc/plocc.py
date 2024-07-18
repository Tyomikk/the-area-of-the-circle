from math import pi, sqrt

class GeometryCalculator:
    """
    Библиотека для вычисления площадей фигур.
    """

    def __init__(self):
        """
        Инициализация класса.
        """
        pass

    def circle_area(self, radius):
        """
        Вычисляет площадь круга по радиусу.

        Args:
            radius: Радиус круга.

        Returns:
            Площадь круга.
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        return pi * radius ** 2

    def triangle_area(self, side1, side2, side3):
        """
        Вычисляет площадь треугольника по трем сторонам.

        Args:
            side1: Длина первой стороны.
            side2: Длина второй стороны.
            side3: Длина третьей стороны.

        Returns:
            Площадь треугольника.
        """
        if any(side <= 0 for side in [side1, side2, side3]):
            raise ValueError("Все стороны треугольника должны быть положительными числами.")
        if not (side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1):
            raise ValueError("Треугольник не может быть построен с такими сторонами.")

        s = (side1 + side2 + side3) / 2
        return sqrt(s * (s - side1) * (s - side2) * (s - side3))