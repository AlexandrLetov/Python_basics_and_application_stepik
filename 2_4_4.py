with open('./Data/dataset_24465_4.txt') as file:
    result = [line.rstrip() for line in file]

for line in reversed(result):
    print(line)


# print([line for line in reversed(open('./Data/dataset_24465_4.txt').readlines())])
