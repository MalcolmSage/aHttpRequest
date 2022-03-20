import sys, json, requests




def data_input():
# Read input from stdin in newline format
    print("Enter the urls:\n")   
    userInput = sys.stdin.readlines()
    return userInput


if __name__ == "__main__":
    data_input()