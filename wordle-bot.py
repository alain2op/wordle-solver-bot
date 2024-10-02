
def find_missing_letters(response,word,present_letters):#returns the letters that are not in the word
    indices=[i for i,char in enumerate(response) if char=='0' ]
    missing_letters=[word[i] for i in indices if word[i] not in present_letters]
    return missing_letters,present_letters

def positioned_letters(response,word,present_letters):#returns the letters that are in the word at the correct position
    indices=[i for i,char in enumerate(response) if char=='2']
    positioned_pairs=[(i,word[i]) for i in indices]
    present_letters=[char for i,char in positioned_pairs if char not in present_letters]
    return positioned_pairs,present_letters

def non_positioned_letters(response,word,present_letters):#returns the letters that are in the word but not at the correct position
    indices=[i for i,char in enumerate(response) if char=='1']
    non_positioned_pairs=[(i,word[i]) for i in indices]
    present_letters+=[char for i,char in non_positioned_pairs if char not in present_letters]
    return non_positioned_pairs,present_letters

def spit_top_words_to_exploit(word_list,count_list):
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

def spit_top_words_to_explore(word_list,count_list,unused_letters):
    max_word_list=[]
    for word in word_list:
        sum=0
        used_letters=[]
        for letter in word:
            if letter not in used_letters:
                sum+=count_list[ord(letter)-ord('a')]
                used_letters.append(letter)
                if(letter in unused_letters):
                    sum+=10000
        if len(max_word_list)<7:
            max_word_list.append((word,sum))
        else:
            if sum>max_word_list[0][1]:
                max_word_list[0]=(word,sum)
        max_word_list=sorted(max_word_list,key=lambda k:k[1])
    return max_word_list[::-1]

def update_word_list(word_list,chosen_word,response,present_letters):
    positioned_pairs,present_letters=positioned_letters(response,chosen_word,present_letters)
    non_positioned_pairs,present_letters=non_positioned_letters(response,chosen_word,present_letters)
    missing_letters,present_letters=find_missing_letters(response,chosen_word,present_letters)
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


#main

possible_words=[]

present_letters=[]
unused_letters=[chr(i) for i in range(ord('a'),ord('z')+1)]


answer_words=open("wordle-answer-dictionary.txt",'r')
count_list=[0]*26
for word in answer_words:
    possible_words.append(word.strip())
    for letter in word.strip():
            count_list[ord(letter)-ord('a')]+=1
answer_words.close()

top_words_to_exploit=spit_top_words_to_exploit(possible_words,count_list)
print("Top words to exploit:",top_words_to_exploit,'\n')



guess_words=open("wordle-guess-dictionary.txt",'r')
guess_words_list=[]
for word in guess_words:
    guess_words_list.append(word.strip())
guess_words.close()

top_words_to_explore=spit_top_words_to_explore(guess_words_list,count_list,unused_letters)
print("Top words to explore:",top_words_to_explore,'\n')



chosen_word=input("What's the word chosen: ").strip().lower()
response=input("What's the wordle response: ").strip()
unused_letters=[char for char in unused_letters if char not in chosen_word]
while(response!="!" and len(possible_words)>1):
    if not (chosen_word.isalpha() and len(chosen_word) == 5):
        print("Error: The chosen word must be exactly 5 letters (a-z). Try again or type ! to exit.")
    elif not (response.isdigit() and len(response) == 5 and all(char in '012' for char in response)):
        print("Error: The response must be a 5 character string containing only 0s, 1s, and 2s. Try again or type ! to exit.")
    else:
        chosen_word = chosen_word.lower()
        possible_words,count_list=update_word_list(possible_words,chosen_word,response,present_letters)
        top_words_to_exploit=spit_top_words_to_exploit(possible_words,count_list)
        top_words_to_explore=spit_top_words_to_explore(guess_words_list,count_list,unused_letters)
        print("No of possible words left: ",len(possible_words),'\n')
        print("Top words to exploit:",top_words_to_exploit,'\n')
        print("Top words to explore:",top_words_to_explore,'\n')
    if(len(possible_words)>1):
        chosen_word=input("What's the word chosen: ").strip()
        response=input("What's the wordle response: ").strip()
        unused_letters=[char for char in unused_letters if char not in chosen_word]

if(len(possible_words)<=1):
    print("I bet you got the word right.")