// Given an integer array nums, find the contiguous subarray (containing at least one number) which has
// the largest sum and return its sum.

// Example

// Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
// Output: 6
// Explanation: [4, -1, 2, 1] has the largest sum = 6

// Time = O(n^2)
const maxSubArray = (nums) => {
    const maxSubarraySum = (arr, n) => {
        var maxSum = 0;
        var windowSum = 0;
        for (var i = 0; i < n; i++) {
            maxSum += arr[i];
        }
        windowSum = maxSum;
        for (var i = n; i < arr.length; i++) {
            windowSum = windowSum - arr[i - n] + arr[i];
            maxSum = Math.max(maxSum, windowSum);
        }
        return maxSum;
    }
    // Iterate through ever possible length of subArray
    max = -Infinity;
    for(let i=1; i<=nums.length; i++){
        max = Math.max(max, maxSubarraySum(nums,i))
    }
    return max;
}