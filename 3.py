infile=open('infile.txt','r')
outfile=open('outfile.txt','w')
m=0
username=input('enter your name: ')
l=[line.rstrip().split("answer") for line in infile]
for i in l:
    print(i[0])
    s=input('enter the answer ')
    if s == i[1]:
        m+=1
l=[username+"\n",str(m)]
for i in l:
    print(i,end=" ")
outfile.writelines(l)
infile.close()
outfile.close()
