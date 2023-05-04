
def main():
    import csv
    f=open('seoul.csv','r',encoding='ANSI')
    data=csv.reader(f,delimiter=',')
    data2=csv.reader(f,delimiter=',')
    header=next(data)

        
    max_temp=-999
    max_date=''
    sum=0
    n=0
    min_temp=999
    min_date=''
    for row in data:
        if row[2]!='':
            row[2]=float(row[2])
            sum=sum+row[2]
            n=n+1
            if max_temp<row[2]:
                max_date=row[0]
                max_temp=row[2]
            if min_temp>row[2]:
                min_date=row[0]
                min_temp=row[2]

        
    f.close()
    avg=sum/n
    #print(max_date,max_temp)
    #print(min_date,min_temp)

    max_temp=round(max_temp,2)
    min_date=round(min_temp,2)
    avg=round(avg,2)
    #print(sum/n)
    print("***Annual Temperature Report for Seoul in 20022")
    print("Average Temperature:"+str(avg)+" Celsius")
    print("Average Minimum Temperature:"+str(min_temp)+" Celsius")
    print("Average Maximum Temperature:"+str(max_temp)+" Celsius") 

if __name__ == '__main__':
    main()

