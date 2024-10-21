import subprocess
import os

class CPPCompilerRunner:
    
    def compile_and_run(self, cpp_file, output_executable, input_file=None):
        # Compile the C++ file
        compile_command = ["g++", cpp_file, "-o", output_executable]
        try:
            subprocess.run(compile_command, check=True)
        except subprocess.CalledProcessError as e:
            return f"Compilation failed for {cpp_file}: {e}"
        
        # Run the executable
        try:
            if input_file:
                # If there is an input file, provide it as stdin
                with open(input_file, "r") as input_f:
                    result = subprocess.run([f"./{output_executable}"], stdin=input_f, text=True, capture_output=True)
            else:
                # Run without input file
                result = subprocess.run([f"./{output_executable}"], text=True, capture_output=True)
            
            # Capture the output and error
            output = result.stdout.strip()  # Strip extra spaces/newlines
            error = result.stderr
            
            if error:
                return f"Error during execution of {cpp_file}: {error.strip()}"
            return output
        except subprocess.CalledProcessError as e:
            return f"Execution failed for {cpp_file}: {e}"

    def compare_outputs(self, cpp_file_1, cpp_file_2, output_executable_1, output_executable_2, input_file=None):
        # Compile and run the first C++ program
        output_1 = self.compile_and_run(cpp_file_1, output_executable_1, input_file)
        
        # Compile and run the second C++ program
        output_2 = self.compile_and_run(cpp_file_2, output_executable_2, input_file)
        
        # Check if any of the outputs have errors
        if "Error" in output_1:
            return f"First program error: {output_1}"
        if "Error" in output_2:
            return f"Second program error: {output_2}"
        
        # Compare the outputs
        if output_1 == output_2:
            print("The outputs are the same.")
            return True
        else:
            print(f"The outputs are different.\nOutput 1:\n{output_1}\nOutput 2:\n{output_2}")
            return False