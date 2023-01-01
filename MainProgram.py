from PySimpleGUI import PySimpleGUI as sg

class MainScreen:

    def __init__(self) -> None:
        
        root = [
            [sg.Text('Usuário:')],
            [sg.Input(key='usuario')],
            [sg.Text('Senha:')],
            [sg.Input(key='senha')],
            [sg.Button('Cadastrar'), sg.Button('Logar')]
        ]
    
        window = sg.Window('Login').layout(root)
        self.events, self.values = window.read()


        if self.events == 'Cadastrar':
            usuario = self.values['usuario']
            usu = True
            
            if self.values['usuario'] != '':

                if usu == True:


                    with open('Nome_Usuario.txt', 'r') as Arc_Nomes:
                        LerNomes = Arc_Nomes.readlines()
                        for i in range(len(LerNomes)):
                            if usuario == LerNomes[i]:
                                usu = False
                                print('Usuário já existe')
                    usuario = self.values['usuario']
                    LerNomes = list(map(lambda x: x.replace('\n', ''), LerNomes))

                        
                    
                    if usu == True:

                        with open('Nome_Usuario.txt', 'a') as nomes:
                            nomes.write(self.values['usuario'] + '\n')
                        with open('Senha_Usuario.txt', 'a') as senhas:
                                senhas.write(self.values['senha'] + '\n')   
                                print('usuario cadastrado')

            else:
                print('campos não preenchidos')
                        

        if self.events == 'Logar':
            with open('Nome_Usuario.txt', 'r') as Arc_Nomes:
                LerNomes = Arc_Nomes.readlines()
            with open('Senha_Usuario.txt', 'r') as Arc_Senhas:
                LerSenhas = Arc_Senhas.readlines()

            LerNomes = list(map(lambda x: x.replace('\n', ''), LerNomes))
            LerSenhas = list(map(lambda x: x.replace('\n', ''), LerSenhas))

            usuario = self.values['usuario']
            senha = self.values['senha']
            logado = False
            for i in range(len(LerNomes)):
                if usuario == LerNomes[i] and senha == LerSenhas[i]:
                    logado = True
            if not logado:
                print('Usuário não existe')
            else: 
                print('Usuario logado')
                


janela = MainScreen()