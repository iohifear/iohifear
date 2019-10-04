import numpy as np

MyPath="C:/Ian/Personal/CIT_Course/Coding/COMP9058/TSPdata/TSP dataset/"
Myfile_1 = MyPath + "inst-2.tsp"

RFull=np.genfromtxt(Myfile_1,dtype=float,delimiter=" ",skip_header=True)

InitCost=0
Fl_Size=len(RFull)
#****** Iterate through all the file entries ******
for n in range(Fl_Size):
    RCan=RFull
    #****** Generate a Random Starting Node ******
    Indx=n
    #****** Save the Starting Node ******
    I_n=RCan[Indx]
    #****** Initialize variables ******
    I_i=I_n;    Cost=0;     TotCost=0

    for x in range(Fl_Size-1):
        #** Remove Current Node so as to allow min distance calc (otherwise it will = 0)
        RCan=np.delete(RCan,Indx,0)
        #** Calculate the distances to all Nodes from the current node
        DistArr=np.sqrt(np.square(RCan[:,1]-I_i[1]) + np.square(RCan[:,2]-I_i[2]))
        #** Calculate the Index of the Next Node
        Indx=np.argmin(DistArr)
        #** Calculate the distance/cost to the nearest Node
        Cost=min(DistArr)
        #** Integrate the Cost
        TotCost += Cost
        #** Save the current Node as it will be removed in the 1st line of the loop
        I_i=RCan[Indx]       
          
    if (n==0) or (TotCost<InitCost):
        InitCost=TotCost;        TotNode=int(I_n[0])
        
print("Starting Node # with least Cost =",TotNode,",Cost =",int(InitCost))

