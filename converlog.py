import sys 
import json
import optparse

def json_convertion(fileinput, fileoutput):
    i = 1
    result = {}
    with open(fileinput) as f:
        lines = f.readlines()
        for line in lines:
            result[i] = line
            i += 1
    output_file = open(fileoutput, "w")
    json.dump(result, output_file, indent = 4, sort_keys = False)
    output_file.close()

def text_convertion(fileinput, fileoutput):
    output_file = open(fileoutput, "w")
    with open(fileinput) as f:
        lines = f.readlines()
        for line in lines:
            output_file.write(line)
    
if __name__=="__main__":
    parser = optparse.OptionParser("usage: %prog fileinput [options] fileoutput")
    parser.add_option("-t", "--type", dest="typefile", default="json", type="string" help="")
    parser.add_option("-o", "--output", dest="output")
    (options, args) = parser.parse_args()

    output_file = options.output
    type_file = options.typefile

    if(type_file == "text"):
        text_convertion(sys.argv[1], output_file)
    else:
        json_convertion(sys.argv[1], output_file )