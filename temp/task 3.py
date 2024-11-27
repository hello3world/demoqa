import random

def get_result_task3():
    N = int(input("Enter number than or equal 3 and odd\n"))
    while True:
        if N % 2 == 0 or N < 3:
            print("Number have to be more than or equal 3 and odd. Enter new Number\n")
            N = int(input("Enter number than or equal 3 and odd\n"))
        else:
            break

    # init 2size array
    array = []
    for i in range(N):
        row = [0] * N
        array.append(row)
        # print("default array", row)

    for i in range(N):
        for j in range(N):
            array[i][j] = random.randint(-100, 100)

    print("Our array:")
    for row in array:
        print(row)

    min_el = array[0][N-1]

    for i in range(N):
        if i != N - 1 - i:
            min_el = min(min_el, array[i][N - 1 - i])

    print("Minimum element:", min_el)

get_result_task3()