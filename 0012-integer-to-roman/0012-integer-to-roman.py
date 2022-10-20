class Solution:
    def intToRoman(self, num: int) -> str:
        
        numeral_map = {
            1: "I", 4: "IV", 5: "V", 9: "IX", \
            10: "X", 40: "XL", 50: "L", 90: "XC", \
            100: "C", 400: "CD", 500: "D", 900: "CM", \
            1000: "M"
        }
        
        sorted_keys = sorted(numeral_map)
        result = ""
        while num > 0:
            for key in reversed(sorted_keys):
                while int(num/key) > 0:
                    num -= key
                    result += numeral_map[key]
        return result
        