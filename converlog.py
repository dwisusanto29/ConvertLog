import sys 
import json
import argparse

fileinput = sys.argv[1]
fileoutpu = sys.argv[2]

i = 1
result = {}
with open(fileinput) as f:
    lines = f.readlines()
    for line in lines:
        r = line.split('] ')
        result[i] = {'timestamp': r[0].replace('[', ''), 'module': r[1].replace('[', ''), 'pid': r[2].replace('[', ''), 'message': r[3].replace('[', '')}
        i += 1

out_file = open(fileoutput, "w")
json.dump(result, out_file, indent = 4, sort_keys = False)
out_file.close()
