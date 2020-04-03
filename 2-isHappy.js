// Write an algorithm to determine if a number is "happy".

// A happy number is a number defined by the following process: Starting with any positive integer,
// replace the number by the sum of the squares of its digits, and repeat the process until the number
// equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers
// for which this process ends in 1 are happy numbers.

// Example
// Input: 19
// Output: True

// Explanation:
// 1^2 + 9^2 = 82
// 8^2 + 2^2 = 68
// 6^2 + 8^2 = 100
// 1^2 + 0^2 + 0^2 = 1

const isHappy = (n) => {
    // Create a helper function to sum up the squares of the digits
    const sumSquares = (m) => {
        let sum = 0;
        while (m > 0){
            sum += Math.pow(m%10, 2);
            m = Math.floor(m/10);
        }
        return sum;
    }
    // Continue iterating the sum until 1 is achieved, and break if a loop is occuring
    // Create a set to keep track of all sums that we have achieved
    let check = new Set();
    while (n !== 1) {
        n = sumSquares(n);
        if (check.has(n)){
            return false;
        }
        check.add(n)
    }
    return true;
}