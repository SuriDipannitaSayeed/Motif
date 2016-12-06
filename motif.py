
import time
start_time = time.time()


def hammingdistance(a, b):
    i = 0
    dist = 0

    for i in range(len(a)):
        if (a[i] != b[i]):
            dist = dist + 1

    return dist

def motiffinding(str,dictA,d):
    count=0
    motifcount=0
    m=0
    for i in range(len(dictA)):
        for j in range(len(dictA[i])):
            count=hammingdistance(str,list(dictA[i])[j])
            if(count<=d):
                motifcount=motifcount+1
                break
    j=0
    print str
    print motifcount
    return motifcount

l=int(raw_input("Enter Motif Length: "))
d=int(raw_input("Enter No of Mismatches: "))
gene = ["GCGCGAT",
        "CAGGTGA",
        "CGATGCC",
        ]

dictA = dict()

for j in range(len(gene)):

    gene_2 = [gene[j]]
    gene2=gene[j]
    for i in range(1, len(gene[j])):
        gene2 = gene2[1:len(gene[j])] + gene2[0]
        gene_2.append(gene2)
    print gene_2
    listA = []
    setA = {0}

    for k in range(0, len(gene_2)+1-l):
        setA.update({gene_2[k][0:l]})
        listA.append(gene_2[k][0:l])

    setA.remove(0)
    dictA[j] = setA



for i in range(len(dictA)):
    print dictA[i]

setB={0}
motif=[]
i=0
j=0
k=0
m=0
flag=0
count=0
for i in range(0,len(dictA)):
    j=0
    m=0
    while(m<len(dictA[i])):
        for j in range(0,len(dictA)):

            if(i!=j):
                while(k<len(dictA[j])):
                    flag=hammingdistance(list(dictA[i])[m],list(dictA[j])[k])
                    if(flag<=d):
                        setB.update({list(dictA[j])[k]})
                    k=k+1

            else:
                j=j+1
        k = 0
        m=m+1
        j=0


print("--- %s seconds ---" % (time.time() - start_time))
setB.remove(0)
for i in range(len(list(setB))):
    str=setB.pop()
    print "mo"+str
    motifcount=motiffinding(str,dictA,d)
    if(motifcount==(len(dictA))):
        motif.append(str)


print  "Motifs:"
print setB
print motif

'''gene = ["GCGCGAT",
        "CAGGTGA",
        "CGATGCC",
        ]'''