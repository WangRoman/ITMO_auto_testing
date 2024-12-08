def length(s: str = " ") -> str:
    return len(s)
print(length())

a: list = [1, 2]
b: list = [1, 2, 3]
def lists(a, b) -> list:
    return max(a, b)
print(lists(a, b))

c = [1, 2, 3, 4]
def result(c):
    c.append(5)
    return c
print(result(c))

d = [1, 2, 3, 4, 5]
def summ(d):
    return d
print(summ(sum(d)))