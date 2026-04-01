class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                  47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        def calculate_products(s):
            product = 1
            for char in s:
                product *= primes[ord(char)-ord('a')]
            return product


        hashmap = defaultdict(list)
        for s in strs:
            key = calculate_products(s)
            hashmap[key].append(s)
        return list(hashmap.values())