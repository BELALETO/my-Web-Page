import localCompiler


class court:
    user_solution = ""
    user_out = ""
    
    main_solution = ""
    main_out = ""
    
    def __init__(self, user_solution, main_solution, user_out, main_out):
        self.user_solution = user_solution
        self.main_solution = main_solution
        
        self.user_out = user_out
        self.main_out = main_out
    
        
    def sentence(self):
        user = localCompiler.compiler(self.user_solution, self.user_out)
        main = localCompiler.compiler(self.main_solution, self.main_out)
        
        return (user.build_Run() == main.build_Run())
        
        
    
