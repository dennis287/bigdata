import sys

countrytemp = {}
countryocc = {}

for line in sys.stdin:
    line = line.strip()

    words = line.split()
    j = 0

    for word in words:
        if j == 0:
            country = word
        else:
            temp = word
        j = j + 1

    if country in countrytemp.keys():
        countrytemp[country] += int(temp)
    else:
        countrytemp[country] = int(temp)
    if country in countryocc.keys():
        countryocc[country] += 1
    else:
        countryocc[country] = 1

for country in countrytemp:
    print(country + ": " + str(countrytemp[country]/countryocc[country]))
