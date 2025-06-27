# Dictionary is used to store key-values
# unordered,mutable,indexed,contain duplicate keys
student = {
    "name": "Ali",
    "age": 20,
    "grade": "A"
}
# print(student["name"])  # Output: Ali
# print(len(student)) # how many keys in Student (Dictionary)
# student.setdefault("ID","Ali123")
# student.pop("age")
# student.update({"age":21}) # we can change age,id by using upadate
student.popitem()
print(student)
