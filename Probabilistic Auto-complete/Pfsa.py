import argparse
import pytest
import json
import nltk  
import re 

def construct(file_str: str) -> dict[str, dict[str, float]]:
    """Takes in the string representing the file and returns pfsa
    The given example is for the statement "A cat"
    """

    # TODO: FILE IN THIS FUNCTION
    tokens = nltk.word_tokenize(file_str)
    lenght = len(tokens)
    for i in range(lenght):
        tokens[i] = re.sub(r"[^\w\s]", "", tokens[i])
        tokens[i] = tokens[i].lower()
    pfsa = {}
    given = {}
    holding = []
    given["*"] = tokens
    # holding.append(given)
    holding = holding + [given]
    i = 1
    while holding:
        dict = holding.pop(0)
        strNewDict = {}
        for j in dict:
            strlist = dict[j]
            length = len(strlist)
            newDict = {}
            for c in strlist:
                string = c[:i]
                strNewDict[string] = []
                if string in newDict:
                    newDict[string] += 1
                else:
                    newDict[string] = 1
            for c in strlist:
                string = c[:i]
                if c == string and c[-1] != "*":
                    c = c + "*"
                    strNewDict[string] = strNewDict[string] + [c]
                elif c[-1] == "*":
                    if string in strNewDict:
                        del strNewDict[string]
                else:
                    strNewDict[string] = strNewDict[string] + [c]

            holdingDict = {}
            for c in newDict:
                holdingDict[c] = newDict[c] / length

            pfsa[j] = holdingDict
        if strNewDict:
            holding = holding + [strNewDict]
        i = i + 1

    return pfsa


def main():
    """
    The command for running is `python pfsa.py text.txt`. This will generate
    a file `text.json` which you will be using for generation.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("file", type=str, help="Name of the text file")
    args = parser.parse_args()

    with open(args.file, "r") as file:
        contents = file.read()
        # print(contents)
        output = construct(contents)

    name = args.file.split(".")[0]

    with open(f"{name}.json", "w") as file:
        json.dump(output, file)


if __name__ == "__main__":
    main()


STRINGS = ["A cat", "A CAT", "", "A", "A A A A"]
DICTIONARIES = [
    {
        "*": {"a": 0.5, "c": 0.5},
        "a": {"a*": 1.0},
        "c": {"ca": 1.0},
        "ca": {"cat": 1.0},
        "cat": {"cat*": 1.0},
    },
    {
        "*": {"a": 0.5, "c": 0.5},
        "a": {"a*": 1.0},
        "c": {"ca": 1.0},
        "ca": {"cat": 1.0},
        "cat": {"cat*": 1.0},
    },
    {
        "*": {},
    },
    {
        "*": {"a": 1.0},
        "a": {"a*": 1.0},
    },
    {
        "*": {"a": 1.0},
        "a": {"a*": 1.0},
    },
]


@pytest.mark.parametrize("string, pfsa", list(zip(STRINGS, DICTIONARIES)))
def test_output_match(string, pfsa):
    """
    To test, install `pytest` beforehand in your Python environment.
    Run `pytest pfsa.py` Your code must pass all tests. There are additional
    hidden tests that your code will be tested on during VIVA.
    """
    result = construct(string)
    assert result == pfsa

    # def create
