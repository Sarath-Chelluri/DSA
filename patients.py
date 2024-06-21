def avg_time(pati):
    d_start = pati[0][0]
    total_time = 0
    for i in pati:
        if i[0] > d_start:
            d_start = i[0]
        d_start += i[1]
        total_time = d_start - i[0]
        

    return total_time//len(pati)





print(avg_time([[5,2],[5,4],[10,3],[20,1]]))