class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0  # Initialize the maximum length
        max_count = 0  # Initialize the count of the most frequent character
        start = 0  # Start index of the sliding window
        char_count = [0] * 26  # Initialize an array to count occurrences of each character

        for end in range(len(s)):
            char_count[ord(s[end]) - ord('A')] += 1  # Increment the count of the current character
            max_count = max(max_count, char_count[ord(s[end]) - ord('A')])  # Update the max count

            # If the number of replacements needed (k) is exceeded, shrink the window from the left
            if (end - start + 1) - max_count > k:
                char_count[ord(s[start]) - ord('A')] -= 1  # Decrement the count of the leftmost character
                start += 1  # Move the left pointer to the right

            max_length = max(max_length, end - start + 1)  # Update the max length

        return max_length

sol = Solution()
sol.characterReplacement("ABBB", 2)

