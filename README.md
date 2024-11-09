The FLAMES Game is a fun, interactive childhood game that predicts the relationship between two people based on their names. This project is implemented in Python and uses the tkinter library to create a simple and user-friendly graphical user interface (GUI). The game analyzes the input names to determine a relationship status from the possible outcomes: Friends, Love, Affection, Marriage, Enemy, or Siblings.

## features
Simple GUI: Uses tkinter to create an intuitive interface for users to input names and see the results.
Easy Interaction: The "Submit" button computes the relationship, and the "Clear" button resets the inputs for a new session.
Fun Logic: Implements the traditional FLAMES logic, where matching characters in the names are removed, and the total remaining characters determine the relationship status.
How the Game Works
The user enters their name and their crush’s name in the input fields.
The program removes matching characters from both names.
The combined number of remaining characters is used to cycle through the outcomes (Friends, Love, Affection, Marriage, Enemy, Siblings).
The program displays the final relationship result in the output field.
## Prerequisites
Python 3.x installed on your system.
tkinter is included by default with Python.
## How to Run the Project
Clone or download the project to your local system.
Run the Python script using:
bash
python flames_game.py
A GUI window will open with fields to input names and buttons for "Submit" and "Clear".
Enter the names and click "Submit" to see the relationship result. Use "Clear" to reset the fields.
# Code Explanation
## Key Functions
remove_match_char(list1, list2): Takes two lists of characters and removes matching characters from both lists. Returns the updated lists and a flag indicating if a match was found.
tell_status(): Main function that processes the user input, calls remove_match_char() to remove matches, counts the remaining characters, and determines the relationship status by cycling through the result list.
clear_all(): Clears all input and output fields to allow for a new session.
## GUI Components
Labels: Guide the user to input their name and their crush’s name and display the relationship status.
Entry Fields: Collect user inputs and display results.
Buttons: Execute the main logic with "Submit" and reset the fields with "Clear".
Example Flow
Input: User enters "Alice" and "Bob".
Process: The program removes matching characters and counts the remaining characters.
Output: Displays the result based on the total count (e.g., "Love").

# Screenshots


<img width="374" alt="flames1" src="https://github.com/user-attachments/assets/8eab3aa8-49ba-48e3-9a66-60d2572534f2">
<img width="371" alt="flames2" src="https://github.com/user-attachments/assets/834ef4bb-6d56-4416-9557-c88a2cbc4ca6">

## Future Enhancements
Adding more relationship status outcomes for fun.
Improving the GUI with better styling and graphics.
Allowing users to save results or share them directly.
## Contributing
Feel free to fork this project and submit pull requests for improvements. Any contributions that enhance the functionality or user experience are welcome!

## License
This project is licensed under the MIT License. You are free to use, modify, and distribute this project as per the terms of the license.



