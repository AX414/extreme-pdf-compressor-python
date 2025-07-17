import fitz
from PIL import Image
import os
import shutil

def gerar_pdf_de_imagens(caminhos_imagens, caminho_saida):
    """
    Gera um novo arquivo PDF a partir de uma lista de imagens.
    Cada imagem vira uma página do PDF com o mesmo tamanho da imagem original.
    """
    pdf = fitz.open()
    for caminho_imagem in caminhos_imagens:
        imagem_doc = fitz.open(caminho_imagem)
        retangulo = imagem_doc[0].rect
        pagina = pdf.new_page(width=retangulo.width, height=retangulo.height)
        pagina.insert_image(retangulo, filename=caminho_imagem)
    pdf.save(caminho_saida)
    pdf.close()

def comprimir_pdf_tamanho_maximo(caminho_entrada, caminho_saida, tamanho_max_kb):
    """
    Comprime um arquivo PDF para que ele fique com tamanho menor ou igual ao especificado (em KB).
    Converte as páginas do PDF em imagens JPEG com diferentes resoluções e qualidades até atingir o tamanho desejado.
    """
    print(f"\nLendo PDF de entrada: {caminho_entrada}")
    tamanho_original_kb = os.path.getsize(caminho_entrada) / 1024
    print(f"Tamanho original: {tamanho_original_kb:.2f} KB")

    if tamanho_original_kb <= tamanho_max_kb:
        print(f"O arquivo já está abaixo de {tamanho_max_kb} KB. Nenhuma compressão será aplicada.")
        shutil.copy(caminho_entrada, caminho_saida)
        print(f"Arquivo copiado para: {caminho_saida}")
        return

    documento = fitz.open(caminho_entrada)
    pasta_temporaria = "paginas_temp"
    os.makedirs(pasta_temporaria, exist_ok=True)

    for dpi in range(100, 30, -10):
        # DPI (dots per inch) define a resolução das imagens geradas das páginas.
        # DPI maior = melhor qualidade e maior tamanho.
        # DPI menor = menor qualidade e menor tamanho.

        for qualidade in range(95, 4, -10):
            # A qualidade define o nível de compressão JPEG (95 = alta qualidade, 5 = muito compactado).
            print(f"Tentando compressão com DPI={dpi}, qualidade JPEG={qualidade}...")

            caminhos_imagens = []
            for i in range(len(documento)):
                imagem = documento[i].get_pixmap(dpi=dpi)
                caminho_img = os.path.join(pasta_temporaria, f"pagina_{i}.jpg")
                Image.frombytes("RGB", [imagem.width, imagem.height], imagem.samples)\
                    .save(caminho_img, "JPEG", quality=qualidade, optimize=True)
                caminhos_imagens.append(caminho_img)

            gerar_pdf_de_imagens(caminhos_imagens, caminho_saida)

            tamanho_final_kb = os.path.getsize(caminho_saida) / 1024
            print(f"Tamanho atual do PDF: {tamanho_final_kb:.2f} KB")

            for arquivo in caminhos_imagens:
                os.remove(arquivo)

            if tamanho_final_kb <= tamanho_max_kb:
                print(f"Compressão concluída com sucesso. Arquivo final: {caminho_saida}")
                documento.close()
                os.rmdir(pasta_temporaria)
                return

    print("Não foi possível atingir o tamanho desejado com os níveis máximos de compressão.")
    documento.close()
    os.rmdir(pasta_temporaria)

if __name__ == "__main__":
    print("\n=== COMPRESSOR DE PDF ===")
    nome_entrada = input("Nome do arquivo PDF de entrada (ex: arquivo): ").strip()
    nome_saida = input("Nome para salvar o arquivo comprimido (ex: comprimido): ").strip()

    if not nome_entrada.lower().endswith(".pdf"):
        nome_entrada += ".pdf"
    if not nome_saida.lower().endswith(".pdf"):
        nome_saida += ".pdf"

    try:
        tamanho_max_kb = int(input("Tamanho máximo desejado (em KB): ").strip())
    except ValueError:
        print("Erro: valor inválido. Digite apenas números inteiros.")
        exit()

    try:
        comprimir_pdf_tamanho_maximo(nome_entrada, nome_saida, tamanho_max_kb)
    except Exception as erro:
        print(f"Erro durante o processo: {erro}")
