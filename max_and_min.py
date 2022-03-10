max = None
min = None
box = []
while True:
    num = input('enter the numbers you like: \n')
    if num == 'done':
        break
    try:
        list = int(num)
        
    except:
        print('please enter a number not letter')
        continue
    box.append(list)

print ("the numbers you inputted are: ",box,'\n')
    
for x in box:
      if max is None or x > max:#to check if there's a number high than the current max else keep the current number
         max = x
print ("the highest number is ",max,'\n')

for y in box:
    if min is None or y < min:#to check if there's a number lower than the current max else keep the current number
        min = y
print ('the lowest number is ',min, '\n')

     