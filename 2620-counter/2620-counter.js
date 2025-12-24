/**
 * @param {number} n
 * @return {Function} counter
 */
var createCounter = function(n) {
    let cur = n
    
    return function() {
        let ans = cur;
        cur += 1;
        return ans;
    };
};

/** 
 * const counter = createCounter(10)
 * counter() // 10
 * counter() // 11
 * counter() // 12
 */