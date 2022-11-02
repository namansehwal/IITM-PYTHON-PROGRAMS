def get_summary(tran):
  
  result= list()
  for trans in tran: 
    cost = 0
    dic= dict()
    for element in trans['Items']:
        cost += element['Price']*element['Qty']
    dic['Cost'] = cost
    dic['TID'] = trans['TID']
    result.append(dic)
    
  
  return result