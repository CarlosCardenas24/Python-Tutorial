name = "Carlos"
count = 1

def another():
    color = "blue"
    global count
    count += 1
    print(count)

    def greeting(name):
        #nonlocal color
        color = "red"
        print(color)
        print(name)

    greeting("Carlos")

another()
print(count)