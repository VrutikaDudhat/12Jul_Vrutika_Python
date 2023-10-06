# Write a Python script to sort (ascending and descending) a dictionary by value. 

d={ "vrutika":1, "abc":10, "xyz":20,
      "angle": 11,  "dwija":24 } 


 #sort by values
y1=sorted(d.items(),key=lambda x:x[1])
print(dict(y1))
