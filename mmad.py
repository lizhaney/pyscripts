import csv

with open('march.csv', mode='r') as infile:
    reader = csv.reader(infile)
    with open('mmad_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        mydict = {rows[0]:rows[1] for rows in reader}

## take index values 0,1. sort 

values = mydict.values()
smallIndex = values.index(min(values))

keys = mydict.keys()
smallKey  = keys[smallIndex]

print mydict
print "SmallKey"
print smallKey

## take 1 , 2 values index and find min

print mydict.items()

import csv
delimiter = ','
result = {}
with open("march.csv", 'r') as data_file:
    data = csv.reader(data_file, delimiter=delimiter)
    headers = next(data)[1:] # month names starting from 2nd column in csv
    for row in data:
        temp_dict = {}
        name = row[0]
        values = []
        # converting each value from string to int / float
        # (as suggested by OP's example)
        for x in row[1:]:
            try:
                values.append(int(x))
            except ValueError:
                try:
                    values.append(float(x))
                except ValueError:
                    print("Skipping value '{}' that cannot be converted " +
                          "to a number - see following row: {}"
                          .format(x, delimiter.join(row)))
                    values.append(0)
        for i in range(len(values)):
            if values[i]: # exclude 0 values
                temp_dict[headers[i]] = values[i]
        result[name] = temp_dict    
print "print result"
print(result)
print"print temp_dict"
print temp_dict

## tried w errorssorted_list = sorted(result, key=lambda d: d['Order'], reverse=True)
# didn't work either result.sort(key=operator.itemgetter('Order'))

#SORTED TEAMS BY ORDER

print"\nSorted keys for result\n"
sorted_keys = sorted(result.keys(), key=lambda y: (result[y]['Order']))

print sorted_keys

print"\nSorted keys for Order\n"
## DOESN'T WORKsorted_keys2 = sorted(temp_dict.keys(), key=lambda y: (temp_dict[y]['Order']))

print "Who Would Win {0} or {1}".format(get.result[1],result[2])
