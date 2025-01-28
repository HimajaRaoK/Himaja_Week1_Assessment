sentence=input("Enter sentence: ")
words=sentence.split()  
word_count = {}  
for word in words:
    if word in word_count:
        word_count[word]+=1  
    else:
        word_count[word]=1 


total_words = len(words)
print(f"\nTotal word count: {total_words}")

for word, count in word_count.items():
    print(word, ":", count)

