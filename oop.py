class pessoa:
    def __init__(self):
	    self._nome = ""
	    self._rg = ""
	    self._cpf = ""
	    self._anoNasc = ""
	    self._mesNasc = ""
	    self._diaNasc = ""
	    self._sexo = ""

    def __new__(cls, *args, **kwargs):
        """previne a classe de ser instanciada diretamente"""
        if cls is pessoa:
            raise TypeError("classe não pode ser instanciada.")
        return object.__new__(cls, *args, **kwargs)
        
    def __str__(self):
        return f'{self._nome}; RG: {self._rg}'

class funcionario(pessoa):
    def __init__(self):
        self._matricula = ""
        self._setor = ""
        self._cargo = ""
        self._nivel = ""
    
    def cadastrar_funcionario(self):
        pass
    
    def exibir_funcionario(self):
        pass

    def exibir_funcionario_por_matricula(self, matricula):
        pass
class coordenador_adm(funcionario):
    def __init__(self):
        self.__area = ""
        self.__plusSalario = ""
    
    def cadastrar_coordenadoradm(self):
        pass
    
    def exibir_coordenadoradm(self):
        pass

    def exibir_coordenadoradm_por_matricula(self, matricula):
        pass

    def calcularPlusSalario(self):
        pass

class aluno(pessoa):
    def __init__(self):
        self._codigo = ""
        self._interesse = ""
        self._desconto = ""
        self.matricula = matricula

    def cadastrar_aluno(self):
        pass
    
    def exibir_alunos(self):
        pass

    def exibir_aluno_por_matricula(self, matricula):
        pass

class professor():
    def __init__(self):
        self.formacao = ""
        self.nivel = ""
        self.disciplina = ""
    
    def cadastrar_professor(self):
        pass
    def exibir_professores(self):
        pass

    def exibir_professor_por_matricula(self, matricula):
        pass

class coordenador_professor(professor):
    def __init__(self):
        self.__area = ""
        self.__plusSalario = ""
    
    def cadastrar_coordenadoraprofessor(self):
        pass
    
    def exibir_coordenadorprofessor(self):
        pass

    def exibir_coordenadorprofessor_por_matricula(self, matricula):
        pass

    def calcularPlusSalario(self):
        pass

class matricula:
    def __init__(self):
        self.id = id
        self.mesMatricula = ""
        self.anoMatricula = ""

    def matricular(self):
        #gera o id de matricula
        pass


class curso:
    def __init__(self):
        self.titulo = ""
        self.descricao = ""
        self.valor = ""
        self.sala = ""
        self.matricula = matricula
        self.professor = professor
    
    def cadastrar_curso(self):
        pass
    
    def exibir_cursos(self):
        pass

    def exibir_curso_por_matricula(self, matricula):
        pass
    
    def calcular_minimo_alunos(self):
        pass
    

    

