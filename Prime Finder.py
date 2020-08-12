
# prime finder

def seive(n):
    
    prime_list = ["P"] * (n+1)

    prime_list[0] = "N"
    prime_list[1] = "N"



    for i in range(2, len(prime_list)//2 + 1):
        if prime_list[i] == "P":
            for j in range(i*i,len(prime_list), i):
                prime_list[j] = "N"

    return(prime_list)

def prettyPrint(L):

    L2 = []
    
    for i in range(len(L)):
        if L[i] == "P":
            L2.append(i)
            
    return L2


n = int(input("Enter the highest number: "))
print(seive(n))
print(prettyPrint(seive(n)))
