# wordle-solver-bot
This is a wordle-solver-bot which is not perfect, but to use this run "python3 wordle-bot.py"\n
And you get a few really good words to attack the wordle puzzle, then the bot asks for a response\n
The response is a string of 0s,1s and 2s\n
For each letter of the five-lettered word,\n
if the letter is not in the word(wordle represents the letter's background in black), add '0' to your string\n
If the letter is in the word, but it is in incorrect position(wordle represents the letter's background in yellow), add '1' to the string\n
If the letter is in it's correct position(wordle represents the letter's background in green), add '2' to the string\n
For example,\n
If the wordle's word was CHOIR, and your word was SHARE, then the response should be 02010\n
Do this until you get your word right\n

# There is a mistake I need to fix if there is multiple of the same letters in the word

