# ----------------------------Inicialização do sistema---------------------------------------------------
from sistema import Sistema
system = Sistema()
# -------------------------------------------------------------------------------------------------------
# --------------------Imput dos dados das embarcações do bot---------------------------------------------
for c in range(0, 4):
    while True:
        system.ObterPosicaoBot()
        while True:
            system.ObterOpicaoBot()
            if not system.opicaobot in system.marcaopocaobot:
                break
        system.ObterDirecaoBot()
        if system.EposicaoValida(system.direcaobot, system.posicaobot, system.opicaobot, system.barcobot):
            system.MarcaEmbarcacoes(system.direcaobot, system.opicaobot, system.posicaobot, system.barcobot)
            system.Marca(system.marcaopocaobot, system.opicaobot)
            break
# ------------------------------------------------------------------------------------------------------
# -------------------Input dos dados das embarcações do player------------------------------------------
while True:
    system.EscreverPainel(system.barco)
    while True:
        system.ObterOpicaoPlayer()
        if system.opicao in system.marcaopicao:
            print('Embarcação ja posicionada')
        else:
            system.Marca(system.marcaopicao, system.opicao)
            break
    system.ObterDirecaoPlayer()
    while True:
        system.ObterMovimentoPlayer()
        if system.EposicaoValida(system.direcao, system.move, system.opicao, system.barco):#
            system.MarcaEmbarcacoes(system.direcao, system.opicao, system.move, system.barco)
            break
        else:
            print('Não foi possivel posicionar a embarcação')
    if len(system.marcaopicao) == 4:
        break
# -----------------------------------------------------------------------------------------------------

# -------------------------------Seção da guerra entre o player e o bot--------------------------------
while True:
    system.ObterTiroPlayer()
    if system.MarcarTiro(system.barcobot, system.tiroplayer):
        print(f'\033[1;32m{"VOCÊ ACETOU UMA EMBARCAÇÃO NA POSIÇÃO"} {system.tiroplayer}\033[m')
        system.MarcaAcertos(system.acertos)
    system.Marca(system.disparos, system.tiroplayer)
    print(f'\033[4;32m{"PAINEL DA SUAS EMBARCAÇÕES":^60}\033[m')
    system.EscreverPainel(system.barco)
    print(f'\033[4;32m{"PAINEL DE DISPAROS":^60}\033[m')
    system.EscreverPainelEstrategico()
    print(f'\033[1;32mTiros acertados: {system.acertos}\033[m|\033[1;31mTiros disparados {system.disparos}\033[m')
    while True:
        system.ObterTiroBot()
        if not system.moveBot in system.disparosbot:
            system.Marca(system.disparosbot, system.moveBot)
            break
    system.MostraNavioAfundado()
    system.MarcarTiro(system.barco, system.moveBot)
    if system.Evitoria(system.barco) or system.Evitoria(system.barcobot):
        break
# ---------------------------------------------------------------------------------------------------
print('Versão inicial ainda =P')
