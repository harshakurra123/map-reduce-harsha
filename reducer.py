
s = open("sorter_output.txt","r")
r = open("reducer_output.txt", "w")

thisKey = ""
thisValue = 0.0
final_list = []


for line in s:
  final_dict = {}
  data = line.strip().split('\t')
  store, amount = data
  if store != thisKey:
    if thisKey:

      # output the last key value pair result
      
      final_dict["key"] = thisKey
      final_dict["amount"] = thisValue
      final_list.append(final_dict)

    # start over when changing keys
    thisKey = store
    thisValue = 0.0

  # apply the aggregation function
  thisValue += float(amount)

# output the final entry when done

final_dict["key"] = thisKey
final_dict["amount"] = thisValue
final_list.append(final_dict)
sorted_amounts = sorted(final_list, key=lambda final_dict: final_dict['amount'], reverse=True)
for sorted_record in sorted_amounts:
    print(sorted_record)
    r.write(sorted_record["key"] + '\t' + str(sorted_record["amount"])+'\n')
s.close()
r.close()