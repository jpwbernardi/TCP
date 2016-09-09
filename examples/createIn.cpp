#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

//./a.out <nomeDoArquivo> <quantidadeDeLinhas>

#define MAX 50

char name[MAX][30] = {"Feijao", "Arroz", "Bala", "Pirulito", "Massa", "Agua sem gas", "Agua com gas", "Abacate", "Abóbora", "Açúcar mascavo", "Açúar", "Agrião", "Aguardente", "Aipo", "Alcachofra", "Alface", "Alho", "Almôndega", "Ameixa seca", "Ameixa", "Amêndoa", "Amendoim", "Atum", "Avelã", "Azeite", "Azeitona", "Bacalhau", "Bacon", "Banana", "Banha de porco", "Batata", "Batata doce", "Batata frita", "Fécula de Batata", "Refrigerante cola", "Refrigerante cola light", "Refrigerante de laranja", "Beringela", "Beterraba", "Biscoitos", "Bolacha água e sal", "Bolacha aveia", "Bolacha baunilha", "Bolacha chocolate", "Bolacha integral", "Bolacha manteiga", "Bolacha Maria", "Bolo de chocolate", "Bolo inglês", "Brócolis" };

void criaProd(char prod[100]) {
  strcpy(prod, name[rand() % MAX]);
  for (int i = 0; i < 2; i++)
    { strcat(prod, " de ");  strcat(prod, name[rand() % MAX]); }
}

int toNumber(char num[]) {
  int ret = 0;
  for (int i = 0; num[i] != '\0'; i++)
    { ret *= 10; ret += num[i] - '0'; }
  return ret;
}

int main(int argc, char *argv[]) {
  if (argc != 3) { printf("Foi passado o número errado(%d) de argumentos\n", argc); return 0; }
  srand((unsigned) time(NULL));

  int i, qtd = toNumber(argv[2]);
  FILE *f = fopen(argv[1], "w");
  if (f == NULL) { printf("Não foi possível criar o arquivo.\n"); return 0; }

  for (i = 0; i < qtd; i++) {
    char prod[100]; criaProd(prod);
    fprintf(f, "(%s, %d, %.2lf)\n", prod, 1 + rand() % 10,
            0.01 + rand() % 10 + (rand() % 100) / 100.);
  }
  fclose(f);
  return 0;
}
