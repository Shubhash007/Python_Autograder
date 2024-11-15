# Add question here
new_question = {
    "title": "NRIC check sum", 
    "description": """
    Write a Python program that takes the first 7 characters of a Singapore NRIC/FIN (excluding the last letter) as input from the user. 
    The program should then calculate the checksum and output the corresponding last alphabet of the NRIC/FIN.

    Prompt the user to enter the first 7 characters of their NRIC/FIN number (e.g., S1234567).
    Using the Singapore NRIC/FIN checksum formula, calculate the corresponding alphabet for the last character.
    The formula uses weights [2, 7, 6, 5, 4, 3, 2] for each digit, starting from the second character.
    Multiply each digit by the corresponding weight and sum the results.
    
    The checksum depends on the first character (e.g., 'S', 'T', 'F', 'G').
    For 'S' and 'F', use this list of letters for modulo results: ['J','Z','I','H','G','F','E','D','C','B','A']
    For 'T' and 'G', use this list of letters: ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'J', 'Z', 'I', 'H']

    if First Character 'S' or 'F':
        Add 0 to the sum.
    if First Character 'T' or 'G':
        Add 4 to the sum.

    The result from the calculation should be taken modulo 11 to find the index of the checksum alphabet.

    Print the complete NRIC/FIN number with the calculated last alphabet.


""", 

    "sample_output_description": """
    If the user enters S1234567, your program should output S1234567D.

     
 """
}