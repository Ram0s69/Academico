from django.shortcuts import render
from . models  import*

def cidade(request):
    cidade = {
         'cidade':Cidade.objects.all()
        }

    return render(request,'cidade/cidade.html',cidade)

def areasaber(request):
    areasaber = {
         'areasaber':AreasSaber.objects.all()
        }

    return render(request,'areasaber/areasaber.html',areasaber)

def avaliacoes(request):
    avaliacoes = {
         'avaliacoes':Avaliacoes.objects.all()
        }

    return render(request,'avaliacoes/avaliacoes.html',avaliacoes)

def cursos(request):
    cursos = {
         'cursos':Cursos.objects.all()
        }

    return render(request,'cursos/cursos.html',cursos)

def disciplinacur(request):
    disciplinacur = {
         'disciplinacur':DisciplinaCurso.objects.all()
        }

    return render(request,'disciplinacur/disciplinacur.html',disciplinacur)

def disciplina(request):
    disciplina = {
         'disciplina':Disciplinas.objects.all()
        }

    return render(request,'disciplina/disciplina.html',disciplina)

def frequencias(request):
    frequencias = {
         'frequencias':Frequencia.objects.all()
        }

    return render(request,'frequencias/frequencias.html',frequencias)

def instituicao(request):
    instituicao = {
         'instituicao':Instituicao.objects.all()
        }

    return render(request,'instituicao/instituicao.html',instituicao)

def matriculas(request):
    matriculas = {
         'matriculas':Matriculas.objects.all()
        }

    return render(request,'matriculas/matriculas.html',matriculas)

def ocorrencias(request):
    ocorrencias = {
         'ocorrencias':Ocorrencias.objects.all()
        }

    return render(request,'ocorrencias/ocorrencias.html',ocorrencias)

def ocupacao(request):
    ocupacao = {
         'ocupacao':Ocupacao.objects.all()
        }

    return render(request,'ocupacao/ocupacao.html',ocupacao)

def pessoas(request):
    pessoas = {
         'pessoas':Pessoas.objects.all()
        }

    return render(request,'pessoas/pessoas.html',pessoas)

def semestre(request):
    semestre = {
         'semestre':Semestres.objects.all()
        }

    return render(request,'semestre/semestre.html',semestre)

def tipoava(request):
    tipoava = {
         'tipoava':Tipos_Avaliacao.objects.all()
        }

    return render(request,'tipoava/tipoava.html',tipoava)

def turmas(request):
    turmas = {
         'turmas':Turmas.objects.all()
        }

    return render(request,'turmas/turmas.html',turmas)