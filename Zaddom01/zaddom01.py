# Maciej Cieszyński

class MyTime:
    def __init__(self, minutes, seconds):
        self.minutes = minutes

        if self.minutes < 0:
            raise ValueError

        self.seconds = seconds

        if (self.seconds < 0) or (self.seconds > 59):
            raise ValueError

    def __lt__(self, other):
        t1 = self.minutes*60 + self.seconds
        t2 = other.minutes*60 + other.seconds

        if t1 < t2:
            return True
        return False
        # if self.minutes < other.minutes:
        #     if self.seconds < other.seconds:
        #         return True
        # return False

    def __gt__(self, other):
        t1 = self.minutes * 60 + self.seconds
        t2 = other.minutes * 60 + other.seconds

        if t1 > t2:
            return True
        return False
        # if self.minutes > other.minutes:
        #     if self.seconds > other.seconds:
        #         return True
        # return False

    def __eq__(self, other):
        if (self.minutes == other.minutes) and (self.seconds == other.seconds):
            # if self.seconds == other.seconds:
            # return f'Obie wartości {self} i {other} są takie same!'
            return True
        return False

    def __add__(self, other):
        total_minutes = self.minutes + other.minutes
        total_seconds = self.seconds + other.seconds
        if total_seconds > 59:
            total_minutes = total_minutes + 1
            total_seconds = total_seconds - 60
            return MyTime(total_minutes, total_seconds)
        return MyTime(total_minutes, total_seconds)

    def __sub__(self, other):
        t1 = self.minutes * 60 + self.seconds
        t2 = other.minutes * 60 + other.seconds

        difference_time = t1 - t2
        if difference_time < 0:
            raise ValueError

        dif_minutes = difference_time // 60
        dif_seconds = difference_time - (dif_minutes * 60)

        # difference_minutes = self.minutes - other.minutes
        # difference_seconds = self.seconds - other.seconds
        # if (difference_minutes < 0) or (difference_seconds < 0):
        #    return ValueError

        return MyTime(dif_minutes, dif_seconds)
        #return MyTime(difference_minutes, difference_seconds)

    def __repr__(self):
        return f'MyTime(minutes = {self.minutes}, seconds = {self.seconds})'


if __name__ == '__main__':
    # tutaj można pisać dowolny kod, nie wpływa to na testy
    p1 = MyTime(10, 10)
    p2 = MyTime(0, 59)
    p3 = p1 + p2
    p4 = p1 - p2
    print(p1)
    print(p2)
    print('Czy p1 < p2?')
    print(p1 < p2)
    print(p1 + p2)
    print(p4)
    pass
