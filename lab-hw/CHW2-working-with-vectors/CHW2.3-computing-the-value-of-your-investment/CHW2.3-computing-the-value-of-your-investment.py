def investment(p1,p2,p3,assets,t):

  # write your code here
  value = assets[0] * p1[t] + assets[1] * p2[t] + assets[2] * p3[t]
  return value