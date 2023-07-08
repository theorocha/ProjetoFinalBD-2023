--Tabela de estudantes

CREATE TABLE Estudantes (
  id INT PRIMARY KEY,
  nome VARCHAR(100),
  matricula VARCHAR(20),
  email VARCHAR(100),
  curso VARCHAR(100),
  senha VARCHAR(100)
);

--Tabela de departamentos
CREATE TABLE Departamentos (
  id INT PRIMARY KEY,
  nome VARCHAR(100)
);

----Tabela de professores, que se associa a um departamento.
CREATE TABLE Professores (
  id INT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100),
  departamento_id INT,
  FOREIGN KEY (departamento_id) REFERENCES Departamentos(id)
);

--Tabela de Disciplinas, que se atrela a um departamento.
CREATE TABLE Disciplinas (
  id INT PRIMARY KEY,
  nome VARCHAR(100),
  departamento_id INT,
  FOREIGN KEY (departamento_id) REFERENCES Departamentos(id)
);

--Tabela de Turmas, se relacionam com professor e de disciplina.
CREATE TABLE Turmas (
  id INT PRIMARY KEY,
  disciplina_id INT,
  professor_id INT,
  FOREIGN KEY (disciplina_id) REFERENCES Disciplinas(id),
  FOREIGN KEY (professor_id) REFERENCES Professores(id)
);

--Tabela de avaliações, que tem uma relação com o estudante que a realizou e com o alvo da avaliação(Turma)
--Um modelo que vale a pena explicitar é que a avaliação a um professor é feita através da avaliação da turma.
CREATE TABLE Avaliacoes (
  id INT PRIMARY KEY,
  estudante_id INT,
  turma_id INT,
  nota DECIMAL(4,2),
  comentario TEXT,
  FOREIGN KEY (estudante_id) REFERENCES Estudantes(id),
  FOREIGN KEY (turma_id) REFERENCES Turmas(id)
);

-- Tabela Denúncias, que tem a avaliação denunciada e o estudante que a denunciou.
CREATE TABLE Denuncias (
  id INT PRIMARY KEY,
  avaliacao_id INT,
  estudante_id INT,
  motivo TEXT,
  FOREIGN KEY (avaliacao_id) REFERENCES Avaliacoes(id),
  FOREIGN KEY (estudante_id) REFERENCES Estudantes(id)
);
