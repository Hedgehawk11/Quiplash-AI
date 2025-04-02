# Quiplash AI
# *THIS DOES NOT PLAY THE GAME FOR YOU, YOU NEED TO HAVE THE GAME OPEN*

This project contains Python scripts that simulate AI players for the game **Quiplash** using OpenAI models. The AI can either generate witty responses to prompts or vote for the funniest quips provided by other players.

## Files

### General Scripts
- **`quiplashAnyW1.py`**: AI script for generating witty responses in any round of Quiplash. The AI provides a single quip or a "safety quip" if no witty response is available.
- **`quiplashAnyV1.py`**: AI script for voting on quips in any round of Quiplash. The AI analyzes two quips and selects the funniest one.

### Quiplash XL Scripts
- **`quiplashXLW3.py`**: AI script for generating witty responses in the third round of Quiplash XL (The Last Lash). The AI provides a single witty response to the prompt.
- **`quiplashXLV3.py`**: AI script for voting on quips in the third round of Quiplash XL (The Last Lash). The AI evaluates multiple quips and selects the funniest one.

### Quiplash 2 Scripts
- **`quiplashTwoW3ACL.py`**: AI script for generating witty acronyms in the third round of Quiplash 2 (Acro Lash). The AI creates a funny acronym based on three provided letters.
- **`quiplashTwoW3WL.py`**: AI script for generating witty responses in the third round of Quiplash 2 (Word Lash). The AI provides a humorous response based on a word and instructions.
- **`quiplashTwoV3.py`**: AI script for voting on quips in the third round of Quiplash 2. The AI evaluates multiple quips and selects the funniest one.

### Quiplash 3 Scripts
- **`quiplashThreeW3.py`**: AI script for generating three witty responses in the third round of Quiplash 3 (Thriplash). The AI provides three quips separated by the `|` character.
- **`quiplashThreeV3.py`**: AI script for voting on quips in the third round of Quiplash 3 (Thriplash). The AI evaluates two sets of three quips and selects the funniest set.

## How to Use

1. **Install Dependencies**:
   - Ensure you have Python installed.
   - Install the `openai` library:
     ```sh
     pip install openai
     ```

2. **Set Up API Key**:
   - Replace `YOUR_TOKEN_HERE` in each script with your OpenAI API key.

3. **Run the Main Script**:
   - Open a terminal and navigate to the project directory.
   - Run the `main.py` script:
     ```sh
     python main.py
     ```

4. **Interact with the AI**:
   - Follow the prompts in the terminal to ask questions or provide inputs.

## Game Modes

### Voting Scripts
- **`quiplashAnyV1.py`**: The AI votes between two quips.
- **`quiplashTwoV3.py`**: The AI votes between multiple quips in Quiplash 2.
- **`quiplashThreeV3.py`**: The AI votes between two sets of three quips in Quiplash 3.
- **`quiplashXLV3.py`**: The AI votes between multiple quips in Quiplash XL.

### Writing Scripts
- **`quiplashAnyW1.py`**: The AI generates a single witty response or a "safety quip."
- **`quiplashTwoW3ACL.py`**: The AI generates a witty acronym for Acro Lash in Quiplash 2.
- **`quiplashTwoW3WL.py`**: The AI generates a witty response for Word Lash in Quiplash 2.
- **`quiplashThreeW3.py`**: The AI generates three witty responses for Thriplash in Quiplash 3.
- **`quiplashXLW3.py`**: The AI generates a witty response for The Last Lash in Quiplash XL.

## Notes

- Ensure your API key has sufficient permissions to access the OpenAI API.
- The AI's responses are influenced by the system prompt in each script, which defines its role and behavior.
- Use the family-filter, otherwise it won't respond to all prompts.