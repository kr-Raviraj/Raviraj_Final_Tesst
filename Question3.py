
# There's a string parameter which a function will accept. You have to replace all the vowels with the letter 'X'. Return the final string after replacement.
# Input: “consultadd”
# OUTPUT: cXnsXltXdd

def Vowel_replace(Input):
    String=Input.lower()
    list1=[]
    vowels=["a","e","i","o","u"]
    for i in range(len(String)):
        if String[i] in vowels:
            list1.append("X")
        else:
            list1.append(String[i])

    Output="".join([i for i in list1])
    return Output


Obj=Vowel_replace(input("Enter the string"))
print(Obj)