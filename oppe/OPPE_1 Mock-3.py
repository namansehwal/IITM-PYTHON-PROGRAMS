# # # version alpha 1.0 (4/5 tests passed)
# def diagonal(D):
#     eligible = True
#     for x in range(len(D)):
#         for y in range(len(D)):
#             if x != y and D[x][y] != 0:
#                 eligible = False
#                 return eligible 
#     return eligible                    
                    
# def scaler(S):

#     first_element = S[0][0]
#     for x in range(len(S)):
#         for y in range(len(S)):
#             if x==y and S[x][y] != first_element:
#                 return False 
#     return True

# def identity(I):
#     eligible = True
#     for x in range(len(I)):
#         for y in range(len(I)):
#             if x == y and I[x][y] != 1:
#                 eligible = False
#                 return eligible          
#     return eligible

# def matrix_type(M):
    
#     if diagonal(M):
#         if scaler(M):
#             if identity(M):
#                 return('identity')
#             else:
#                 return('scaler')
#         else:
#             return('diagonal')                    
#     else:
#         return("non-diagonal")   





#version beta  (5/5 tests passed)

def matrix_type(M):
    flag = True
    count=0
    temp=M[0][0]
    c=True
    for i in range(len(M)):
        for j in range(len(M[i])):
            if i != j: #elements other than diagonal
                if M[i][j] != 0:
                    flag = False
                else:
                    flag = True
            if flag:
                if i==j:
                    if M[i][j]!=temp:
                        c=False
            else: #all elements 
                return "non-diagonal"
    if c==False:
        return "diagonal"
    else:
        if temp==1:
            return "identity"
        else:
            return "scalar"
        
    

