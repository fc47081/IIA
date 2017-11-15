:- ['/home/mooshak-2/iiaimp/prolog/metro_lisboa.pl'].

% estacao(CorLinha,Nome,Ano)
% A estacao Nome pertence a linha CorLinha e foi inaugurada no ano Ano.

estacao(amarela,'Ameixoeira',2004).
estacao(amarela,'Campo Grande',1993).
estacao(amarela,'Campo Pequeno',1959).
estacao(amarela,'Cidade Universitaria',1988).
estacao(amarela,'Entre Campos',1959).
estacao(amarela,'Lumiar',2004).
estacao(amarela,'Marques de Pombal',1995).
estacao(amarela,'Odivelas',2004).
estacao(amarela,'Picoas',1959).
estacao(amarela,'Quinta das Conchas',2004).
estacao(amarela,'Rato',1997).
estacao(amarela,'Saldanha',1959).
estacao(amarela,'Senhor Roubado',2004).
estacao(azul,'Alfornelos',2004).
estacao(azul,'Alto dos Moinhos',1988).
estacao(azul,'Amadora Este',2004).
estacao(azul,'Avenida',1959).
estacao(azul,'Baixa-Chiado',1998).
estacao(azul,'Carnide',1997).
estacao(azul,'Colegio Militar/Luz',1988).
estacao(azul,'Jardim Zoologico',1959).
estacao(azul,'Laranjeiras',1988).
estacao(azul,'Marques de Pombal',1959).
estacao(azul,'Parque',1959).
estacao(azul,'Pontinha',1997).
estacao(azul,'Praca de Espanha',1959).
estacao(azul,'Reboleira',2016).
estacao(azul,'Restauradores',1959).
estacao(azul,'Santa Apolonia',2007).
estacao(azul,'Sao Sebastiao',1959).
estacao(azul,'Terreiro do Paco',2007).
estacao(verde,'Alameda',1972).
estacao(verde,'Alvalade',1972).
estacao(verde,'Anjos',1966).
estacao(verde,'Areeiro',1972).
estacao(verde,'Arroios',1972).
estacao(verde,'Baixa-Chiado',1998).
estacao(verde,'Cais do Sodre',1998).
estacao(verde,'Campo Grande',1993).
estacao(verde,'Intendente',1966).
estacao(verde,'Martim Moniz',1966).
estacao(verde,'Roma',1972).
estacao(verde,'Rossio',1963).
estacao(verde,'Telheiras',2002).
estacao(vermelha,'Aeroporto',2012).
estacao(vermelha,'Alameda',1998).
estacao(vermelha,'Bela Vista',1998).
estacao(vermelha,'Cabo Ruivo',1998).
estacao(vermelha,'Chelas',1998).
estacao(vermelha,'Encarnacao',2012).
estacao(vermelha,'Moscavide',2012).
estacao(vermelha,'Olaias',1998).
estacao(vermelha,'Olivais',1998).
estacao(vermelha,'Oriente',1998).
estacao(vermelha,'Saldanha',2009).
estacao(vermelha,'Sao Sebastiao',2009).

%% liga(X,Y)
%% Existe uma ligacao da estacao X para a estacao Y.

liga('Ameixoeira','Lumiar').
liga('Campo Grande','Cidade Universitaria').
liga('Campo Pequeno','Saldanha').
liga('Cidade Universitaria','Entre Campos').
liga('Entre Campos','Campo Pequeno').
liga('Lumiar','Quinta das Conchas').
liga('Marques de Pombal','Rato').
liga('Odivelas','Senhor Roubado').
liga('Picoas','Marques de Pombal').
liga('Quinta das Conchas','Campo Grande').

liga('Saldanha','Picoas').
liga('Senhor Roubado','Ameixoeira').
liga('Alfornelos','Pontinha').
liga('Alto dos Moinhos','Laranjeiras').
liga('Amadora Este','Alfornelos').
liga('Avenida','Restauradores').
liga('Baixa-Chiado','Terreiro do Paco').
liga('Carnide','Colegio Militar/Luz').
liga('Colegio Militar/Luz','Alto dos Moinhos').
liga('Jardim Zoologico','Praca de Espanha').
liga('Laranjeiras','Jardim Zoologico').
liga('Marques de Pombal','Avenida').
liga('Parque','Marques de Pombal').
liga('Pontinha','Carnide').
liga('Praca de Espanha','Sao Sebastiao').
liga('Reboleira','Amadora Este').
liga('Restauradores','Baixa-Chiado').

liga('Sao Sebastiao','Parque').
liga('Terreiro do Paco','Santa Apolonia').
liga('Alameda','Arroios').
liga('Alvalade','Roma').
liga('Anjos','Intendente').
liga('Areeiro','Alameda').
liga('Arroios','Anjos').
liga('Baixa-Chiado','Cais do Sodre').

liga('Campo Grande','Alvalade').
liga('Intendente','Martim Moniz').
liga('Martim Moniz','Rossio').
liga('Roma','Areeiro').
liga('Rossio','Baixa-Chiado').
liga('Telheiras','Campo Grande').
liga('Aeroporto','Encarnacao').
liga('Alameda','Saldanha').
liga('Bela Vista','Olaias').
liga('Cabo Ruivo','Olivais').
liga('Chelas','Bela Vista').
liga('Encarnacao','Moscavide').
liga('Moscavide','Oriente').
liga('Olaias','Alameda').
liga('Olivais','Chelas').
liga('Oriente','Cabo Ruivo').
liga('Saldanha','Sao Sebastiao').

caminho(E1,E2,Caminho):-
    forall(liga(X,Y), assert(liga(Y,X))),
    travel(E1,E2,[E1],AccCaminho),
    reverse(AccCaminho,Caminho).

travel(E1,E2,CaminhoSoFar,[E2|CaminhoSoFar]):-
    liga(E1,E2).

travel(E1,E2,CaminhoSoFar,Caminho):-
    liga(E1, NextStation),
    NextStation \== E2,
    \+ member(NextStation, CaminhoSoFar),
    travel(NextStation,E2,[NextStation|CaminhoSoFar], Caminho).
