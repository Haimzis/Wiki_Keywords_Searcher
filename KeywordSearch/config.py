KEYWORDS_DELIMITERS_REG_EXPRESSION = '\\s|\\W'
INPUT_DELIMITERS_REG_EXPRESSION = '[\\s\\W]?'
KEYWORDS_FILE_PATH = 'keywords.txt'

TEST_EXAMPLES = [{'input': 'Welcome to >>GENERAL-motors! We love programming!',
                          'result': {'General Motors', 'Programming'}
                  },
                 {'input': 'Beside being a team focused on cyber-security, we also do software engineering. '
                                   'With good communication we might figure out some unsolved problems in '
                                   'computer-science!',
                          'result': {'Communication', 'Cyber Security', 'Computer science', 'Software engineering',
                                     'Unsolved problems in computer science'}
                          }
                 ]
