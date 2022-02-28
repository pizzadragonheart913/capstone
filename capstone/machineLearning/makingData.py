temp = [10,12,14,16,18,20,22,24,26,28,30]
dirthumi = ["enough","notenough"]
humi = [10,20,30,40,50,60,70,80,90,100]
lux = [0,2000,4000,6000,8000,10000,12000,14000,16000,18000,20000]

for a in temp:
    databuffer = ''
    print("\n")
    for b in dirthumi:
        for c in humi:
            for d in lux:
                print("\n")
                databuffer += str(a)
                databuffer += ','
                databuffer += str(b)
                databuffer += ','
                databuffer += str(c)
                databuffer += ','
                databuffer += str(d)
                print(databuffer, sep="\n")
                print()
                