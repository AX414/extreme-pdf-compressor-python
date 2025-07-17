# Compressor extremo de PDF

Este script em Python reduz ao máximo o tamanho de arquivos PDF, mesmo com perda significativa de qualidade, com o objetivo de atingir um tamanho final em kilobytes definido pelo usuário. Ou seja, você pode ir até o limite máximo que você definir, e a qualidade irá ficar avariada de acordo com o seu critério apenas, chega de depender de sites de compressores de PDF e faça você mesmo!

## Como funciona

1. Cada página do PDF é convertida em uma imagem rasterizada (JPEG).
2. As imagens são comprimidas com diferentes valores de resolução (DPI) e qualidade.
3. Um novo PDF é criado a partir dessas imagens.
4. O processo para automaticamente ao atingir o tamanho máximo especificado.

## Observações

- O PDF resultante será composto apenas por imagens.
- Textos, links, marcadores e outros elementos interativos serão perdidos.
- A qualidade visual será degradada proporcionalmente à meta de tamanho.
- Ideal para situações onde o tamanho do arquivo é prioridade.