def maximo(resp,k):
  max_k = 0  
  for i in range(len(resp[k])):
    if(abs(resp[k][i]-resp[k-1][i])>max_k):
        max_k = abs(resp[k][i]-resp[k-1][i])
  return max_k
  
def isolar(matriz):
    for i in range(len(matriz)):
        divisor = matriz[i][i]
        for j in range(len(matriz[i])):
            if j == i:
                matriz[i][j] = 0
            elif j == len(matriz[i])-1:
                matriz[i][j] = matriz[i][j]/divisor
            else:
                matriz[i][j] = (-matriz[i][j]/divisor)
    return matriz

def aproxima(matriz, k, resp):
    new_resp = []
    for i in range(len(matriz)):
        soma = 0
        for j in range(len(matriz)):
            if i!=j:
                soma += matriz[i][j]*resp[k-1][j]
        xi = soma + matriz[i][j+1]
        new_resp.append(xi)
    return new_resp

def jacobi(matriz,tol):
    k = 1
    resp =[[0]*len(matriz)]
    matriz = isolar(matriz)
    resp.append(aproxima(matriz, k, resp))
    print((aproxima(matriz, k, resp)))
    while maximo(resp,k)>tol:
      k+=1
      resp.append(aproxima(matriz, k, resp))
      print((aproxima(matriz, k, resp)))
    return "Número de iterações: {0}\nRespostas: {1}".format(k,resp[k]) 
        
x = [
  [10, -1, 2, 0, 6],
  [-1, 11, -1, 3, 25],
  [2, -1, 10, -1, -11],
  [0, 3, -1, 8, 15]]

# y = [[2,1,2],[1,-2,-2]]

# a = [[3,-1,1,1],[3,6,2,0],[3,3,7,4]]
# b = [[10,-1,0,9],[-1,10,-2,7],[0,-2,10,6]]
# c = [[10,5,0,0,6],[5,10,-4,0,25],[0,-4,8,-1,-11],[0,0,-1,5,-11]]
# d = [[4,1,1,0,1,6],[-1,-3,1,1,0,6],[2,1,5,-1,-1,6],[-1,-1,-1,4,0,6],[0,2,-1,1,4,6]]
print("\nMétodo de Jacobi\n")
print(jacobi(x,10**(-3)))
# print(jacobi(y,0.1))
# print("\nA)  " +jacobi(a,0.01))
# print("\nB)  " +jacobi(b,0.01))
# print("\nC)  " +jacobi(c,0.01))
# print("\nD)  " +jacobi(d,0.01))