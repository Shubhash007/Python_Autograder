# upload specific rubrics for question
new_rubrics = {
    "Criteria": [                
        "Input Handling",
        "Use of strip function",
        "Use of upper function",
        
        "Convert digit to integer - for loop and int()", 
        "Convert digit to integer - list comprehension with int()",
        
        "Applies correct weights - list for weights",
        "Calculates weighted sum - for loop",
        "Calculates weighted sum - list comprehension with *",

        "Compute modulo 11",
        "Select right checksum letter - if-else",
        "Correct checksum letter - list for S and F",
        "Correct checksum letter - list for T and G"
    ],

    "Marks": [2,1,1,1,1,1,1,1,2,0.5,0.5,0.5],

    "Description": [
        # Input Handling
        """ As long as input() exists anywhere in the program, return 2 mark.
        """,

        # Use of strip function
        """ As long as strip() exists anywhere in the program, return 1 mark.
        """,

        # Use of upper function
        """ As long as upper() exists anywhere in the program, return 1 mark
          """,

        # Convert digit to integer - for loop and int()
        """Check for a for-loop exists in the program, and check that int() function exists within the for loop, return 1 mark.""",
        # Convert digit to integer - list comprehension with int()
        """Check if a list comprehension exists in the program and if the int() function is used within that list comprehension. If both are present, return 1 mark.""",



        # Applies correct weights - list for weights
        """Check that exact list [2, 7, 6, 5, 4, 3, 2] exists anywhere in the program, return 1 mark.""",

        # Calculates weighted sum - for loop
        """Check for a for-loop that exists in the program, and check that operator * is used within the for loop, return 1 mark.""",
        # Calculates weighted sum - list comprehension with *
        """Check if a list comprehension exists in the program and if operator * is used within that list comprehension, return 1 mark.""",

        
        # Compute modulo 11
        """If modulo '%' and 11 exists anywhere in the program, return 2 mark.""",

        # Select right checksum letter - if-else
        """ Check for if-else statement exists anywhere in program, return 0.5 mark.
        """,
        
        # Correct checksum letter - list for S and F
        """Check that exact list ['J','Z','I','H','G','F','E','D','C','B','A'] exists anywhere in the program, return 0.5 mark.""",

        # Correct checksum letter - list for T and G
        """Check that exact list ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'J', 'Z', 'I', 'H'] exists anywhere in the program, return 0.5 mark.""",


    ],
    "Total": 10.5
}
output_rubrics = {
   
}