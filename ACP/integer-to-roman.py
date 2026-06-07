class Solution(object):
    def intToRoman(self, num):
        # Mapping for every decimal place value
        mapping = {
            1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
            10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
            100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
            1000: "M", 2000: "MM", 3000: "MMM"
        }
        
        digit = 1
        result = ""
        
        # Process the number digit by digit from right to left
        while num > 0:
            value = num % 10
            # If the digit is not zero, map it to its Roman counterpart
            if value > 0:
                result = mapping[value * digit] + result
            
            # Move to the next decimal place
            num = num // 10
            digit = digit * 10
        
        return result