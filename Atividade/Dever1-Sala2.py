class Professor:
    def _init_(self, nome):
        self.nome = nome

    def ministrar_aula(self, assunto):
        return f"O professor {self.nome} está ministrando uma aula sobre {assunto}."


class Aluno:
    def _init_(self, nome):
        self.nome = nome

    def presenca(self):
        return f"O aluno {self.nome} está presente."


class Aula:
    def _init_(self, professor, assunto, alunos):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def listar_presenca(self):
        lista_presenca = [aluno.presenca() for aluno in self.alunos]
        return f"Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:\n" + "\n".join(lista_presenca)

# Example usage:

professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
aula = Aula(professor, "Programação Orientada a Objetos", [aluno1, aluno2])
print(aula.listar_presenca())
