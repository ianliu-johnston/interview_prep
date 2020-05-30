from timeit import timeit

def fizzbuzz_nomod():
    count4 = 0
    count6 = 0
    buff = ""
    for i in range(1, 101):
        count4 += 1
        count6 += 1
        if count4 != 4 and count6 != 6:
            buff += str(i)
        if count4 == 4:
            buff += "Linked"
            count4 = 0
        if count6 == 6:
            buff += "In"
            count6 = 0
    return buff


def fizzbuzz_mod():
    buff = ""
    for i in range(1, 101):
        if i % 4 == 0 and i % 6 == 0:
            buff += "LinkedIn"
        elif i % 4 == 0:
            buff += "Linked"
        elif i % 6 == 0:
            buff += "In"
        else:
            buff += str(i)
    return buff

if __name__ == "__main__":
    timed_nomod = timeit(fizzbuzz_nomod, number=5)
    timed_mod = timeit(fizzbuzz_mod, number=5)
    print("")
    print(f"nomod: {timed_nomod}, mod: {timed_mod}")
