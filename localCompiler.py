import subprocess

class CPPCompilerRunner:
    
    # The name of the method descripe it self bro :)    
    def compile_and_run(self, cpp_file, output_executable, input_file=None):
       
        compile_command = ["g++", cpp_file, "-o", output_executable]
        try:
            subprocess.run(compile_command, check=True)
        except subprocess.CalledProcessError as e:
            return f"Compilation failed for {cpp_file}: {e}"
        
       
        try:
            if input_file:
                with open(input_file, "r") as input_f:
                    result = subprocess.run([f"./{output_executable}"], stdin=input_f, text=True, capture_output=True)
            else:
                result = subprocess.run([f"./{output_executable}"], text=True, capture_output=True)
            
            output = result.stdout.strip()  
            error = result.stderr
            
            if error:
                return f"Error during execution of {cpp_file}: {error.strip()}"
            return output
        except subprocess.CalledProcessError as e:
            return f"Execution failed for {cpp_file}: {e}"

    # Method to compile 2 file and compare their outputs.
    def compare_outputs(self, cpp_file_1, cpp_file_2, output_executable_1, output_executable_2, input_file=None):
        output_1 = self.compile_and_run(cpp_file_1, output_executable_1, input_file)
        
        output_2 = self.compile_and_run(cpp_file_2, output_executable_2, input_file)
        
        if "Error" in output_1:
            return f"First program error: {output_1}"
        if "Error" in output_2:
            return f"Second program error: {output_2}"
        
        # Compare the outputs
        if output_1 == output_2:
            return True
        else:
            return False