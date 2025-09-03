def FirstThree(lst):
    lst.sort(reverse = True)
    Nums = lst[0:3]
    
    print("\nThe Largest Three No.s are: ")
    lst = []
    i = 1
    for nos in Nums:
        print(f"{i}. {nos}")
        i+=1

n = int(input("How many elements for the list: "))
lst = []
for i in range(1, n+1):
    lst.append(int(input(f"Enter the element {i}: ")))

FirstThree(lst)
