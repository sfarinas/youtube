from hashlib import sha256
import time 

#url = "https://www.youtube.com/watch?v=ae6w0-kZ3-M"
#file = "aranha.mp4"
#yt_download(url,file)
def aplicar_sha256(texto):

    return(sha256(texto.encode("ascii")).hexdigest())


def minerar(num_bloco, transacoes, hash_anterior, qtde_zero):
    nonce = 0

    while True:
        texto = str(num_bloco) + transacoes + hash_anterior + str(nonce)  
        meu_hash = aplicar_sha256(texto)  
        if meu_hash.startswith("0" * qtde_zero):
            return nonce, meu_hash
        nonce += 1