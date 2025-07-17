# Compressor extremo de PDF

Este script em Python reduz ao máximo o tamanho de arquivos PDF, mesmo com perda significativa de qualidade, com o objetivo de atingir um tamanho final em kilobytes definido pelo usuário. Ou seja, você pode ir até o limite máximo que você definir, e a qualidade irá ficar avariada de acordo com o seu critério apenas, chega de depender de sites de compressores de PDF e faça você mesmo!

## Como funciona

1. Você insere um arquivo PDF que quer comprimir na pasta, indica o nome do arquivo comprimido e o tamanho máximo que quer que ele tenha.
2. Cada página do PDF é convertida em uma imagem rasterizada (JPEG).
3. As imagens são comprimidas com diferentes valores de resolução (DPI) e qualidade.
4. Um novo PDF é criado a partir dessas imagens.
5. O processo para automaticamente ao atingir o tamanho máximo especificado ou próximo dele.


## Observações

- O PDF resultante será composto apenas por imagens.
- Textos, links, marcadores e outros elementos interativos serão perdidos.
- A qualidade visual será degradada proporcionalmente à meta de tamanho.
- Ideal para situações onde o tamanho do arquivo é prioridade.

## Exemplo extremo
> "a" é o pdf original, "b" é o pdf após comprimir com o input de 40 KB.
![Imagem de exemplo](https://github.com/AX414/extreme-pdf-compressor-python/blob/main/imgs/img1.png?raw=true)
