def main():
    import csv
    f=open('seoul.csv','r',encoding='ANSI')
    data=csv.reader(f,delimiter=',')
    header=next(data)
    max_temp=-999
    max_date=''
    min_temp=999
    min_date=''
    for row in data:
        if (row[4]!=''and row[3]!=''):
            row[4]=float(row[4])
            row[3]=float(row[3])
            if max_temp<(row[4]-row[3]):
                max_temp=row[4]-row[3]
                max_date=row[0]
            if min_temp>(row[4]-row[3]):
                min_temp=row[4]-row[3]
                min_date=row[0]
    f.close()
    max_temp=round(max_temp,1)
    min_temp=round(min_temp,1)

    print("***Annual Temperature Report for Seoul in 2022***")
    print("Day with the Largest Temperature Variation : "+str(max_date))
    print("Maximum Temperature Difference: "+str(max_temp))
    print("Day with Smallest Temperature Variation: "+str(min_date))
    print("Minimum Temperature Difference: "+str(min_temp))
if __name__ == '__main__':
    main()
