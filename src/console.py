class Console:
    clean = "\033[m"
    blue = "\033[34m"
    red = "\033[31m"
    pink = "\033[35m"
    yellow = "\033[33m"
    cyan = "\033[36m"
    green = "\033[32m"
    grey = "\033[37m"

    @classmethod
    def log(cls, color: str, content: str):
        print(f"{color}{content}{cls.clean}")
