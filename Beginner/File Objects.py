
with open('test.txt', 'r') as f:
    f_contents = f.read(4)
    print(f_contents, end=" ")

    # for line in f:
    #     print(line, end="")
    # f_contents = f.readline()
    # print(f_contents, end="")


print(f.mode)
print(f.name)
print(f.closed)

f.close()