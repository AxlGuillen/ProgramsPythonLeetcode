def findMedianSortedArrays( nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    que escoga el minimo y el maximo
    """
    l1 = len(nums1)
    l2 = len(nums2)

    menor = min(nums1[0],nums2[0])
    maximo = max(nums1[l1-1],nums2[l2-1])

    m1 = (nums1[0] + nums1[l1-1])/2
    m2 = ((nums2[0] + nums2[l2-1])/2)

    mediana = (m1+m2)/2

    return mediana



nums1 = [1,2]
nums2 = [3,4]

print(findMedianSortedArrays( nums1, nums2))