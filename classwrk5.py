python={"nandhu","heyden","joy",}
data_science={"abhi","bobby","vishnu","joy"}
python.add("sitharth")
print(python)
data_science.pop()
print(data_science)
print(python & data_science)
print(python|data_science)
new_dict= {
    "python":3,
    "data_science":4
}
for key,items in new_dict.items():
    print(key,items)
double_stud={key:items*2 for key,items in new_dict.items()}
print(double_stud)