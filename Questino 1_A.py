L1=["HTTP","HTTPS","FTP","DNS"]
L2=[80,443,21,53]
D={}
for i in range(len(L1)):
    D[L1[i]]=L2[i]
print(D)    