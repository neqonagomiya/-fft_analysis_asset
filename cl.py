class Colin:
    BLACK           = '\033[30m'
    RED             = '\033[31m'
    GREEN           = '\033[32m'
    YELLOW          = '\033[33m'
    BLUE            = '\033[34m'
    MAGENTA         = '\033[35m'
    CYAN            = '\033[36m'
    WHITE           = '\033[37m'
    COLOR_DEFAULT   = '\033[39m'
    BOLD            = '\033[1m'
    UNDERLINE       = '\033[4m'
    END             = '\033[0m'    
    
    def cstr(self, txt, color=RED):
        return f"{color}{txt}{self.END}"
    
    def cprint(self, txt, color=RED):
        print(f"{color}{txt}{self.END}")


