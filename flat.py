def flat(a,i,b):
    l = len(a);
    c = [];
    if (i < l):
        if (isinstance(a[i],list) == False):
            b.append(a[i]);
            return flat(a,i+1,b);
        else:
            b = b+flat(a[i],0,c);
            return flat(a,i+1,b);
    else:
        return b;




def main():
    x = [1,2,3];
    t = [1,1,1];
    u = [2,2,2];
    y = [1,x,t];
    b = [1,y,u];
    c = [];
    a = [];
    a = flat(b,0,c);
    print (a);
main();
