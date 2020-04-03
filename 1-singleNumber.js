// Given a non-empty array of integers, every element appears twice except for one. Find that single one.

// Note:
// Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

// Examples

// Input: [2, 2, 1]
// Output: 1

// Input: [4, 1, 2, 1, 2]
// Output: 4

// Using a frequency counter: Time => O(n), Memory => O(n)
const singleNumber = (arr) => {
    // Create an object to keep track of each element
    freqCounter = {};
    // Iterate through element in the array
    for(let val of arr){
        // Increment the frequency of each number
        freqCounter[val] = (freqCounter[val] || 0) + 1;
    }
    // Iterate through the dictionary until a key with a value 1 is found
    for (val in freqCounter){
        if (freqCounter[val] == 1){
            return val;
        }
    }
}

// Using the XOR bitwise operator: Time => O(n), Memory => O(1)
// XOR Rules:
// n^n == 0
// n^0 == n
// so therefore, if input is [4, 1, 2, 1, 2]
// 4^1^2^2^1 == 4^1^1^2^2 == 4^0^0 == 4
const singleNumber = (arr) => {
    let ans = 0;
    for (let val of arr){
        ans = ans^val;
    }
    return ans;
}

//console.log(singleNumber([4, 1, 2, 1, 2]));