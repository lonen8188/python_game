# Counter.py
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1

a = Counter() # Counter a = new Counter()
print("count 의 값 : ", a.count)
a.increment()
print("count 의 값 : ", a.count)
