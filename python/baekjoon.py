while(True) :
    n = int(input())

    if(n == -1) :
        break
    else :
        measure = []
        result = ''
        for i in range(1, n, 1) :
            if((n % i) == 0) :
                measure.append(i)

        if(sum(measure) == n) :

            result += "%d = " % n

            for num in measure :
                result += "%d + " % num
            
            print(result[:len(result)-3])
        else :
            print(n, "is NOT perfect.")