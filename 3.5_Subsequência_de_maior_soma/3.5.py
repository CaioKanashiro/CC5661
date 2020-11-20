  
def sms_pd(vetor):
    vetor_memo = [0 for i in range(len(vetor))]
    vetor_memo[0] = vetor[0]
    for i in range(1,len(vetor)):
        vetor_memo[i] = max(vetor_memo[i-1]+vetor[i],vetor[i])
    return max(vetor_memo)

print(sms_pd([-2,-3,4,-1,-2,0,1,5,-3]))
print(sms_pd([5,2,3,-2,80000,-4,-5,1]))