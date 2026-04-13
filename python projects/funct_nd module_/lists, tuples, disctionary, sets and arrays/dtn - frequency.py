strt = {"t": 2, "u": 3, "p": 2, "l": 2, "e": 1}
print(strt)
print(strt.items())

k = 2 #assigning "value" from key:value in dictinary

res = 0
for key in strt: #key represents key in key:value in dtn
    if strt[key] == k:
     res += 1
print("frequency of k(2) is ", str(res))