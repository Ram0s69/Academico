from django.db import models

# Create your models here.
class Cidade(models.Model):
    nome_cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    def __str__(self):
        return f"{self.nome_cidade}, {self.uf}"
    
class Ocupacao(models.Model):
    nome_ocupacao = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_ocupacao

class Pessoas(models.Model):
    nome = models.CharField(max_length=100)
    pai = models.CharField(max_length=100)
    mae = models.CharField(max_length=100)
    cpf = models.CharField(max_length=100)
    data_nasc = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    
class Instituicao(models.Model):
    nome_instituicao = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_instituicao
    
class AreasSaber(models.Model):
    nome_areas = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_areas
    
class Cursos(models.Model):
    nome_curso = models.CharField(max_length=100)
    carga_horaria_total =  models.CharField(max_length=100)
    duracao_meses = models.CharField(max_length=110)
    areas_saber = models.ForeignKey(AreasSaber, on_delete=models.CASCADE)
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_curso

class Semestres(models.Model):
    nome_periodo = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_periodo
    
class Disciplinas(models.Model):
    nome_diciplina = models.CharField(max_length=100)
    areas_saber = models.ForeignKey(AreasSaber, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome_diciplina

class Matriculas(models.Model):
    instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)
    curso = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    nome_pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)
    data_inicio = models.DateField()
    data_previsao_termino = models.DateField()

class Tipos_Avaliacao(models.Model):
    nome_avaliacao = models.CharField(max_length=100)
    def __str__(self):
        return self.nome_avaliacao

class Avaliacoes(models.Model):
    descricao= models.CharField(max_length=100)
    cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplinas = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    tipo_avaliacao = models.ForeignKey(Tipos_Avaliacao, on_delete=models.CASCADE)

class Frequencia(models.Model):
    cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplinas = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)    
    numero_faltas =  models.CharField(max_length=100)

class Turmas(models.Model):
    turno = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    nome_turma = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)    
    periodo_semestre =  models.CharField(max_length=100)

class Ocorrencias(models.Model):
    descricao= models.CharField(max_length=100)
    data = models.DateField()
    cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    disciplinas = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)
    nome_pessoa = models.ForeignKey(Pessoas, on_delete=models.CASCADE)

class DisciplinaCurso(models.Model):
    nome_disciplinacurso= models.CharField(max_length=100)
    carga_horaria = models.CharField(max_length=100)
    cursos = models.ForeignKey(Cursos, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Semestres, on_delete=models.CASCADE)