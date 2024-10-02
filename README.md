# Wordle Solver Bot
# Wordle Solver Bot

This bot helps you find the best words to solve the Wordle puzzle, though it may not be the most efficient one.

## Usage

Run the following command to use the bot:

```bash
python3 wordle-bot.py
```

The bot will suggest a few good starting words. You can choose between two strategies: **Explore** and **Exploit**.

- **Explore**: Gather maximum information from each guess.
- **Exploit**: Make the most likely guess based on the current information.

It's recommended to use the Explore strategy initially and switch to the Exploit strategy when fewer words remain.

## Response Format

After each guess, the bot will ask for feedback in the form of a string of 0s, 1s, and 2s:

- `0`: The letter is not in the word (Wordle shows the letter's background in black).
- `1`: The letter is in the word but in the wrong position (Wordle shows the letter's background in yellow).
- `2`: The letter is in the correct position (Wordle shows the letter's background in green).

### Example

If the Wordle word is **CHOIR** and your guess is **SHARE**, the response should be `02010`.

Continue this process until you guess the correct word.
