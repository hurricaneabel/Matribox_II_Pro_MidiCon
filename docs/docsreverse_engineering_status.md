Projeto: Matribox Controller (Matribox II Pro)



Status atual:



\- decode\_sysex já identifica:

&#x20; - Presets (banco + letra)

&#x20; - Modo stomp/preset

&#x20; - Drum on/off

&#x20; - Effect block on/off (12 slots)



Arquivos principais:

\- matribox\_sysex.py

\- matribox\_listener.py

\- matribox\_state.py

\- reverse\_listener.py



Objetivo atual:

\- Engenharia reversa dos modelos de efeitos.

\- Descobrir IDs dos efeitos para permitir edição pelo software.



Descobertas:



Mensagens de troca de modelo:

\- LEN=108

\- DATA8=48



Categoria DYN:



(data\[58], data\[59])



(0,0)  = COMP1

(0,1)  = COMP2

(0,3)  = COMP3

(1,4)  = M-Boost

(1,10) = E-Boost

(0,10) = AC-Boost



Observações:

\- Os pacotes LEN=126 parecem ser atualização geral da cadeia.

\- Os pacotes LEN=108 carregam o modelo real do efeito.

\- data\[58] e data\[59] parecem identificar o efeito.



Próximo passo:

\- Continuar mapeando todos os efeitos da categoria DYN.

\- Depois descobrir outras categorias (DRV, AMP, MOD, DLY, REV etc.).

\- Em seguida localizar os parâmetros de cada efeito.

