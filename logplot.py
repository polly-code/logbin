def logplot (data_x, data_y, err_y=None, numdots=20, ptf='Deafault path'):
    '''replot data from linear space to logspace with evenly distributed dots.
    data_x, data_y - arrays of x,y
    err_y - y error
    numdots - number of values on the future graph'''
    import numpy as np
    import matplotlib.pyplot as plt
    newdata_y=[]
    newdata_x=[]
    newdata_err_y=[]
    distr=np.logspace(np.log10(min(data_x)),np.log10(max(data_x)),num=numdots*2+1)
    for i in range(1,len(distr),2):
        val=0
        val_err_y=0
        counter=0
        for j in range(len(data_x)):
            if data_x[j] > distr[i-1] and data_x[j] < distr[i+1]:
                val += data_y[j]
                counter += 1
                if err_y is not None:
                    val_err_y+=err_y[j]
        if counter>0:
            newdata_y.append(val/counter)
            if err_y is not None:
                newdata_err_y.append(val_err_y/counter)
            newdata_x.append(distr[i])
    if err_y is None:
        plt.loglog(newdata_x, newdata_y,'ro')
        plt.savefig(ptf+'.png', dpi=300)
        f1=open(ptf+'log','w')
        for i in range(len(newdata_y)):
            f1.write('%f\t%f\n'%(newdata_x[i],newdata_y[i]))
    else:
        ax=plt.subplot()
        ax.set_yscale('log')
        ax.set_xscale('log')
        plt.errorbar(newdata_x,newdata_y,yerr=newdata_err_y, fmt='--bo')
        plt.savefig(ptf+'.png', dpi=300)
        f1=open(ptf+'log','w')
        for i in range(len(newdata_y)):
            f1.write('%f\t%f\t%f\n'%(newdata_x[i],newdata_y[i],newdata_err_y[i]))
    f1.close()
    
# Main
    
path = 'enter your path'
f=open(path)
x=[]
y=[]
yr=[]
init=True
for line in f:
    if len(line)>1:
        if init:
            init=False
            continue
        a,b=line.split() #change to a,b,err=line.split() in case of std
        x.append(float(a))
        y.append(float(b))
        #yr.append(float(err))
f.close()
#logplot(x,y,err_y=yr, ptf=path)
logplot(x,y,ptf=path)
