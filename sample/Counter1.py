# Counter1.py
class Counter:
    def __init__(self, initvalue = 0):
        self.count = initvalue
    def increment(self):
        self.count += 1

a=Counter(100)

print("count 의 값 : ", a.count)
a.increment()
print("count 의 값 : ", a.count)

b = Counter()
print("count 의 값 : ", b.count)
b.increment()
print("count 의 값 : ", b.count)
