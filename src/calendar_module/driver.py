from util import get_day

if __name__=="__main__":
    d=int(input("Enter Day: "))
    m=int(input("Enter Month: "))
    y= int(input("Enter Year: "))
    res=get_day(d,m,y)
    print(res)