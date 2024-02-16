def kthsmallest(arr1, arr2, k):

    l1 = 0 
    r1 = len(arr1) - 1

    l2 = 0
    r2 = len(arr2) - 1

    while not (l1 > r1 or l2 > r2): 

        m1 = (l1 + r1) // 2
        m2 = (l2 + r2) // 2

        k_c = (m1 - l1 + 1) + (m2 - l2 + 1)

        if k_c <= k:
            if arr1[m1] < arr2[m2]:
                k = k - (m1 - l1 + 1)
                l1 = m1 + 1
            else:
                k = k - (m2 - l2 + 1)
                l2 = m2 + 1
        else:
            if arr1[m1] < arr2[m2]:
                r2 = m2 - 1
            else:
                r1 = m1 - 1

    # print(l1, r1, l2, r2, k)
    if l1 > r1:
        return arr2[l2 + k - 1]
    else:
        return arr1[l1 + k - 1]
    
if __name__ == "__main__":

    arr1 = [1, 4, 8, 10]
    arr2 = [3, 5, 6,  9]

    print(kthsmallest(arr1, arr2, 4))

    for k in range(1, 9):
        print(f"{k}th: {kthsmallest(arr1, arr2, k)}")