class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;

    const charCounts = new Map<string, number>();

    // Step 1: Count up for 's' and count down for 't'
    for (let i = 0; i < s.length; i++) {
        charCounts.set(s[i], (charCounts.get(s[i]) ?? 0) + 1);
        charCounts.set(t[i], (charCounts.get(t[i]) ?? 0) - 1);
    }

    // Step 2: Check if all counts are exactly 0
    for (const count of charCounts.values()) {
        if (count !== 0) return false;
    }

    return true;
}
}
