# Quiplash AI
# *THIS DOES NOT PLAY THE GAME FOR YOU, YOU NEED TO HAVE THE GAME OPEN*

This project contains Python scripts that simulate AI players for the game **Quiplash** Using github models. The AI can either generate witty responses to prompts or vote for the funniest quips provided by other players.

## Files

- **`quiplashAnyW1.py`**: AI script for generating witty responses in any round of Quiplash. The AI provides a single quip or a "safety quip" if no witty response is available.
- **`quiplashAnyV1.py`**: AI script for voting on quips in any round of Quiplash. The AI analyzes two quips and selects the funniest one.

### These are for quiplash three (1+XL+2 are coming soon™️)
- **`quiplashThreeW3.py`**: AI script for generating three witty responses in the third round of Quiplash (Thriplash).
- **`quiplashThreeV3.py`**: AI script for voting on quips in the third round of Quiplash (Thriplash). The AI evaluates two sets of three quips and selects the funniest set. (takes a while, YOU MAY NEED TO PAUSE GAME)



## How to Use

1. **Install Dependencies**:
   - Ensure you have Python installed.
   - Install the `openai` library:
     ```sh
     pip install openai
     ```

2. **Set Up API Key**:
   - Replace `YOUR_TOKEN_HERE` in each script with your github token.

3. **Run a Script**:
   - Open a terminal and navigate to the project directory.
   - Run the desired script

4. **Interact with the AI**:
   - Follow the prompts in the terminal to ask questions or provide inputs.

## Game Modes

### Voting Scripts
- **`quiplashAnyV1.py`**: The AI votes between two quips.
- **`quiplashThreeV3.py`**: The AI votes between two sets of three quips.

### Writing Scripts
- **`quiplashAnyW1.py`**: The AI generates a single witty response or a "safety quip."
- **`quiplashThreeW3.py`**: The AI generates three witty responses for Thriplash.

## Notes

- Ensure your API key has sufficient permissions to access the Github Models API.
- The AI's responses are influenced by the system prompt in each script, which defines its role and behavior.
- Use the family-filter, otherwise it won't respond to all