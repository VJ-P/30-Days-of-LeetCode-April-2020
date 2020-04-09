# Given an array of strings, group anagrams together.

# Example:

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
# ]

# Note:
# - All inputs will be in lowercase.
# - The order of your output does not matter.

def groupAnagrams(strs):
    hashmap = {}
    for string in strs:
        charArray = list(string)
        charArray.sort()
        charArray = ''.join(charArray)
        if not(charArray in hashmap):
            hashmap[charArray] = []
        hashmap[charArray].append(string)
    return hashmap.values()

#print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))