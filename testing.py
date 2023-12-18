# digits=[0]


# if (len(digits)<2) & (digits[0]==9):
#     digits[:]=[1,0]
# elif (len(digits)<2) & (digits[0]!=9):
#     digits[:]=[digits[0]+1]
# elif (len(digits)==2) & (digits[1]==9) & (digits[0]!=9): 
#     digits0=[digits[0]+1]
#     digits1=[0]
#     digits[:]= digits0 +digits1
# elif (len(digits)==2) & (digits[0]==9) & (digits[1]==9):
#     digits0=[1]
#     digits1=[0]
#     digits2=[0]

#     digits[:]= digits0 +digits1+digits2
#     print("this")
# else:
#     print("or")   
#     list1= [digits[-1:][0]+1]
#     digits[:]=digits[:-1]+list1

# print(digits)

# nums=[0,0,1]

# i=0
# k=0
# while i<len(nums):
#     if(nums[i]==0):
#         print(i)
#         del nums[i]
#         print(nums)
#         print(i)
#         nums[:]=nums + [0]
#         print(nums)
#         i-=1
#     #print(i)
#     i+=1
#     k=k+1
#     if(k==len(nums)):
#         break

# print(nums)
 
from asyncio import isfuture


board=[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]



for i in range (0, len(board[0])):
    board[i]=[value for value in board[i] if value != "."]
    print(board[i])



# i=0
# j=0

# while i<len()





# print(board[0][0])
# for i in range(0, 9):
#     for j in range (0, 9):
#         if (board[i][j]=="."):
#             del board[i][j]
#             print(board)

# print(board)

