class Processor():
    def __init__(self,input_file,output_file):
        self.input_file=input_file
        self.output_file=output_file

    def processing_file(self):
        with open(self.input_file,'r') as file:
            content4=file.read()

            content4=content4.replace('\n',' ')
            content4=content4+'$'

        with open(self.output_file,'w') as out_file:
            out_file.write(content4)



