class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> numSet1 = new HashSet<>();
        Set<Integer> numSet2 = new HashSet<>();

        for (int num : nums1) numSet1.add(num);
        for (int num: nums2) numSet2.add(num);

        List<Integer> res1 = new ArrayList<>(numSet1);
        res1.removeAll(numSet2);

        List<Integer> res2 = new ArrayList<>(numSet2);
        res2.removeAll(numSet1);

        return Arrays.asList(res1,res2);
        
    }
}