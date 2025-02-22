# Flashy - French Learning Flashcards

## Description

Flashy is a simple flashcard application built using Python and Tkinter to help users learn French vocabulary. It displays French words along with their English translations and allows users to mark words they already know, saving their progress.

## Features

- Displays a random French word from the dataset.
- After 3 seconds, the flashcard flips to reveal the English translation.
- Users can mark words they already know, removing them from future practice sessions.
- Progress is saved in `words_to_learn.csv`, ensuring users only review unknown words.

## Requirements

Ensure you have the following installed:

- Python 3
- Pandas
- Tkinter (usually included with Python)

## Installation

1. Clone this repository or download the files.
2. Ensure you have the required dependencies installed:
   ```bash
   pip install pandas
   ```
3. Place the following required files in the correct directories:
   - `french_words.csv` inside the `data` folder.
   - `words_to_learn.csv` (auto-generated, stores progress).
   - Image assets (`card_front.png`, `card_back.png`, `wrong.png`, `right.png`) inside the `images` folder.

## Usage

1. Run the script:
   ```bash
   python main.py
   ```
2. A flashcard will display a French word.
3. Wait 3 seconds for the English translation to appear.
4. Click the **✓ (Right)** button if you know the word, removing it from future sessions.
5. Click the **✗ (Wrong)** button to see another word.

## File Structure

```
📂 Project Folder
 ┣ 📂 data
 ┃ ┣ french_words.csv
 ┃ ┗ words_to_learn.csv
 ┣ 📂 images
 ┃ ┣ card_front.png
 ┃ ┣ card_back.png
 ┃ ┣ wrong.png
 ┃ ┗ right.png
 ┣ main.py
 ┗ README.md
```

## Author

Developed by Guranda Jikia.
