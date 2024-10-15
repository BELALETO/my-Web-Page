import subprocess

class compiler:
    cpp_file = ""
    cpp_out = ""
    input_file = "" 
    
    def __init__(self, cpp_file, cpp_out, input_file = ""):
        self.cpp_file = cpp_file
        self.cpp_out = cpp_out
        self.input_file = input_file
        
    def build_Run(self):
        command = ["g++", self.cpp_file, "-o", self.cpp_out]
        try:
            subprocess.run(command, check=True)
            if self.input_file:
                # print(self.input_file)
                with open(self.input_file, "r") as input:
                    result = subprocess.run(["./" + self.cpp_out], stdin = input) #passing the input file to stdin buffer.
            else:        
                result = subprocess.run(["./"+ self.cpp_out], check=True, text=True, capture_output=True)
                
            output = result.stdout
            error = result.stderr

            if error:
                return error
            else:
                return output
    
        except subprocess.SubprocessError as e:
           return f"Error: {e}"