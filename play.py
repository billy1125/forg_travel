import frog

gift = []

name = input("Input: ")
my_frog = frog.frog(name)
print('我的青蛙名字叫：' + my_frog.my_name())

while True:

    go = input("Input: (give)")

    if go == 'give':
        gift = my_frog.go_to_travel([10,3,5])

        print(gift)

    if go == 'end':
        break

exit()
