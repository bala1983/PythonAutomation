class Diamont:

    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a

    def __setattr__(self, key, value):
        if key == 'side_a':
            if value <= 0:
                raise ValueError('side_a must be more than 0')

        if key == 'angle_a':
            if not 180 >= value >= 0:
                raise ValueError('angle_a and angle_b must be 180 degrees')

        super().__setattr__(key, value)

d = Diamont(10, 150)
print(d.side_a, d.angle_a, d.angle_b)