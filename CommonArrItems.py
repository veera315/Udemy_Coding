# Two Input Arrays
# Return True/False
# Input arrays can be unlimited

#def containsCommonItems(arr1, arr2):
#  for i in arr1:
##    for j in arr2:
#      if i == j:
#        print("Found a Common Element " + str(i))
#        return True
#  return False


arrdict= {}
def containsCommonItemseff(arr1, arr2):
  for i in arr1:
    if i not in arrdict:
      arrdict[i] = True
  
  print (arrdict)
  for j in arr2:
    if j in arrdict:
      print ("Found the common element " + j)
      return True
  
  return False

a = ['a', 'b', 'c', 'x']
b = ['z','y','t']
Res = containsCommonItemseff(a,b)
print("Found Common Elements " + str(Res))