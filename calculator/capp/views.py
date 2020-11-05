from django.shortcuts import render

# Create your views here.
def cal(req):
    print(req.method)
    c = 0



    if req.method=="POST":

        ope=req.POST.get('op')
        t1=req.POST.get('n1')
        t2=req.POST.get('n2')
        if ope=="add" and t1.isnumeric() and t2.isnumeric():
            c=int(t1)+int(t2)
            print("addition is:",c)
        elif ope=="sub" and t1.isnumeric() and t2.isnumeric():
            c=int(t1)-int(t2)
            print("substraction is:",c)
        elif ope=="multi" and t1.isnumeric() and t2.isnumeric():
            c=int(t1)*int(t2)
            print("multiplication is:",c)
        elif ope=="div" and t1.isnumeric() and t2.isnumeric():
            try:
                if t2!=0:
                    c=int(t1)/int(t2)
                    print("division is:",c)
            except ZeroDivisionError as e:
                msg=e
                return render(req,"capp/addition.html",{"msg":msg})


        else:
            msg="Please enter valid inputs !"
            return render(req,"capp/addition.html",{"msg":msg})

        return render(req, "capp/addition.html", {"c": c})

    return render(req,"capp/addition.html")



