import subprocess


class compiler:
    cpp_file = ""
    cpp_out = ""

    def __init__(self, cpp_file, cpp_out):
        self.cpp_file = cpp_file
        self.cpp_out = cpp_out
    
    def build_Run(self):
        command = ["g++", self.cpp_file, "-o", self.cpp_out]
        try:
            subprocess.run(command, check=True)
            result = subprocess.run(["./"+ self.cpp_out], check=True, text=True, capture_output=True)
            output = result.stdout
            error = result.stderr

            if error:
                return error
            else:
                return output
    
        except subprocess.SubprocessError as e:
           return f"Error: {e}"