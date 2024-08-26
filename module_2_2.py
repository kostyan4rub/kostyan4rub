first = int(input())
second = int(input())
third = int(input())
if first==second or second==third or third==first:
    print(2)
elif first==second==third:
    print(3)
else:
    print(0)