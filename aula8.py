velocidade = 61  # velocidade atual do carro
local_carro = 101  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

if velocidade > RADAR_1:
    print('Carro passou do radar')

if local_carro >= (LOCAL_1+RADAR_RANGE) and local_carro <= (LOCAL_1 + RADAR_RANGE) and velocidade > RADAR_1:
    print('carro multado em radar 1')