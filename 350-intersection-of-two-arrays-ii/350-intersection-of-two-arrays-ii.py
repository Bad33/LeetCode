class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        c = collections.Counter(nums1) & collections.Counter(nums2)
        intersect = []
        for i in c:
            intersect.extend([i] * c[i])
        return intersect
                 
            