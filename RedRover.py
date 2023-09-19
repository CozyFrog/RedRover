"""
Garrett Sward
09/17/2023
For Mike Sheldon of Red Rover. Thank you for your consideration!

This is a program built to convert the input string to two outputs.

input string: (id, name, email, type(id, name, customFields(c1, c2, c3)), externalId)

output one:
- id
- name
- email
- type
  - id
  - name
  - customFields
    - c1
    - c2
    - c3
- externalId

output two:
- email
- externalId
- id
- name
- type
  - customFields
    - c1
    - c2
    - c3
  - id
  - name


parseOne and parseTwo are the functions that will convert the input string to each  desired output.
 """


def printAttrOne(s, indent):
    """Print s, an attribute, with its corresponding level of indentation."""
    print(indent * "  " + "- " + s)
    return

def printAttrTwo(d, indent):
    """Iterate through dict of attributes, print them in alphanumeric order."""
    sD = sorted(d)
    for i in range(len(sD)):
        s = sD[i]
        printAttrOne(s, indent)
        if type(d[s]) is dict:
            newInd = indent + 1
            printAttrTwo(d[s], newInd)
    return

def parseOne(strInput):
    """Parse input string and output in first format."""
    s = ""
    indent = 0
    for i in range(1, len(strInput)):
        if strInput[i] == ",":
            if s != "":
                printAttrOne(s, indent)
                s = ""
        elif strInput[i] == " ":
            continue
        elif strInput[i] == "(":
            printAttrOne(s, indent)
            s = ""
            indent += 1
        elif strInput[i] == ")":
            if s != "":
                printAttrOne(s, indent)
                s = ""
            indent -= 1
        else:
            s = s + strInput[i]

    return strInput


def parseTwoHelper(strInput, i, d):
    """Recursively work through input string, add attributes to nested dict."""
    s = ""
    while i < len(strInput):
        i += 1
        if strInput[i] == ")":
            if s != "":
                d[s] = s
                s = ""
            return d, i
        elif strInput[i] == ",":
            if s != "":
                d[s] = s
                s = ""
        elif strInput[i] == " ": pass
        elif strInput[i] == "(":
            d[s], i = parseTwoHelper(strInput, i, {})
            s = ""
        else:
            s = s + strInput[i]
    return d, i


def parseTwo(strInput):
    """Parse input string and outputs in second format; call recursive helper function."""
    d, i = parseTwoHelper(strInput, 0, {})
    printAttrTwo(d, 0)
    return


parseOne("(id, name, email, type(id, name, customFields(c1, c2, c3)), externalId)")
print()
parseTwo("(id, name, email, type(id, name, customFields(c1, c2, c3)), externalId)")
