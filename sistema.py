from embarcacoes import Embarcacoes


class Sistema:

    def __init__(self):
        # --------- dados do player----------------
        self.args = [' '] * 101
        self.move = 0
        self.opicao = 0
        self.tiroplayer = 0
        self.indicadorboom = 0
        self.direcao = ''
        self.barco = Embarcacoes()
        self.marcaopicao = []
        self.disparos = []
        self.acertos = []
        self.cor = {'Azul': '\033[1;34m',
                    'Remve': '\033[m'
        }
        # -----------------------------------------
        # ----------dodos do bot-------------------
        self.barcobot = Embarcacoes()
        self.direcaobot = ''
        self.opicaobot = 0
        self.posicaobot = 0
        self.marcaopocaobot = []
        self.tirobot = 0
        self.bool1 = False
        self.bool2 = False
        self.moveBot = 1
        self.moveBotConstante = 1
        self.testeLogico = 1
        self.acertosbot = []
        self.disparosbot = []
        self.contAnalise = 0
        self.detectaInverso = 0
    # ----------------------------------------

# ------------------declaração dos métodos-----------------------------------------------
    def EscreverPainel(self, instancia):
        """
        -> Escreve o painel de embarcações na tela
        :param instancia: indica qual classe de embarcações serão exibidas
        :return: None
        """
        n = 1
        for a in range(1, 11):
            for b in range(1, 11):
                if n in instancia.portaavioes or n in instancia.contratorpeideiro or n in instancia.cruzador or \
                        n in instancia.fragata:
                    print(f'{self.cor["Azul"]}[{self.cor["Remve"]}  \033[1;33mO\033[m  {self.cor["Azul"]}]{self.cor["Remve"]}', end=' ')
                else:
                    print(f'{self.cor["Azul"]}[{n:^5}]{self.cor["Remve"]}', end=' ')
                n = n + 1
            print()

    def EscreverPainelEstrategico(self):
        """
        -> Inprime um painel auxiliar na tela mostrando onde o player atirou e onde ele acertou
        :return: Sem retorno
        """
        n = 1
        for a in range(1, 11):
            for b in range(1, 11):
                if n in self.acertos:
                    print(f'[  \033[1;32mX\033[m  ]', end=' ')
                elif n in self.disparos:
                    print(f'[  \033[1;31mX\033[m  ]', end=' ')
                else:
                    print(f'{self.cor["Azul"]}[{n:^5}]{self.cor["Remve"]}', end=' ')
                n = n + 1
            print()

    def ObterOpicaoPlayer(self):
        """
        -> Da input na opição de embarcação que o player deseja posicionar
        :return: Sem retorno
        """
        while True:
            print('''\033[1;30m
[1] Porta Aviões
[2] Cruzador
[3] Contratorpedeiro
[4] Fragata\033[m''')
            try:
                self.opicao = int(input())
            except ValueError:
                print('Apenas valores inteiros')
            if self.opicao > 4 or self.opicao < 1:
                print('Número de embarcação inesistente')
            else:
                break

    def ObterMovimentoPlayer(self):
        """
        -> Da input na 'casa' em que o player deseja posicionar a embarcação
        :return: Sem retorno
        """
        self.move = 0
        while self.move > len(self.args) or self.move <= 0 or self.EposiDeEmbarcacao(self.move, self.opicao, self.barco):
            try:
                self.move = int(input('Digite uma casa: '))
            except:
                print('Digite um valor inteiro')

    def ObterDirecaoPlayer(self):
        """
        -> Input da direção em que o player quer a embarcação (vertical ou horizontal)
        :return: Sem retorno
        """
        while True:
            n = str(input('Digite a direção [v\h]:\n'))
            if n[0] == 'v':
                self.direcao = 'vertical'
                break
            elif n[0] == 'h':
                self.direcao = 'horizontal'
                break
            print('Apenas v ou h')

    def EespacoValido(self, vetor, posi):
        """
        -> Verifica se o a posição solicitada esta dentro do vetor ou seja n <= 100 e n > 0
        :param vetor: vetor solicitado
        :param posi: posição solisitada
        :return: Retorna True se a posição estiver dentro da lista se não False
        """
        try:
            return vetor[posi] == ' '
        except:
            return False

    def EposiDeEmbarcacao(self, posi, op, instancia):
        """
        Verifica se a posi��o solicitada est� dentro da embarca��o com a inst�ncia solicitada.  
        :param posi: Posi��o solicitada.  
        :param op: Op��o da embarca��o.
        :param instancia: Classe de embarca��es que ser� verificada.  
        :return: Retorna `True` se a `posi` estiver em alguma das embarca��es,  
         exceto a embarca��o que estiver com a mesma op��o passada.  
         Caso contr�rio, retorna `False`.  
        """
        return posi in instancia.fragata and op != 4 or posi in instancia.contratorpeideiro and op != 3 or \
               posi in instancia.cruzador and op != 2 or posi in instancia.portaavioes and op != 1

    def EposicaoValida(self, derect, posi, op, instancia):
        """
        -> Funcao que verifica se a embarcação esta em um local valido
        :param derect: direção da embarcação (vertical ou horizontal)
        :param posi: posição inicial da embarcação
        :param op: opição de qual e a embarcação
        :param instancia: classe de embarcação que sera analísada
        :return: None
        """
        p = posi
        if op == 1:
            tan = instancia.portaavioes[:]
        elif op == 2:
            tan = instancia.cruzador[:]
        elif op == 3:
            tan = instancia.contratorpeideiro[:]
        else:
            tan = instancia.fragata[:]

        for c in range(len(tan)):
            if derect == 'vertical':
                if self.EposiDeEmbarcacao(p, op, instancia) or not self.EespacoValido(self.args, p):
                    #print(f'Erro detectado 1{tan}')
                    return False
                tan[c] = p
                p = p + 10
            elif derect == 'horizontal':
                if self.EposiDeEmbarcacao(p, op, instancia) or not self.EespacoValido(self.args, p):
                    #print(f'Erro detectado 2{tan}')
                    return False
                tan[c] = p
                p = p + 1
        if derect == 'horizontal':
            if 10 in tan and 11 in tan or 20 in tan and 21 in tan or 30 in tan and 31 in tan or \
                    40 in tan and 41 in tan or 50 in tan and 51 in tan or 60 in tan and 61 in tan or 70 in tan and 71 in tan or \
                    80 in tan and 81 in tan or 90 in tan and 91 in tan:
                #print(f'Erro detectado 3{tan}')
                return False
        #print(f'valido: {tan}')
        return True

    def MarcaEmbarcacoes(self, direcao, op, posi, instanica):
        """
        -> Função que grava a posição de cada embarcação
        :param direcao: direção da embarcação (vertical ou horizontal)
        :param op: opicão de qual embarcação
        :param posi: posição inicial
        :param instanica: instancia de embarcações
        :return: None
        """
        if op == 1:
            tanM = instanica.portaavioes
        elif op == 2:
            tanM = instanica.cruzador
        elif op == 3:
            tanM = instanica.contratorpeideiro
        else:
            tanM = instanica.fragata

        for c in range(len(tanM)):
            if direcao == 'vertical':
                tanM[c] = posi
                posi = posi + 10
            else:
                tanM[c] = posi
                posi = posi + 1
        #print(tanM)

    def ObterTiroPlayer(self):
        """
        -> Input na 'casa' em que o player ira disparar o tiro
        :return: Sem retorno
        """
        self.tiroplayer = 0
        while self.tiroplayer > len(self.args) or self.tiroplayer <= 0 or self.tiroplayer in self.disparos or \
                self.tiroplayer in self.acertos:
            try:
                self.tiroplayer = int(input('\033[1;30mDigite o a casa para o tiro:\033[m\n'))
            except ValueError:
                print('Apenas valores interios')

    def MarcarTiro(self, instancia, atributotiro):
        """
        -> Marca na Classe de embarcação passada 0 ou seja que atingiu-la com o tiro eliminando
        UMA parte de seus dados
        :param instancia: Embarcações que serão manipuladas
        :param atributotiro: valor do tiro passado
        :return: Retorna True se o valor de tiro passado estiver dentro da instancia de embarcações,
        se não sem retorno
        """
        if atributotiro in instancia.portaavioes:
            instancia.portaavioes[instancia.portaavioes.index(atributotiro)] = 0
            return True
        elif atributotiro in instancia.cruzador:
            instancia.cruzador[instancia.cruzador.index(atributotiro)] = 0
            return True
        elif atributotiro in instancia.contratorpeideiro:
            instancia.contratorpeideiro[instancia.contratorpeideiro.index(atributotiro)] = 0
            return True
        elif atributotiro in instancia.fragata:
            instancia.fragata[instancia.fragata.index(atributotiro)] = 0
            return True
        else:
            print('Você não acetou nem uma embarcação')

    def Evitoria(self, instanicia):
        """
        -> Identifica se ouve vitoria
        :param instanicia: embarcações que serão analísadas
        :return: Retorna True se todas as somas de todas embarcações forem 0, ou seja estiverem sem dados,
        se não retorna False
        """
        return sum(instanicia.portaavioes) == 0 and sum(instanicia.cruzador) == 0 and \
               sum(instanicia.contratorpeideiro) == 0 and sum(instanicia.fragata) == 0

    def Marca(self, instancia, operacao):
        """
        -> Adiciona a uma lista passada
        :param instancia: instanica de lista passada
        :param operacao: valor que sera adicionado
        :return: Sem retorno
        """
        instancia.append(operacao)

    def MarcaAcertos(self, instancia):
        """
        -> Adiciona a uma lista passada o atributo 'self.tiroPlayer'
        :param instancia: instanica de lista passada
        :return: Sem retorno
        """
        instancia.append(self.tiroplayer)

    def ObterPosicaoBot(self):
        """
        -> Input de uma forma aleatoria a 'casa' em que o bot marcara
        :return: Sem retorno
        """
        import random
        n = random.randint(1, 100)
        self.posicaobot = n

    def ObterOpicaoBot(self):
        """
        -> Input de uma forma aleatória a opição da embarcação
        :return: Sem retorno
        """
        import random
        n = random.randint(1, 4)
        if n == 1:
            self.opicaobot = 1
        elif n == 2:
            self.opicaobot = 2
        elif n == 3:
            self.opicaobot = 3
        else:
            self.opicaobot = 4

    def ObterDirecaoBot(self):
        """
        -> Input de uma forma aleatórtia a direção do bot (vertical se n for 1 e horizontal se n for 0)
        :return: Sem retorno
        """
        import random
        n = random.randint(0, 1)
        if n == 0:
            self.direcaobot = 'horizontal'
        else:
            self.direcaobot = 'vertical'

    def ObterTiroBot(self):
        """
        -> Marca de uma forma analítica um 'casa' para  o bot posicionar. De forma geral esse e o 'cérebro' do Bot.
        incialmente o Bot soreteara um valor aleatório e se esse valor estiver dentro de algumas embarcações do player
        ele comecara o script. Inicialmente existem 4 posibilidades de verificação a n - 10 (cima), n + 1 (direita),
        n + 10 (baixo) e n - 1 (esqueda), dessa forma ele analisara nessar opições, lógico se ele não encontrar nem uma
        parte da embarcação do pleyer nessa verificação, ele retornara mesmo assim , pois, se não, seria vantajoso para
        o bot. OBS: self.moveBot != 10 serve para evitar um bug =P
        :return: Retorna a posição analisada ou a soretada
        """
        import random
        if self.bool1:
            if self.testeLogico == 1:
                if self.moveBot != 10 and self.moveBot - 10 in self.barco.fragata or self.moveBot - 10 in self.barco.contratorpeideiro or \
                        self.moveBot - 10 in self.barco.cruzador or self.moveBot - 10 in self.barco.portaavioes:
                    # ---------------------------------------------------------------
                    self.contAnalise = self.contAnalise + 1
                    if self.contAnalise == 1:
                        self.detectaInverso = self.moveBot + 10
                    # ---------------------------------------------------------------
                    self.moveBot = self.moveBot - 10
                    #print(f'encontrei um embarcação na posição {self.moveBot}')
                    return self.moveBot
                else:
                    self.testeLogico = 2
                    #print(f'Nâo encontrei nada na verificação n - 10 porém retornarei a mesma:{self.moveBot - 10}')
                    return self.moveBot - 10
            if self.testeLogico == 2:
                if self.moveBot + 1 in self.barco.fragata or self.moveBot + 1 in self.barco.contratorpeideiro or \
                        self.moveBot + 1 in self.barco.cruzador or self.moveBot + 1 in self.barco.portaavioes:
                    # ---------------------------------------------------------------
                    self.contAnalise = self.contAnalise + 1
                    if self.contAnalise == 1:
                        self.detectaInverso = self.moveBot - 1
                    # ---------------------------------------------------------------
                    self.moveBot = self.moveBot + 1
                    #print(f'encontrei um embarcação na posição {self.moveBot}')
                    return self.moveBot
                else:
                    self.testeLogico = 3
                    #print(f'Nâo encontrei nada na verificação n + 1 porém retornarei a mesnma:{self.moveBot - 10}')
                    return self.moveBot + 1
            if self.testeLogico == 3:
                if self.moveBot + 10 in self.barco.fragata or self.moveBot + 10 in self.barco.contratorpeideiro or \
                        self.moveBot + 10 in self.barco.cruzador or self.moveBot + 10 in self.barco.portaavioes:
                    # ---------------------------------------------------------------
                    self.contAnalise = self.contAnalise + 1
                    if self.contAnalise == 1:
                        self.detectaInverso = self.moveBot - 10
                    # ---------------------------------------------------------------
                    self.moveBot = self.moveBot + 10
                    #print(f'encontrei um embarcação na posição {self.moveBot}')
                    return self.moveBot
                else:
                    self.testeLogico = 4
                    #print(f'Nâo encontrei nada na verificação n + 10 porém retornarei a mesma:{self.moveBot - 10}')
                    return self.moveBot + 10
            if self.testeLogico == 4:
                if self.moveBot - 1 in self.barco.fragata or self.moveBot - 1 in self.barco.contratorpeideiro or \
                        self.moveBot - 1 in self.barco.cruzador or self.moveBot - 1 in self.barco.portaavioes:
                    # ---------------------------------------------------------------
                    self.contAnalise = self.contAnalise + 1
                    if self.contAnalise == 1:
                        self.detectaInverso = self.moveBot + 1
                    # ---------------------------------------------------------------
                    self.moveBot = self.moveBot - 1
                    #print(f'encontrei um embarcação na posição {self.moveBot}')
                    return self.moveBot
                else:
                    self.bool1 = False
                    # ---------------------------------------------------------------
                    self.bool2 = True
                    # ---------------------------------------------------------------
                    #print(f'Não encontrei nada em todas as minhas verificações retornarei a ultima verificação n - 1:{self.moveBot - 1}')
                    self.testeLogico = 1
                    return self.moveBot - 1

        else:
            n = random.randint(1, 100)
            # ----------------------------------------------------------------
            if self.bool2 and self.detectaInverso != 0:
                #print(f'irei analisar em baixo do começõ {self.detectaInverso}')
                n = self.detectaInverso
                self.bool2 = False
                self.contAnalise = 0
                self.detectaInverso = 0
            if n in self.barco.fragata or n in self.barco.contratorpeideiro or \
                    n in self.barco.cruzador or n in self.barco.portaavioes:
                #print(f'encontrei um enbarcação na posição {n}')
                self.bool1 = True
            self.moveBot = n
            #print(f'Não encotrei nada randomizei o valor {n}')
            return self.moveBot

    def MostraNavioAfundado(self):
        if sum(self.barco.fragata) == 0 and self.barco.indfragata:
            print('\033[1;33mBOOMM! A SUA FRAGATA FOI DESTRUIDA111\033[m')
            self.barco.indfragata = False
        elif sum(self.barco.contratorpeideiro) == 0 and self.barco.indcontra:
            print('\033[1;33mBOOM! O BOT AFUNDOU O SEU CONTRATORPEDEIRO!!!\033[m')
            self.barco.indcontra = False
        elif sum(self.barco.cruzador) == 0 and self.barco.indicruz:
            print('\033[1;33mBOOM! O BOT AFUNDOU O SEU CRUZADOR!!!\033[m')
            self.barco.indicruz = False
        elif sum(self.barco.portaavioes) == 0 and self.barco.indporta:
            print('\033[1;33mBOOM O BOT AFUNDOU O SEU PORTA-AVIÕES!!!\033[m')
            self.barco.indporta = False
