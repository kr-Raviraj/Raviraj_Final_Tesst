# Input: [1,2,e,3,4,a,b,5,6,7]
# Return a list with all numbers coming first and then characters.
# Output- [1,2,3,4,5,6,7,a,b,c,e]
# The numbers and characters needs to be sorted in the list itself.
#

list1=[]
list2=[]

def sort_num(Input):
    for i in Input:
        a=str(i)
        if a.isdigit():
            list1.append(int(a))
            list1.sort()
        else:
            list2.append(a)
            list2.sort()

    Output=[]
    Output.extend(list1)
    Output.extend(list2)

    return Output
a=sort_num([1,2,"e",3,4,"a","b",5,6,7])
print(a)