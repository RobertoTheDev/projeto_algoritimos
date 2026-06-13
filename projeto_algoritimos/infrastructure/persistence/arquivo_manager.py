class ArquivoManager:

    def __init__(self, caminho):
        self.caminho = caminho

    def ler_linhas(self):
        try:
            with open(
                self.caminho,
                "r",
                encoding="utf-8"
            ) as arquivo:
                return arquivo.readlines()
            
        except FileNotFoundError:
            return []
        
    def escrever_linhas(self, linhas):
        with open(
            self.caminho,
            "w",
            encoding="utf-8"
        ) as arquivo:
            arquivo.writelines(linhas)