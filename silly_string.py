import random

def silly_string(nouns, verbs, templates):
    # Choose a random template.
    template = random.choice(templates)
    # We'll append strings into this list for output.
    output = []
    # Keep track of where in the template string we are.
    index = 0

    while index < len(template):
        if template[index:index+8] == '{{noun}}':
            # Add a random noun to the output.
            output.append(random.choice(nouns))
            index += 8
        elif template[index:index+8] == '{{verb}}':
            # Add a random verb to the output.
            output.append(random.choice(verbs))
            index += 8
        else:
            # Copy a character to the output.
            output.append(template[index])
            index += 1
    # Join the output into a single string.
    return ''.join(output)
nouns = ['apple', 'ball', 'cat', 'dog', 'elephant',
         'fish', 'goat', 'house', 'iceberg', 'jackal',
         'king', 'llama', 'monkey', 'nurse', 'octopus',
         'pie', 'queen', 'robot', 'snake', 'tofu',
         'unicorn', 'vampire', 'wumpus', 'x-ray', 'yak',
         'zebra']

verbs = ['ate', 'bit', 'caught', 'dropped', 'explained',
         'fed', 'grabbed', 'hacked', 'inked', 'jumped',
         'knitted', 'loved', 'made', 'nosed', 'oiled',
         'puffed', 'quit', 'rushed', 'stung', 'trapped',
         'uplifted', 'valued', 'wanted']

templates = ['Waiter! I found a {{noun}} in my {{noun}}!',
        'The {{noun}} {{verb}} the {{noun}}.',
        'If you {{verb}} the {{noun}}, '
        'the {{noun}} will get you.',
        "Let's go: the {{noun}} is {{verb}}.",
        'Colorless green {{noun}}s {{verb}} furiously.']        

if __name__ == '__main__':
    print(silly_string(nouns, verbs, templates))

