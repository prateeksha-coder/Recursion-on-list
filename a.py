def MinElementArray(a):
    length=len(a)
    if length==1:
        return a[0]
    return min(a[0],MinElementArray(a[1:]))
a=[-1,-56,2,234,234,745,3,6,3987]
print("Largest Element of array: ",MinElementArray(a))