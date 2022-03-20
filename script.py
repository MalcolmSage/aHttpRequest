import sys, json, requests


def output_packaging(response):
    # created schema for processing
    prepackaged = {
        "Url": response.url,
        "Status-code": response.status_code,
        "Content-length": len(response.content)
    }

    # json packaging
    packaged = json.dumps(prepackaged)
    print(packaged)
    return packaged


def validation(url):
    # testing url is real
    try:
        response = requests.get(url)
        return True
    except:
        return False


def request_handling(request):
    response = requests.get(request)
    response.close()
    return output_packaging(response)


def data_handling(data):
    # Take in the data as list
    print("Please wait")
    url_list = data.split('\n')[:-1]
    outputFile = "stdout.txt"
    newList = open(outputFile, "w")

    # iterate through list
    for url in url_list:
        # handle request in request_handling
        if validation(url):
            newList.write(request_handling(url))
        else:
            pass

    print("Done")
    # returns url_list for testing
    return url_list


def data_input():
    # Read input from stdin in newline format
    print("Enter the urls:\n")
    user_input = ""
    for line in sys.stdin:
        if line == '\n':
            break
        user_input += line
        
    # returns data_handling for testing
    return data_handling(user_input)


if __name__ == "__main__":
    data_input()
