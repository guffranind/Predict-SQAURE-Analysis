from flask import Flask,render_template,request
import math

#Flask_app='temp.py'
app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def square(num):
    print("This calcualtor is used to find least subtract/add/multiply/divisibale number")
    print("                   to get a perfect square                                  ")
    #num=int(request.form['id'])
    #a=int(input("Enter an interger to find perfect square- "))
# to get lease subtract number
    sq=int(math.sqrt(num))
    s=sq**2
    dif=num-s
# to get lease add number
    sq2=sq+1
    s=sq2**2
    dif2=s-num
   
    # to get least multiply
#def prime_factors(num):
    org=int(num)
    l1=[]
    l2=[]
    while num % 2 == 0:  
        #print(2,)  
        num = num / 2
        l1+=[2]
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:  
            #print(i,)  
            num = num / i  
            l1+=[i]
    if num > 2:  
        #print(num)
        l1+=[num]
    for k in set(l1):
        chk=l1.count(k)
        if chk>1:
            chk2=int(chk/2)
            while chk2==1:
                l1.remove(k)
                chk2=chk2-1
        if chk%2!=0:
            #print("no prime",k)
            l2+=[k]
    #print(l2)
    li_mu=1
    for x in l2:
        li_mu=int(li_mu*x)
    li_min=int(li_mu*org)
    li_sq=int(math.sqrt(li_min))
    div_mu=li_mu
    div_min=int(org/div_mu)
    div_sq=int(math.sqrt(div_min))
    #print('Least multiply number is      {f} \n   and perfect square is      {l}'.format(f=li_mu,l=li_sq))
    #print('Least divide number is        {f} \n   and perfect square is      {l}'.format(f=div_mu,l=div_sq))
    ml=str(li_mu)
    ms=str(li_sq)
    dl=str(div_mu)
    ds=str(div_sq)
    #result=(ml,ms,dl,ds)
    #return result      
# to get least multiply
    al=str(dif2)
    als=str(sq2)
    sl=str(dif)
    sls=str(sq)
   # result=(al,als,sl,sls,ml,ms,dl,ds)
    u='least subtract number is '+sl+' and perfect square is \n '+sls
    v=' ,least add number is '+al+' and perfect square is '+als
    w=' ,least multiply number is '+ml+' and perfect square is '+ms
    y=' ,least divide number is '+dl+' and perfect square is '+ds
    z=u+v+w+y
    #print('Least subtract number is      {f} \n   and perfect square is      {l}'.format(f=dif,l=sq))
    #print('Least add number is           {f} \n   and perfect square is      {l}'.format(f=dif2,l=sq2))
    return z
    

@app.route('/',methods=['POST']) 
def getvalue():
    num=int(request.form['id'])
    #a=int(request.form['id'])
    #b=square()
    #print(b)
    #return b
    return render_template('index.html',x=square(num))
    
if __name__ == '__main__':
    app.run(debug=True)
