import random as rand
# python3
# This algorithm takes more time
# def max_pairwise_product(numbers):
#     n = len(numbers)
#     max_product=numbers[0]
#     if n != 1:
#         max_product = 0
#     for first in range(n):
#         for second in range(first + 1, n):
#             max_product = max(max_product,
#                 numbers[first] * numbers[second])
#     return max_product
def max_pairwise_product_fast(numbers):
    n = len(numbers)
    max_index1 = -1
    for i in range(n):
        if(max_index1== -1)|(numbers[i]>numbers[max_index1]):
            max_index1 = i
    if n!=1:
      max_index2= -1
      for j in range(n):
         if j!=max_index1:
             if((max_index2== -1)|(numbers[j]>numbers[max_index2])):
                 max_index2=j
      return (numbers[max_index1] * numbers[max_index2])
    else:
        return numbers[max_index1]

if __name__ == '__main__':
  input_n = int(input())
  input_numbers = [int(x) for x in input().split()]
  print(max_pairwise_product_fast(input_numbers))

  # STRESS TESTING
  # while(True):
  #     n=rand.randint(1,3)
  #     print("",n)
  #     a=[]
  #     for j in range(n):
  #         a.append(rand.randint(0,100000))
  #     for i in range(n):
  #         print(a[i],end=" ")
  #     res1=max_pairwise_product(a)
  #     res2=max_pairwise_product_fast(a)
  #     if(res1!=res2):
  #         print(" \nwrong answer ",res1," ",res2," ")
  #         break
  #     else:
  #         print("\nOK")


