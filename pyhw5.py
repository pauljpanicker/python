frontend={"sitharth","thobith"}
backend={"vishnu"}
backend.add("jayan")
print(backend)
frontend.pop()
print(frontend)
union=(frontend | backend)
print(union)
print(frontend & backend)
print(len(union))
my_dict={
    "frontend":2,
    "backend":2
}
for x,y in my_dict.items():
    print(x,y)
new_dict= {x: str(y) + "fullstack" for x,y in my_dict.items()}
print(new_dict)


