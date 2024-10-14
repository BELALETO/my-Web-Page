import localCompiler


class court:
    user_solution = ""
    user_out = ""
    input_file = ""
    
    main_solution = ""
    main_out = ""
    
    def __init__(self, user_solution, main_solution, user_out, main_out, input_file):
        self.user_solution = user_solution
        self.main_solution = main_solution
        
        self.user_out = user_out
        self.main_out = main_out
        
        self.input_file = input_file
    
        
    def sentence(self):
        user = localCompiler.compiler(self.user_solution, self.user_out, self.input_file)
        main = localCompiler.compiler(self.main_solution, self.main_out, self.input_file)
        
        return (user.build_Run() == main.build_Run())
        
        
    
