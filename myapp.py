while True :
    from math import *
    def fib(a):
        fib = [0, 1, 1]
        for i in range(3, No+1) :
            fib.append(fib[i-2]+fib[i-1])
        return fib
    def morabe(a, b):
        mohit = 2 *(tool + arz)
        masahat = tool*arz
        return masahat , mohit
    selector = input('choose : Calculator of 2 Nombers(cal) , Calculate the perimeter and area(ea) , Factorial calculation(fact), Fibonacci numbers(fib) , Recognize being a prime number(pr) , The largest common denominator of two numbers(cd) , Algebra sets(set) , to close app(close): ')
    selector = selector.lower()
    if selector == 'ea' :
        tool = float(input('the length: '))
        arz = float(input('Width: '))
        print( 'area: %f and perimeter: %f ' % morabe(arz, tool))
    elif selector == 'fib':
        No = int(input('until the : '))
        print(fib(No))
    elif selector == 'pr' :
        Nom = int(input('Enter No : '))
        Up = ceil(sqrt(Nom))
        for m in range(2, Up) : 
            if Nom%m == 0 :
                print('%i is not prime!' % Nom)
                break
        else :
            print("%i is prime!" % Nom)
    elif selector == 'cd' :
        no1 = int(input('No1: '))
        no2 = int(input('No2: '))
        bmm = gcd( no1 , no2 )
        print('The largest common denominator of two numbers :', bmm )
        no3 = int(input('No3: '))
        bmm2 = gcd( bmm , no3 )
        print('The largest common denominator of two numbers :', bmm2 )
        no4 = int(input('No4: '))
        bmm3 = gcd(bmm2, no4)
        print('The largest common denominator of two numbers : ', bmm3)
        no5 = int(input('No5: '))
        bmm4 = gcd(bmm3, no5)
        print('The largest common denominator of two numbers : ', bmm4)
    elif selector == 'set' :
        a = [int(input( 'No1 a : ')) , int(input( 'No2 a : ')), int(input( 'No3 a : ')), int(input( 'No4 a : '))]
        b = [int(input( 'No1 b : ')) , int(input( 'No2 b : ')), int(input( 'No3 b : ')), int(input( 'No4 b : '))]
        zarbdd = [a[0]*b[0], a[0]*b[1], a[0]*b[2], a[0]*b[3], a[1]*b[0], a[1]*b[1], a[1]*b[2], a[1]*b[3], a[2]*b[0],a[2]*b[1], a[2]*b[2], a[2]*b[3] , a[3]*b[0], a[3]*b[1], a[3]*b[2],  a[3]*b[3]]
        gamdd = [a[0]+b[0], a[0]+b[1], a[0]+b[2], a[0]+b[3], a[1]+b[0], a[1]+b[1], a[1]+b[2], a[1]+b[3], a[2]+b[0],a[2]+b[1], a[2]+b[2], a[2]+b[3],  a[3]+b[0], a[3]+b[1], a[3]+b[2] , a[3]+b[3]]
        agtema = set(a)|set(b)
        tafazol = set(a)-set(b)
        tafazol2 = set(b)-set(a)
        eshterak = set(b)&set(a)
        zirma = 2**len(a)
        zirmb = 2**len(b)
        print('\n Number of subsets of a :' , zirma ,'\n Number of subsets of b :' , zirmb ,'\n Multiply sets by sets (persian : zarb doone be doone) : ',  zarbdd , '\n Collect one by two collections (persian : game doone be doone) : ', gamdd ,'\n a-b :',tafazol,'\n b-a :',tafazol2,'\n union of 2 sets : ', agtema, '\n intersection of 2 sets : ', eshterak)
    elif selector == 'fact' :
        N = int(input('no : '))
        print('%i! = %i' % (N, factorial(N)))
    elif selector == 'cal' :
        from myclass import calculator
        a = int(input('num1 : '))
        b = int(input('num2 : '))
        mycalc = calculator(a,b)
        selector = input('choose : Addition(a), Subtraction(sub), Multiplication(m), Division(d), All operations!(all) : ')
        selector = selector.lower()
        if selector == 'a' :
            print(a, '+', b, '=', mycalc.sum())
        elif selector == 'sub' :
            print(a, '-', b, '=', mycalc.Submission())
        elif selector == 'm' :
            print(a, '×', b, '=', mycalc.Multiplication())
        elif selector == 'd' :
            print(a, '÷', b, '=', mycalc.Division())
        elif selector == 'all' :
            print('', a, '+', b, '=', mycalc.sum() , '\n', a, '-', b, '=', mycalc.Submission(),'\n', a, '×', b, '=', mycalc.Multiplication(), '\n', a, '÷', b, '=', mycalc.Division())
        else : 
            print('Error!!!, please try again')
    elif selector == 'close' :
        break
    else :
        print('Error!!!, please try again')
