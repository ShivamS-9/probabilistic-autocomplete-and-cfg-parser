# Programming Assignments for Automata Theory (Monsoon 2023)

## Overview

This repository contains implementations for the two programming assignments as part of the Automata Theory course at IIIT Hyderabad. The assignments are:

1. **Probabilistic Auto-complete**: Implementation of a Probabilistic Finite State Automaton (PFSA) to generate a letter-level auto-complete system.
2. **Compiler with Tokenization and CFG Parsing**: Implementation of a compiler that performs lexical and syntactical analysis based on a given context-free grammar.

---

## Probabilistic Auto-complete

### Description
This program constructs a PFSA from a given text corpus and allows sampling of random words based on the PFSA's probabilities. It includes two parts:
1. `pfsa.py`: Builds the PFSA and stores it in a JSON file.
2. `generator.py`: Reads the PFSA JSON file and generates random words.

### Input and Output
1. **Input**: A text corpus file containing valid English words.
2. **Output**: A JSON representation of the PFSA and a text file with sampled words.

### Assumptions
- Each state in the PFSA represents a prefix of an English word.
- Transition probabilities are based on the text corpus and follow the axioms of probability.
- Valid words in the corpus are marked with a `*`.

### Usage
1. Run `pfsa.py` with the text corpus to generate the PFSA.
2. Use `generator.py` to sample words based on the generated PFSA.

---

## Compiler with Tokenization and CFG Parsing

### Description
This program implements a compiler for a simple programming language. It performs:
1. **Lexical Analysis**: Tokenizes the source code into identifiers, keywords, integers, floating-point numbers, and symbols.
2. **Syntactical Analysis**: Validates the structure of the source code against a given CFG.

### Input and Output
1. **Input**: A single line of source code.
2. **Output**:
   - On successful parsing: Prints the token types and values.
   - On error: Prints a description of the lexical or syntactic error.

### Assumptions
- The source code follows the CFG rules mentioned in the assignment.
- Keywords have higher precedence than identifiers.
- Errors are clearly reported with appropriate descriptions.

### Usage
1. Run the program and provide a line of source code as input.
2. Review the tokens or errors displayed.

---

## Requirements
- Python 3.x
- Standard Python libraries (No external dependencies unless approved)
