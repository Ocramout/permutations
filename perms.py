class Digit:
    def __init__(self, arr, next_digit=None):
        self.arr = arr
        self.next_digit = next_digit
        self.arr_cycle = self.__cycle()
        self.increment()

    def __cycle(self):
        while True:
            for item in self.arr:
                  yield item
            if self.next_digit:
                self.next_digit.increment()

    def increment(self):
        self.value = self.arr_cycle.next()

    def __str__(self):
        return str(self.value)

class Code:
    def __init__(self, arr, dep):
        self.arr = arr
        self.dep = dep
        self.values = []

        prev = Digit(arr)
        for i in range(dep):
            if i == 0:
                digit = Digit(arr)
            else:
                digit = Digit(arr, prev)

            self.values += [digit]
            prev = digit

    def increment(self):
        LAST = -1
        if len(self.values) != 0:
            self.values[LAST].increment()

    def permutations(self):
        for _ in range(len(self.arr)**self.dep):
            yield str(self)
            self.increment()

    def __str__(self):
        return ''.join([str(v) for v in self.values])


code = Code(range(1, 10), 8)
# for permutation in code.permutations():
#     print(permutation)

import time
start = time.time()
for perm in code.permutations():
    i = 1
stop = time.time()
print("time: {}".format(stop - start))