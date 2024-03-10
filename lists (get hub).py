def lists():
# NAME: alwalid Mahmoud Ebrahim mohammedosman
# ID: 20230719
# problem 5
    #enter multiple of numners
    list1 = int(input("enter lists of number")) #enter any list of number
    list2 = int(input("enter another lists of number")) #enter the same number of elements in this list

    list1 = [int(x) for x in str(list1)] # the numbers will be string
    list2 = [int(x) for x in str(list2)] # the same with this
    if sorted(list1) == sorted(list2): #check if thier are equal
        print("true")
    else:
        print("false")
lists()