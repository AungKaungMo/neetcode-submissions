class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums: number[]): boolean {
        let input_set = new Set();

        for (let i = 0; i < nums.length; i++) {
            if (input_set.has(nums[i])) {
                return true;
            }
            input_set.add(nums[i]);
        }

        return false;
    }
}
