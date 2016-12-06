


def hammingdistance(a, b):
    i = 0
    dist = 0

    for i in range(len(a)):
        if (a[i] != b[i]):
            dist = dist + 1

    return dist

l=int(raw_input("Enter Motif Length: "))
d=int(raw_input("Enter No of Mismatches: "))
gene = ["GCGCGAT","CAGGTGA","CGATGCC"]
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
i=0
j=0
k=0
m=0
flag=0
count=0
for i in range(0,len(dictA)):
    j=0
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

setB.remove(0)
print  "Motifs:"
print setB