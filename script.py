import sys, json, requests



def outputPackaging(response):
    prepackaged = {
        "Status-code": response.status_code,
    }
    packaged = json.dumps(prepackaged)
    # print(packaged)
    return packaged


def request_handling(request):
    response = requests.get(request)
    response.close()
    return outputPackaging(response)

def data_handling(data):
# Take in the data as list
    print("Please wait")
    url_list = data.split('\n')[:-1]
    outputFile = "stdout.txt"
    newList = open(outputFile, "w")
    
    # iterate through list
    for url in url_list:
        # handle request in request_handling
        newList.write(request_handling(url))
        
    print("Done")
    return url_list

def data_input():
# Read input from stdin in newline format
    print("Enter the urls:\n")   
    user_input = ""
    for line in sys.stdin:
        if line == '\n':
            break
        user_input += line
    return data_handling(user_input)


if __name__ == "__main__":
    data_input()