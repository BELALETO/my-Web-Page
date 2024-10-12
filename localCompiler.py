import subprocess

class compiler:
    cpp_file = ""
    cpp_out = ""
    
    def __init__(self, cpp_file, cpp_out):
        self.cpp_file = cpp_file
        self.cpp_out = cpp_out
        
    def build(self, cpp_file, cpp_out):
        command = ["g++", cpp_file, "-o", cpp_out]
        try:
            subprocess.run(command, check=True)
            return f"code compiled successfully"
        
        except subprocess.SubprocessError as e:
            return f"compiler error: {e}"
    
    def run_exe(self, cpp_out):
        command = ["./", cpp_out]
        return subprocess.run(command, check=True, capture_output=True, text=True)
        