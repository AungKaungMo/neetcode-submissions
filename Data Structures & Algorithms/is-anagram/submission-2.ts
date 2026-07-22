class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s: string, t: string): boolean {
        const transformed_s = s.split('');
        let counter = 0
        let transformed_t = t

        if (s.length !== t.length) return false

        for (let i = 0; i < transformed_s.length; i++) {
            if(transformed_t.includes(transformed_s[i])) {
                counter++
                transformed_t = transformed_t.replace(transformed_s[i], "")
            }
        }

        if (counter === transformed_s.length) {
            return true
        }

        return false;
    }
}
