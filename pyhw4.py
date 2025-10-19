fruits=["apple","orange","grape"]
vegetables=["tomato","carrot","onion"]
beverages=["moutaindew","supermakka","brocode"]
fruits.append("mango")
print(fruits)
del beverages[-1]
print(beverages)
inventery=[fruits,vegetables,beverages]
print(inventery)

print(fruits[0:2]) #slicing
print(vegetables[-1])
for x in fruits:
    print(x)
length=[len(x) for x in fruits]
print(length)
if "water" in beverages :
    print("true")
else:
    print("false")
print("water" in beverages)
tuple=(fruits[0],beverages[0],vegetables[0])
print(tuple)