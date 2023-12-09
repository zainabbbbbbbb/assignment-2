from preprocessor import Preprocessor
from processor import Processor
from lexical_analyzer import LexicalAnalyzer

if __name__ == "__main__":
    
    preprocessor = Preprocessor('input_file.py', 'out1.py')
    preprocessor.preprocess()

   
    with open(preprocessor.output_file, 'r') as result_file:
        print("Task 1 Output:")
        print(result_file.read())

    
    processor = Processor('out1.py', 'out2.py')
    processor.process_file()

    
    with open('out2.py', 'r') as result_file:
        print("\nTask 2 Output:")
        print(result_file.read())

    
    lexical_analyzer = LexicalAnalyzer('out2.py')
    print("\nTask 3 Output:")
    lexical_analyzer.analyze_lexemes()

