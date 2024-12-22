##################### BOILERPLATE BEGINS ############################

# Token types enumeration
##################### YOU CAN CHANGE THE ENUMERATION IF YOU WANT #######################
class TokenType:
    IDENTIFIER = "IDENTIFIER"
    KEYWORD = "KEYWORD"
    INTEGER = "INTEGER"
    FLOAT = "FLOAT"
    SYMBOL = "SYMBOL"

# Token hierarchy dictionary
token_hierarchy = {
    "if": TokenType.KEYWORD,
    "else": TokenType.KEYWORD,
    "print": TokenType.KEYWORD
}


# helper function to check if it is a valid identifier
def is_valid_identifier(lexeme):
    if not lexeme:
        return False

    # Check if the first character is an underscore or a letter
    if not (lexeme[0].isalpha() or lexeme[0] == '_'):
        return False

    # Check the rest of the characters (can be letters, digits, or underscores)
    for char in lexeme[1:]:
        if not (char.isalnum() or char == '_'):
            return False

    return True


keywords = ["if", "else", "print"]

# Tokenizer function
def tokenize(source_code):
    tokens = []
    position = 0

    while position < len(source_code):
        # Helper function to check if a character is alphanumeric
        def is_alphanumeric(char):
            return char.isalpha() or char.isdigit() or (char=='_')

        char = source_code[position]

        # Check for whitespace and skip it
        if char.isspace():
            position += 1
            continue

        # Identifier recognition
        if char.isalpha():
            lexeme = char
            position += 1
            while position < len(source_code) and is_alphanumeric(source_code[position]):
                lexeme += source_code[position]
                position += 1

            if lexeme in token_hierarchy:
                token_type = token_hierarchy[lexeme]
            else:
                # check if it is a valid identifier
                if is_valid_identifier(lexeme):
                    token_type = TokenType.IDENTIFIER
                else:
                    raise ValueError(f"Invalid identifier: {lexeme}")

        # Integer or Float recognition
        elif char.isdigit():
            lexeme = char
            position += 1

            is_float = False
            while position < len(source_code):
                next_char = source_code[position]
                # checking if it is a float, or a full-stop
                if next_char == '.':
                    if (position + 1 < len(source_code)):
                        next_next_char = source_code[position+1]
                        if next_next_char.isdigit():
                            is_float = True

                # checking for illegal identifier
                elif is_alphanumeric(next_char) and not next_char.isdigit():
                    while position < len(source_code) and is_alphanumeric(source_code[position]):
                        lexeme += source_code[position]
                        position += 1
                    if not is_valid_identifier(lexeme):
                        raise ValueError(f"Invalid identifier: {str(lexeme)}\nIdentifier can't start with digits")

                elif not next_char.isdigit():
                    break

                lexeme += next_char
                position += 1

            token_type = TokenType.FLOAT if is_float else TokenType.INTEGER

        # Symbol recognition
        else:
            lexeme = char
            position += 1
            token_type = TokenType.SYMBOL

        tokens.append((token_type, lexeme))

    return tokens

########################## BOILERPLATE ENDS ###########################







grammar = {
        'S': {'FA', 'KK', 'sig'},
        'K': {'FA', 'KK', 'sig'},
        'A': {'CK', 'CV'},
        'C': {'XW', 'R_'},
        'O': {'+', '-', '^', '/', '*', '<', '>', '='},
        'X': {'R_', 'XW'},
        'F': {'if'},
        'V': {'KN'},
        'N': {'EK'},
        'E': {'else'},
        'W': {'OX'},
    }

def cykCheck(grammar, tokens):
    n = len(tokens)
    dp = [[set() for _ in range(n + 1)] for _ in range(n + 1)]

# using dp matrix

    for i in range(1, n + 1):
        for keys in grammar:
            for j in range(n):
                if tokens[j] in grammar[keys]:
                    dp[j + 1][j + 1].add(keys)
                if tokens[j] not in ('if', 'else'):
                    dp[j + 1][j + 1].add('K')

    for l in range(2, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            for k in range(i, j):
                for keys in grammar:
                    for value in grammar[keys]:
                        if value not in tokens and len(value) == 2:
                            if all(v in dp[i][k] for v in value[:1]) and all(v in dp[k + 1][j] for v in value[1:]):
                                dp[i][j].add(keys)

    return 'S' in dp[1][n]
 

def checkGrammar(tokens):
    new_tokens = []
    for token in tokens:
        if token[0] != 'INTEGER' and token[0] != 'FLOAT':
            if token[1] == 'if' or token[1] == 'else':
                new_tokens.append(token[1])
            else:
                new_tokens.append('sig')
        else:
            new_tokens.append('R_')

    is_accepted = cykCheck(grammar, new_tokens)

    if not is_accepted:
        print('Syntax Error: Invalid statement')

if __name__ == "__main__":
    source_code = input()

    if not source_code:
        print("False")
    else:
        tokens = tokenize(source_code)

        new_tokens = []
        for token in tokens:
            if token[0] != 'INTEGER' and token[0] != 'FLOAT':
                if token[1] == 'if' or token[1] == 'else':
                    new_tokens.append(token[1])
                else:
                    new_tokens.append('sig')
            else:
                new_tokens.append('R_')

        is_accepted = cykCheck(grammar, new_tokens)
        # print(is_accepted)
        if(is_accepted):
            for token in tokens:
                print(f"Token Type: {token[0]}, Token Value: {token[1]}")

        checkGrammar(tokens)

