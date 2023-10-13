# Projeto de TCC -  Lucas de A. Louzada - 2023

## Segmentação da Articulação Sacroilíaca em Imagens de Ressonância Magnética Utilizando a Rede Neural Convolucional nnU-Net

## Descrição do Projeto

- Este repositorio contém o código fonte do projeto de TCC do curso de Informática Biomédica da Universidade de São Paulo (USP) do aluno Lucas de A. Louzada. O projeto consiste na segmentação da articulação sacroilíaca em imagens de ressonância magnética utilizando a rede neural convolucional nnU-Net.

- Específicamente, o repositório faz todo o pré processamento das imagens e máscaras, juntamente com o aumento da base de dados através do uso da biblioteca albumentenations. Além disso, o repositório contém o código para análise dos resultados obtidos.

- O treinamento foi realizado em um Google Colab, utilizando-se do ambiente de execução com GPU. [Link para o notebook](https://github.com/LLouzada/tcc/blob/master/nnunet_tcc.ipynb)

- O código deste repositório esta otimizado para uso com a base de dados *HCFMRP_sacroiliitis_v1*, a qual foi
anteriormente estruturada e anonimizada para uso público, com aprovação do Comitê de Ética em Pesquisa do Hospital das Clínicas de Ribeirão Preto (CEP-HCRP), sob parecer número 1.951.052.

### Autor

- Lucas de A. Louzada - [LLouzada](https://github.com/LLouzada)

### Orientador

- Prof. Dr. Paulo Mazzoncini de Azevedo Marques

### Links

- Repositório original do nnU-NET: [nnU-Net](https://github.com/MIC-DKFZ/nnUNet)

- Repositório fork do nnU-NET utilizado no projeto: [nnU-Net](https://github.com/LLouzada/nnUNet)

### Licença

- Este projeto está sob a licença [MIT](https://opensource.org/licenses/MIT)
