print("-" * 50)
print("Controle Acadêmico")
print()
print("1 - Cadastrar aluno\n \n2 - Cadastrar disciplinas\n \n3 - Cadastrar notas em disciplina\n \n4 - Remover aluno\n \n5 - Remover disciplina\n \n6 - Remover nota de disciplina\n \n7 - Atualizar dados do aluno\n \n8 - Atualizar disciplina de aluno\n \n9 - Atualizar nota de disciplina\n \n10 - Visualize a média de um aluno\n \n11 - Visualize quais alunos estão com a média menor que 7\n \n12 - Visualize quais alunos estão com média maior ou igual a 7\n \n13 - Visualize as notas das disciplinas cadastradas em um aluno\n \n")
print()
print("-" * 50)


#celula *buscaR (int qnt, int x, celula *ini)
#{
#   if (ini->prox == NULL) 
#      return NULL;
#   p = ini->prox;
#   int count = 0;
#   while (p != NULL && p->conteudo != x) {
#        p = p->prox;
#        if(count++ == qnt/2){
#            if (p->prox->conteudo == x) 
#              return p->prox;
#            else{
#                if(p->prox->conteudo > x){
#                    return buscaR (qnt/2, x, p->prox);      
#                }else{
#                    return buscaR (qnt/2, x, ini->prox);
#                }
#            }
#        }
#   }
#}