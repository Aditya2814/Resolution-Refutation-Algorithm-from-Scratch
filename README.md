# Resolution-Refutation-Algorithm-from-Scratch

## Overview

Python scripts implement an automated theorem proving algorithm based on resolution in propositional logic. It utilizes the SymPy library for symbolic mathematics to handle logical expressions, CNF conversion, and simplification.

## Algorithm Description

The algorithm employs resolution to determine whether a given query is entailed by a knowledge base (KB) of logical formulas. Key components include:

- Heuristic Functions: Evaluates the priority of clauses based on the total number of negations of literals in the KB.

- Resolution Functions:
  - Checks if two clauses can be resolved.
  - Performs the resolution operation between two clauses.
  - Iteratively resolves clauses in the KB until a conclusion is reached or no further resolution is possible.

## Usage

1. **Install Dependencies:**
    ```pip install sympy```

2. **Run the Script in a Terminal:**
    ```python uninformed.py```
    This will run the uninformed search algorithm.

    ```python greedy.py```
    This will run the greedy search algorithm.

3. **Input Format:**
    - Enter the number of formulas in the KB (n) and choose whether to display detailed steps (m).
    - For the next n lines, formulas should be entered in a certain format as given below
	The following characters are used to denote different operators: <br />
	OR: | <br />
	AND: & <br />
	NOT: ! <br />
	IMPLICATION: > <br />
	IFF (bidirectional): = <br />
	OPENING BRACKET: ( <br />
	CLOSING BRACKET: ) <br />
	For boolean literals, upper case letters of the alphabet are used (A, B, C …… Z). <br />

    - Input the query in the same format.

    (Note: There is no space between two consecutive operators/variables)

## Output

- The script outputs whether the query is entailed by the KB.
- If detailed steps are requested (m=1), the resolution steps are printed.

## Example

(Open a terminal in the same folder)

python greedy.py <br />
4 0 <br />
P|(Q&(R>T)) <br />
P>R <br />
Q>T <br />
Q>(R=T) <br />
R <br />
(click enter to run) <br />
0 <br />
(0 is the output which indicates the query R is not entailed by KB) <br />
