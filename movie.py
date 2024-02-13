def solution(N, K, seat):
    count = 0
    stack = Stack()
    for i in seat:
        # print(stack.show())
        if i == 0:
            count += 1
            stack.add(count)

        if i > 0:
            # stack.remove()
            count -= 1

    return stack.show()


class Stack:
    def __init__(self):
        self.arr = []

    def add(self, val):
        return self.arr.append(val)

    def remove(self):
        return self.arr.pop()

    def show(self):
        return self.arr


print(solution(5, 12, [0, 0, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1]))
