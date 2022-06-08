# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    openfile = open(filename,"r")
    read_file_content = openfile.read()
    return read_file_content



def count_words():
    text = read_file_content("./story.txt")
    # print(text)
    # [assignment] Add your code here
    newtext = text.split()
    count = dict()

    for word in newtext:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

a = count_words()
print(a)