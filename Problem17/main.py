#NOTE: THIS PROBLEM IS NOT SOLVED

singles = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
decimals = ["ten","twenty","thirty","fourty","fifty","sixty","seventy","eighty","ninety"]
hundreds = [x+"hundred" for x in singles[:-1]]
thousand = "one thousand"

def makeDez(dez,sing):
    ret = []
    ret.append(dez)
    for i in sing:
        ret.append(dez+i)
    return(ret)

nums = []
for i in singles:
    nums.append(i)
for i in range(1,len(decimals)):
    twen = makeDez(decimals[i],singles[:9])
    [nums.append(i) for i in twen]

firstHundred = nums
firstHunCount = sum ([len(i) for i in firstHundred])
count = firstHunCount
for i in hundreds:
    count+=len(i)*100+99*3+firstHunCount

#add thousand
count += len("onethousand")
print(count)