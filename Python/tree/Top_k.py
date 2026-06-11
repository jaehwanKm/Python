'''def swap_elements(top_k, index):
    if top_k[ index ] > top_k[ index - 1 ]:
        top_k[ index ], top_k[ index - 1 ] = top_k[ index - 1 ], top_k[ index ]
        return True
    return False

def top_k_unique(mylist, k):
    elements = {}
    for num in mylist:
        elements[ num ] = True
    mylist = list( elements.keys() )
    top_k = []
    for num in mylist:
        if len( top_k ) < k:
            top_k.append( num )
            for index in range( len( top_k ) - 1, 0, -1 ):
                if not swap_elements(top_k, index):
                    break
        else:
            a = top_k[ k-1 ]
            if num > a:
                top_k[ k-1 ] = num
                for index in range( len( top_k ) - 1, 0, -1 ):
                    if not swap_elements(top_k, index):
                        break
    return top_k

mylist = [5, 2, 8, 3, 8, 10, 7, 10]
k = 3


result = top_k_unique(mylist, k)

print(result)'''

def swap_elements(top_k, index):
    if top_k[index] < top_k[index - 1]:
        top_k[index], top_k[index - 1] = top_k[index - 1], top_k[index]
        return True
    return False

def top_k_unique(mylist, k):
    elements = {}
    for num in mylist:
        elements[num] = True
    mylist = list(elements)
    top_k = []
    for num in mylist:
        if len(top_k) < k:
            top_k.append(num)
            for index in range(len(top_k) - 1, 0, -1):
                if not swap_elements(top_k, index):
                    break
        else:
            a = top_k[0]
            if num > a:
                top_k[0] = num
                for index in range(len(top_k) - 1, 0, -1):
                    if not swap_elements(top_k, index):
                        break
    return top_k

mylist = [5, 2, 8, 3, 8, 10, 7, 10]
k = 3


result = top_k_unique(mylist, k)

print(result)