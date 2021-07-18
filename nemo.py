nemo = ["Nemo","Nemo1","Nemo2","Nemo3"]

import time
t0 = time.time()
for i in nemo:
  if i == "Nemo":
    print ("Found Nemo")
  else:
    print ("Nemo not found")
t1 = time.time()
print ("Time taken: " + str(t1-t0))