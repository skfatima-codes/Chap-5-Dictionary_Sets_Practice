marks={
    "Harry":96,
    "Fatima":96,
    "Ali":94,
    0:"Harry" # we can also write harry like that and 
}
#print(marks.items()) #we got key-value pairs in the form of tuple
# ouptut=dict_items([('Harry', 96), ('Fatima', 96), ('Ali', 94), (0, 'Harry')])
# print(marks.keys())
# print(marks.values())
marks.update({"Harry":99,"Naima":98}) # it will change the marks of harry
print(marks) # output={'Harry': 99, 'Fatima': 96, 'Ali': 94, 0: 'Harry'}
# get-->return the value of specifeid key
print(marks.get("Fatima2"))# None
print(marks.get["Fatima2"])# it will through an error

# print(marks.pop("Harry")) # it remove Harry from list which is key value
print(marks)