def string_times(str, n):
    """
    https://codingbat.com/prob/p193507

    Given a string and a non-negative int n, return a larger string that is n copies of the original string.

    string_times('Hi', 2) â†’ 'HiHi'
    string_times('Hi', 3) â†’ 'HiHiHi'
    string_times('Hi', 1) â†’ 'Hi'
    """
    return str*n # Remove this line and add your implementation


def front_times(str, n):
    """
    https://codingbat.com/prob/p165097

    Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;

    front_times('Chocolate', 2) â†’ 'ChoCho'
    front_times('Chocolate', 3) â†’ 'ChoChoCho'
    front_times('Abc', 3) â†’ 'AbcAbcAbc'
    """
    return str[0:3]*n # Remove this line and add your implementation


def array_count9(nums):
    """
    https://codingbat.com/prob/p166170

    Given an array of ints, return the number of 9's in the array.

    array_count9([1, 2, 9]) â†’ 1
    array_count9([1, 9, 9]) â†’ 2
    array_count9([1, 9, 9, 3, 9]) â†’ 3
    """
    c=0
    for n in nums:
        if n==9:
            c+=1
    return c # Remove this line and add your implementation


def array_front9(nums):
    """
    https://codingbat.com/prob/p110166

    Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.

    array_front9([1, 2, 9, 3, 4]) â†’ True
    array_front9([1, 2, 3, 4, 9]) â†’ False
    array_front9([1, 2, 3, 4, 5]) â†’ False
    """
    for i in range(min(len(nums),4)):
        if nums[i]==9:
            return True
    return False # Remove this line and add your implementation


def array123(nums):
    """
    https://codingbat.com/prob/p193604

    Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.

    array123([1, 1, 2, 3, 1]) â†’ True
    array123([1, 1, 2, 4, 1]) â†’ False
    array123([1, 1, 2, 1, 2, 3]) â†’ True
    """
    for i in range(len(nums)-2):
        if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
            return True
    return False # Remove this line and add your implementation


def string_match(a, b):
    """
    https://codingbat.com/prob/p182414

    Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

    string_match('xxcaazz', 'xxbaaz') â†’ 3
    string_match('abc', 'abc') â†’ 2
    string_match('abc', 'axc') â†’ 0
    """
    c=0
    for i in range(min(len(a)-1,len(b)-1)):
        if a[i]==b[i] and a[i+1]==b[i+1]:
            c+=1
    return c # Remove this line and add your implementation


def first_half(str):
    """
    https://codingbat.com/prob/p107010

    Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

    first_half('WooHoo') â†’ 'Woo'
    first_half('HelloThere') â†’ 'Hello'
    first_half('abcdef') â†’ 'abc'
    """
    return str[0:int(len(str)/2)] # Remove this line and add your implementation


def without_end(str):
    """
    https://codingbat.com/prob/p138533

    Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will be at least 2.

    without_end('Hello') â†’ 'ell'
    without_end('java') â†’ 'av'
    without_end('coding') â†’ 'odin'
    """
    return str[1:len(str)-1] # Remove this line and add your implementation


def combo_string(a, b):
    """
    https://codingbat.com/prob/p194053

    Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside and the longer string on the inside. The strings will not be the same length, but they may be empty (length 0).

    combo_string('Hello', 'hi') â†’ 'hiHellohi'
    combo_string('hi', 'Hello') â†’ 'hiHellohi'
    combo_string('aaa', 'b') â†’ 'baaab'
    """
    if len(a)>len(b):
        return b+a+b
    return a+b+a # Remove this line and add your implementation


def left2(str):
    """
    https://codingbat.com/prob/p160545

    Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string length will be at least 2.

    left2('Hello') â†’ 'lloHe'
    left2('java') â†’ 'vaja'
    left2('Hi') â†’ 'Hi'
    """
    return str[2:]+str[0:2] # Remove this line and add your implementation


def near_ten(num):
    """
    https://codingbat.com/prob/p165321

    Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod

    near_ten(12) â†’ True
    near_ten(17) â†’ False
    near_ten(19) â†’ True
    """
    return (num%10<=2 or num%10-10>=2) # Remove this line and add your implementation


def count_code(str):
    """
    https://codingbat.com/prob/p186048

    Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

    count_code('aaacodebbb') â†’ 1
    count_code('codexxcode') â†’ 2
    count_code('cozexxcope') â†’ 2
    """
    c=0
    for i in range(max(len(str)-3,0)):
        if str[i]=="c" and str[i+1]=="o" and str[i+3]=="e":
            c+=1
    return c # Remove this line and add your implementation


def end_other(a, b):
    """
    https://codingbat.com/prob/p174314

    Given two strings, return True if either of the strings appears at the very end of the other string, ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). Note: s.lower() returns the lowercase version of a string.

    end_other('Hiabc', 'abc') â†’ True
    end_other('AbC', 'HiaBc') â†’ True
    end_other('abc', 'abXabc') â†’ True
    """
    c=""
    d=""
    if len(a)<len(b):
        c+=a.lower()
        d+=b.lower()
    else:
        c+=b.lower()
        d+=a.lower()
    if c in d[len(d)-len(c):]:
        return True
    return False # Remove this line and add your implementation


def centered_average(nums):
    """
    https://codingbat.com/prob/p126968

    Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.

    centered_average([1, 2, 3, 4, 100]) â†’ 3
    centered_average([1, 1, 5, 5, 10, 8, 7]) â†’ 5
    centered_average([-10, -4, -2, -4, -2, 0]) â†’ -3
    """
    nums.sort()
    s=0
    for i in range(1,len(nums)-1):
        s+=nums[i]
    return int(s/(len(nums)-2)) # Remove this line and add your implementation


"""
https://www.cs.toronto.edu/~guerzhoy/180/midterm/mt2022/paper.pdf#page=7

Write a function that, when called, returns the next digit of Ï€ (approx 3.14159...). You may assume that
the function will not be called more than 10 times.

The function would be used like this:

print(next_digit_pi()) # 3
print(next_digit_pi()) # 1
print(next_digit_pi()) # 4
print(next_digit_pi()) # 1

You may import math and use math.pi
"""

import math


# Define any additional global variables here
cc=0
nu=math.pi
def next_digit_pi():
    global nu
    global cc
    i=nu//1
    nu=(nu%1)*10
    cc+=1
    return int(i) # Remove this line and add your implementation


if __name__ == "__main__":
    # Add any code to test your functions here
    print(string_times("H",10))
    print(front_times("1234",10))
    print(array123([1,2,2,2,3,1,2,4,3,1,2,3]))
    print(array_count9([1,2,3,9,4,5]))
    print(array_front9([1,3,9]))
    print(array_front9([1,2,3,4,5,6,9]))
    print(string_match("yeet","neet"))
    print(first_half("yeee"))
    print(without_end("abc"))
    print(combo_string("a","bb"))
    print(combo_string("bb","a"))
    print(left2("yeet"))
    print(near_ten(12))
    print(count_code("yeetcodecooecooo"))
    print(end_other("BOOOIIIIyeet","YEeT"))
    print(centered_average([1,2,3,4,8,5,6]))
    print(next_digit_pi())
    print(next_digit_pi())
    print(next_digit_pi())
    print(next_digit_pi())
