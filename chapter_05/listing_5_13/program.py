def positive_integers(until: int):
    for integer in range(until):
        yield integer


positive_iterator = positive_integers(2)

print(next(positive_iterator))
print(next(positive_iterator))


gen = positive_integers(10)

print(type(gen))

for val in gen:
    print(val)


gen2 = positive_integers(5)

while True:

    try:

        print(next(gen2))

    except StopIteration:

        print("That is all")
        break