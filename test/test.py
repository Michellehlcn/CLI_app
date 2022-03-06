import pandas as pd
import json
import statistics


with open(r'purchases_v1.json', "r") as f:
    data = json.load(f)
    df = pd.json_normalize(data)

    value1,price1,name1,quant1= [],[],[],[]
    value2,price2,name2,quant2= [],[],[],[]

    for i in df['items']:
        for item in i:   
            #Value of each items          
            price1.append(float(item['price']))
            quant1.append(float(item['quantity']))
            value1.append(float(item['price'])*float(item['quantity']))
            name1.append(item['product_name'])

        #Sum of each purchase:
    for x in range(0,len(value1)):
        if (x %2) ==0:
            value2.append(value1[x]+value1[x+1])
        else:
            continue
    a = len(value2) #Total number of purchases
    b = sum(value2) #Total volume of spend
    c = sum(value2)/len(value2) #Average purchase value
    d = max(value2) #Maximum purchase value
    e = statistics.median(sorted(value2)) #Median purchase value
    f = len(list(set(name1))) #Number of unique products purchased

    result = {'Total number of purchases':a, 'Total volume of spend': b, 'Average purchase value':c,'Maximum purchase value':d,'Median purchase value': e,'Number of unique products purchased':f}
    print(json.dumps(result, indent =4 , sort_keys = False))