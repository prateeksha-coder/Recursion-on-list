#for descending order sorting check
def checksorted(a):
   length = len(a)
   if length == 1 or length == 0:
       return True  
   return a[0] >= a[1] and checksorted(a[1:])
   
a = [8,7,6,5,1,-1] 
if checksorted(a):
   print("\nyes given array is sorted")
else:
   print("\nNo given array id not sorted")