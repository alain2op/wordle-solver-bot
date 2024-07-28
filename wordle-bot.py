
def find_missing_letters(response,word):
    indices=[i for i,char in enumerate(response) if char=='0' ]
    letters=[word[i] for i in indices]
    return letters

def positioned_letters(response,word):
    indices=[i for i,char in enumerate(response) if char=='2']
    positioned_pairs=[(i,word[i]) for i in indices]
    return positioned_pairs

def non_positioned_letters(response,word):
    indices=[i for i,char in enumerate(response) if char=='1']
    non_positioned_pairs=[(i,word[i]) for i in indices]
    return non_positioned_pairs

def spit_top_words(word_list,count_list):
    max_word_list=[]
    for word in word_list:
        sum=0
        used_letters=[]
        for letter in word:
            if letter not in used_letters:
                sum+=count_list[ord(letter)-ord('a')]
                used_letters.append(letter)
        if len(max_word_list)<7:
            max_word_list.append((word,sum))
        else:
            if sum>max_word_list[0][1]:
                max_word_list[0]=(word,sum)
        max_word_list=sorted(max_word_list,key=lambda k:k[1])
    return max_word_list[::-1]

def word_add(nword_list,word,ncount_list):
    nword_list.append(word)   
    for letter in word:
        ncount_list[ord(letter)-ord('a')]+=1
    return nword_list,count_list

def update_word_list(word_list,chosen_word,response):
    missing_letters=find_missing_letters(response,chosen_word)
    positioned_pairs=positioned_letters(response,chosen_word)
    non_positioned_pairs=non_positioned_letters(response,chosen_word)
    nword_list=[]
    ncount_list=[0]*26
    for word in word_list:
        chosen=True
        for letter in missing_letters:
            if letter in word:                
                chosen=False
                break
        for i,char in positioned_pairs:
            if word[i]!=char:               
                chosen=False
                break
        for i,char in non_positioned_pairs:
            if char not in word or word[i]==char:                
                chosen=False
                break
        if chosen:
            nword_list.append(word)   
            for letter in word:
                ncount_list[ord(letter)-ord('a')]+=1
    return nword_list,ncount_list

possible_words=[]
words=open("wordle-dictionary.txt",'r')
count_list=[0]*26
for word in words:
    possible_words.append(word.strip())
    for letter in word.strip():
            count_list[ord(letter)-ord('a')]+=1
words.close()
top_words=spit_top_words(possible_words,count_list)
print(top_words)

chosen_word=input("What's the word chosen: ").strip()
response=input("What's the wordle response: ").strip()
while(response!="!" and len(possible_words)>1):
    if len(chosen_word)!=5 and len(response)!=5:
        print("Error in data provided. Try again or type ! to exit ")
    else:
        possible_words,count_list=update_word_list(possible_words,chosen_word,response)
        top_words=spit_top_words(possible_words,count_list)
        print(len(possible_words))
        print(top_words)
    chosen_word=input("What's the word chosen: ").strip()
    response=input("What's the wordle response: ").strip()

if(len(possible_words)<=1):
    print("I bet you got the word right.")