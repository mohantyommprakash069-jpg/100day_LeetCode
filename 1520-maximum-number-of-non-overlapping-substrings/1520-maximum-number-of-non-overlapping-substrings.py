class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        first = {}
        last = {}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i
        
        valid_intervals = []
    
        # Step 2: Expand intervals for each character starting from its first appearance
        for ch in first:
            l = first[ch]
            r = last[ch]
            valid = True
        
            i = l
            while i <= r:
                # Expand the right bound if a character inside ends later
                r = max(r, last[s[i]])
                
                # If a character inside starts before l, this start position 'l' is invalid
                if first[s[i]] < l:
                    valid = False
                    break
                i += 1
            
            if valid:
                valid_intervals.append((l, r))
            
        # Step 3: Sort valid intervals by their end index (Greedy choice)
        valid_intervals.sort(key=lambda x: x[1])
    
        result = []
        prev_end = -1
    
        for l, r in valid_intervals:
            if l > prev_end:
                result.append(s[l:r + 1])
                prev_end = r
            
        return result