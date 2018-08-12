def lcs(str1, str2):
  if len(str1) == 0 or len(str2) == 0:
    return ""
 
  if str1[-1] == str2[-1]:
    return lcs(str1[:-1], str2[:-1]) + str1[-1]
  t1 = lcs(str1[:-1], str2)
  t2 = lcs(str1, str2[:-1])
  if len(t1) > len(t2):
    return t1
  else:
    return t2

def commonSubstring(a, b):
  for i in range(len(a)):
    print(lcs(a[i], b[i]))
