# Github user name : ndilhara


def binary_Todecimal(list_):
    """This function convert binary values to decimal values"""
    list_dec=[]

    for i in list_:
        x=str(i) #Assign each elements in the List accoding to index
        count=0
        power=0
        for j in range(len(x)-1,-1,-1):

            count=count+(int(x[j])*2**power)
            power=power+1

        list_dec.append(count)

    return(list_dec)


x=[1111, 1011, 1110, 1010]
print("Decimal list =",binary_Todecimal(x)) 