import construction_matrice_K as cons_K


#A = adjacency matrix, u = vertex u, v = vertex v
def weight(A, u, v):
    return A[u][v]

#A = adjacency matrix, u = vertex u
def adjacent(A, u):
    L = []
    for x in range(len(A)):
        if A[u][x] > 0 and x != u:
            L.insert(0,x)
    return L

#Q = min queue
def extractMax(Q):
    q = Q[0]
    Q.remove(Q[0])
    return q

#Q = max queue, V = vertex list
def decreaseKey(Q, K):
    for i in range(len(Q)):
        for j in range(len(Q)):
            if K[Q[i]] > K[Q[j]]:
                s = Q[i]
                Q[i] = Q[j]
                Q[j] = s

#V = vertex list, A = adjacency list, r = root
def prim(V, A, r):
    u = 0
    v = 0
    cost=0
    # initialize and set each value of the array P (pi) to none
    # pi holds the parent of u, so P(v)=u means u is the parent of v
    P=[None]*len(V)

    # initialize and set each value of the array K (key) to some large negative number (simulate infinity)
    K = [-999999]*len(V)

    # initialize the max queue and fill it with all vertices in V
    Q=[0]*len(V)
    for u in range(len(Q)):
        Q[u] = V[u]
    # set the key of the root to 0
    K[r] = 0
    decreaseKey(Q, K)    # maintain the max queue

    # loop while the min queue is not empty
    while len(Q) > 0:
        u = extractMax(Q)    # pop the first vertex off the max queue

        # loop through the vertices adjacent to u
        Adj = adjacent(A, u)
        for v in Adj:
            w = weight(A, u, v)    # get the weight of the edge uv

            # proceed if v is in Q and the weight of uv is less than v's key
            if Q.count(v)>0 and w > K[v]:
                # set v's parent to u
                P[v] = u
                # v's key to the weight of uv
                K[v] = w
                decreaseKey(Q, K)    # maintain the max queue
    list=[]
    for i in range(len(V)):
        if P[i]!=None:
            a=P[i]*1
            cost= cost+ A[a][i]  
            list.append(A[a][i])
        else:
            list.append(None)
    return P,cost,list




A1=[]

Mat1= cons_K.Mat_adjac
Mat2=cons_K.Mat_prob


  

V=[]
for i in range(len(Mat1)):
    V.append(i)

def all_prim(V,A):
    for i in range(len(V)):
        print(prim(V,A,i)[0],prim(V,A,i)[1],"\n")

   


print("Avec S: \n",prim(V,Mat1,1)[0],prim(V,Mat1,1)[1]," \n")
print("Avec K :\n",prim(V,Mat2,1)[0],prim(V,Mat2,1)[1]," \n")
#
def decision_adapt(n):
  result= prim(V,Mat2,n)[0]
  for i in range(len(result)):
      if i!=n and result[i]==None:
          if i<len(Mat2)-1:
              result[i]=i+1
          else:
              result[i]=i-1
  return(result)
print("adapté: \n",decision_adapt(1))

#all_prim(V,Mat1)
#
#def decision_pertinance_arbre(prim_Gauche,prim_Droit):
#    poids=0
#    liste_poids=[]
#    arbre=[]
#    l_Gauche=prim_Gauche[0]
#    l_Droit=prim_Droit[0]
#    for i in range(len(l_Gauche)):
#        if l_Gauche[i]!=None and l_Gauche[i]<i:
#            l_Gauche[i]=None
#        if l_Droit[i]!=None and l_Droit[i]>i:
#            l_Droit[i]=None 
#    p_Gauche=prim_Gauche[2]
#    p_Droit=prim_Droit[2]
#    
#    for i in range(len(l_Gauche)):
#        if l_Gauche[i]!=None and l_Droit[i]!=None:
#            if p_Gauche[i]>=p_Droit[i]:
#                arbre.append(l_Gauche[i])
#                poids=poids+p_Gauche[i]
#                liste_poids.append(p_Gauche[i])
#            else:
#                 arbre.append(l_Droit[i]) 
#                 poids=poids+p_Droit[i]
#                 liste_poids.append(p_Droit[i])
#        elif  l_Gauche[i]==None and l_Droit[i]!=None:
#              arbre.append(l_Droit[i])
#              poids=poids+p_Droit[i]
#              liste_poids.append(p_Droit[i])
#        elif l_Droit[i]==None and   l_Gauche[i]!= None:
#              arbre.append(l_Gauche[i])
#              poids=poids+p_Gauche[i]
#              liste_poids.append(p_Gauche[i])
#        elif l_Droit[i]==None and l_Gauche[i]==None:
#              arbre.append(None)
#              liste_poids.append(None)
#    return(arbre,poids)
    

    

    