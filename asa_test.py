import subprocess
class Aitalker:
    def __init__(self, prompt) -> None:
        self.prompt = ""

    def ai (prompt, response):
        output = subprocess.run(['ollama', 'run', 'llama3.2', prompt] stdout=subprocess.PIPE)
        response = output.stdoud.decode('utf-8')
        print(response)
 
test = Aitalker()
test.ai("What is 2+2")