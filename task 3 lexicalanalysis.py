class LexicalAnalyzer:
    def __init__(self, input_file):
        self.input_file = input_file

    def analyze_lexemes(self):
        with open(self.input_file, 'r') as file:
            content = file.read()

       
        tokenss = content.split()

        
        keyword_lexemes = set(["and", "as", "assert", "break", "class", "continue", "def", "del", "elif", "else", "except", "False", "finally", "for", "from", "global", "if", "import", "in", "is", "lambda", "None", "nonlocal", "not", "or", "pass", "raise", "return", "True", "try", "while", "with", "yield"])
        identifier_lexemes = set(["x", "y", "z", "sum", "count", "temp", "my_var", "my_function"])  
        operator_lexemes = set(["+", "-", "*", "/", "%", "=", "+=", "-=", "*=", "/=", "==", "!=", "<", ">", "<=", ">=", "and", "or", "not", "in", "is"])
        punctuator_lexemes = set(["{", "}", "[", "]", "(", ")", ",", ";", ":", "."])
        literal_lexemes = set(["42", "3.14", '"Hello, world!"', "'A'", "'9'", "True", "False", "None"])
        comment_lexemes = set(["#"])
        annotation_lexemes = set(["@"])
        import_lexemes = set(["import", "from"])

        
        for token in tokenss:
            lexeme_category = None

            if token in keyword_lexemes:
                lexeme_category = "Keyword"
            elif token in identifier_lexemes:
                lexeme_category = "Identifier"
            elif token in operator_lexemes:
                lexeme_category = "Operator"
            elif token in punctuator_lexemes:
                lexeme_category = "Punctuator"
            elif token in literal_lexemes:
                lexeme_category = "Literal"
            elif token in comment_lexemes:
                lexeme_category = "Comment"
            elif token in annotation_lexemes:
                lexeme_category = "Annotation"
            elif token in import_lexemes:
                lexeme_category = "Import"
            else:
               
                if token.isdigit():
                    lexeme_category = "Literal (Number)"
                elif token[0] == "'" and token[-1] == "'":
                    lexeme_category = "Literal (Character)"
                elif token[0] == '"' and token[-1] == '"':
                    lexeme_category = "Literal (String)"
                else:
                    
                    lexeme_category = "Unknown"

            print(f"Lexeme: {token} \t Category: {lexeme_category}")

