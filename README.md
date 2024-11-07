# Projeto de TCC - Lucas de A. Louzada - 2023

## Segmentação da Articulação Sacroilíaca em Imagens de Ressonância Magnética Utilizando a Rede Neural Convolucional nnU-Net

## Descrição do Projeto

Este repositório contém o código fonte do projeto de TCC do curso de Informática Biomédica da Universidade de São Paulo (USP) desenvolvido por Lucas de A. Louzada. O projeto realiza a segmentação da articulação sacroilíaca em imagens de ressonância magnética por meio da rede neural convolucional nnU-Net.

Especificamente, o repositório abrange o pré-processamento das imagens e máscaras, incluindo a expansão da base de dados com a biblioteca **Albumentations** para aumento de dados. Além disso, estão incluídos scripts de análise dos resultados obtidos. O treinamento do modelo foi realizado no Google Colab com suporte a GPU.

Este repositório foi configurado para trabalhar com a base de dados pública *HCFMRP_sacroiliitis_v1*, que foi previamente estruturada e anonimizada para uso em pesquisas, contando com a aprovação do Comitê de Ética em Pesquisa do Hospital das Clínicas de Ribeirão Preto (CEP-HCRP), sob parecer número 1.951.052.

- **Notebook do treinamento - git**: [nnunet_tcc.ipynb - git](https://github.com/LLouzada/tcc/blob/master/nnunet_tcc.ipynb)

- **Notebook do treinamento - colab**: [nnunet_tcc.ipynb - colab](https://colab.research.google.com/drive/138njb6bvCkxIeRqZCvoWbAUSy7Y8kGMn?usp=sharing)

## Autor

- Lucas de A. Louzada - [GitHub](https://github.com/LLouzada)

## Orientador

- Prof. Dr. Paulo Mazzoncini de Azevedo Marques

## Resultados

- **Monografia**: [Monografia Completa - PDF](https://github.com/LLouzada/preprocess-segmentation-nnunet/blob/master/projeto_final/TCC_L_Louzada-final.pdf)
- **Apresentação do Projeto**: [Slides - PDF](https://github.com/LLouzada/preprocess-segmentation-nnunet/blob/master/projeto_final/TCC%20-%20apresenta%C3%A7%C3%A3o%20-%20LLouzada.pdf)
- **Pôster Científico**: [Poster - PDF](https://github.com/LLouzada/preprocess-segmentation-nnunet/blob/master/projeto_final/Poster-Lucas_Louzada.pdf)

## Recursos e Referências

- **Repositório Original do nnU-Net**: [nnU-Net - MIC-DKFZ](https://github.com/MIC-DKFZ/nnUNet)
- **Fork Customizado Utilizado no Projeto**: [nnU-Net - Customizado](https://github.com/LLouzada/nnUNet)

## Licença

Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT).
