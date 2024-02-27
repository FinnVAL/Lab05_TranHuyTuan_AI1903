tuple1 = (11,22)
tuple2 = (99,88)

temp = tuple2
tuple2 = tuple1
tuple1 = temp

print("tuple1:",tuple1)
print("tuple2:",tuple2)