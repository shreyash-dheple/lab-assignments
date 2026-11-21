num = int(input())

previous = None
count = 0
maximum = 0

while num != 0:
    if num == previous:
        count += 1
    else:
        count = 1

    if count > maximum:
        maximum = count

    previous = num
    num = int(input())

print(f'The maximum number of consecutive occurrences is: {maximum}')
      
