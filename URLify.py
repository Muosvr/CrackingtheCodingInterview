def urlify (str):
    arr = list(str)
    for i in range(len(arr)):
        if arr[i] == " ":
            arr[i]="%20"
    return "".join(arr)

# if __name__=="__main__":
#     print(urlify("This is an apple tree"))


def unUrlify (str):
    arr = str.split("%20")
    return " ".join(arr)

sentence = raw_input("Please enter a sentence: ")
print urlify(sentence)
print unUrlify(urlify(sentence))
