O labirinto do horror II

Na segunda etapa de sua escavação arqueológica em Creta, você decifra mais inscrições e descobre por que a civilização cretense foi desestabilizada e destruída, mesmo com Ariadne tendo salvo Teseu do Minotauro. Os labirintos das lendas eram descritos por MxN células e cada célula Cij podia se conectar com as células imediatamente acima, abaixo, à esquerda e à direita. Os cretenses já conheciam a numeração hexadecimal e codificavam as paredes de cada célula com um número de 4 bits, indicando se existiam ou não paredes para as células vizinhas. Os bits correspondiam às paredes nesta ordem: superior, direita, inferior e esquerda. Um exemplo é o labirinto da figura abaixo:

Neste exemplo a célula inferior esquerda (chamada de C61) é codificada por 0011, indicando que existem paredes abaixo e à esquerda. Da mesma forma, todas as outras células recebem um dos dezesseis códigos possíveis.

O problema dos cretenses é que eles tinham m, n e a descrição das MxN células do labirinto, mas muitas vezes existiam regiões do labirinto que eram inatingíveis a partir de outras regiões. Ou seja, poderia ser que Teseu estivesse em uma região fechada, Ariadne estivesse em outra e o Minotauro em uma terceira, e eles nunca se encontrariam. Dois exemplos seguem, mostrando as entradas de dados, onde temos labirintos divididos em regiões distintas e sem conexão:

Há um detalhe adicional: por algum motivo desconhecido, esses labirintos eram povoados por Anões, Bruxas, Cavaleiros, Duendes, Elfos e Feijões. As células com esses seres são indicadas com o valor hexa EM MAIÚSCULA.

Portanto, sua missão é receber vários arquivos descrevendo labirintos diferentes e informar:

Quantas regiões diferentes de células isoladas existem no labirinto; e

Considerando todas as regiões, qual é o tipo de ser que mais aparece numa dada região?

Para o labirinto acima à esquerda, existem três regiões isoladas e para o da direita existem quatro regiões. No labirinto da esquerda, o ser que mais aparece numa região é o Anão. Já no labirinto da direita, o que mais aparece numa região é o Elfo.

Você deve apresentar um relatório incluindo:
• A descrição do problema e como ele foi resolvido;
• Detalhes de algoritmos e pseudo-código adequado;
• Resultados dos casos de teste fornecidos;
• Análise e dados de desempenho do algoritmo;
• Conclusões.