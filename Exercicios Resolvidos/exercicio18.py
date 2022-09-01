"""
18) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de
um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando
este link (em minutos).
"""
tamanho_arquivo = float(input('Tamanho do arquivo(MB): '))
velocidade_internet = float(input('Velocidade de um link de internet(Mbps): '))
tempo_download = tamanho_arquivo / velocidade_internet
tempo_minutos = tempo_download / 60
print('Tempo aproximado para download: {:.2f} minutos'.format(tempo_minutos))