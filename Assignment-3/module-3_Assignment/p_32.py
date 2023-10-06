# Write a Python program to map two lists into a dictionary

values=['vrutika','sajani','griva']
keys=[1,2,3]
print(str(keys))
print(str(values))

d={}
for key in keys:
    for value in values:
        d[key]=value
        values.remove(value)
        break
print(str(d))


name = [ "dwija", "krisha", "mishu", "Astha" ]
roll_no = [ 4, 5, 6, 7 ]
 
mapped = zip(name, roll_no)
 
print(dict(mapped))