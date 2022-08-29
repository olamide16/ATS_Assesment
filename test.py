#------Anagrams-------
# def are_anagrams(s1,s2):
#     if len(s1) != len(s2):
#         return False
#     freq1 = {}
#     freq2 = {}
#     for i in s1:
#         if i in freq1:
#             freq1[i] += 1
#         else:
#             freq2[i] = 1
#     for key in freq1:
#         if key not in freq2 or freq1[key] != freq2[key]:
#             return False
#     return True
# age = int(input("How old are you? "))
# if age == 10:
#     print ("You can't ride the roller coaster.")
# elif age == 13:
#     print ("You can ride the roller coaster!")
# elif age == 14:
#     print ("You can ride the roller coaster!")
# language = input("what's your programming language? ")
# if language == "Python":
#     print("Nice choice!")
# elif language == "Golang":
#     print("You're a cool kid I see...") 
# elif language == "JavaScript":
#     print("Okay Mr. web developer.")
# else:
#     print("I don't know that language.")
# sum1 = int(input("Enter a number: "))
# sum2 = int(input("Enter another number: "))
# sum_all = sum1 + sum2
# if sum_all <= 100:
#     print(f"The sum of there two number is {sum_all}")
# else:
#     print(f"The sum of there two number is {sum_all}\n That is a large sum!")
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    # Write your code here.
    A = []
    while head:
        A.append(head)
        head = head.next
    A[-1]. next, k = A[0], -k % len(A)
    A[k-1].next = None
    return A[k]

def maxProfitWithKTrasnsactio(prices, k):
    cache = {}
    def helper(index,buy,cap):
        key = "{}-{}-{}".format(index,buy,cap)
        if key in cache:
            return cache[key]
        if index == len(prices) or cap == 0:
            return 0

        profit = 0
        if buy:
            profit = max(-prices[index]+helper(index+1,0,cap),
                         helper(index+1,1,cap)
                        )
        else:
            profit = max(prices[index]+helper(index+1,1,cap-1),
             helper(index+1,0,cap)
            )

        cache[key] = profit
        return cache[key]
    return helper(0,1,k)