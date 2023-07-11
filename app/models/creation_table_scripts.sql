--Tabela de estudantes

CREATE TABLE Estudantes (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  matricula VARCHAR(20),
  email VARCHAR(100),
  curso VARCHAR(100),
  senha VARCHAR(100),
  foto BLOB
);


--Tabela de departamentos
CREATE TABLE Departamentos (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100)
);


----Tabela de professores, que se associa a um departamento.
CREATE TABLE Professores (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  email VARCHAR(100),
  departamento_id INTEGER UNSIGNED,
  matricula VARCHAR(100),
  FOREIGN KEY (departamento_id) REFERENCES Departamentos(id)
);



--Tabela de Disciplinas, que se atrela a um departamento.
CREATE TABLE Disciplinas (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(100),
  departamento_id INTEGER UNSIGNED,
  FOREIGN KEY (departamento_id) REFERENCES Departamentos(id)
);

--Tabela de Turmas, se relacionam com professor e de disciplina.
CREATE TABLE Turmas (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  disciplina_id INTEGER UNSIGNED,
  professor_id INTEGER UNSIGNED,
  FOREIGN KEY (disciplina_id) REFERENCES Disciplinas(id),
  FOREIGN KEY (professor_id) REFERENCES Professores(id)
);

--Tabela de avaliações, que tem uma relação com o estudante que a realizou e com o alvo da avaliação(Turma)
--Um modelo que vale a pena explicitar é que a avaliação a um professor é feita através da avaliação da turma.
CREATE TABLE Avaliacoes (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  estudante_id INTEGER UNSIGNED,
  turma_id INTEGER UNSIGNED,
  nota DECIMAL(4,2),
  comentario TEXT,
  FOREIGN KEY (estudante_id) REFERENCES Estudantes(id),
  FOREIGN KEY (turma_id) REFERENCES Turmas(id)
);

-- Tabela Denúncias, que tem a avaliação denunciada e o estudante que a denunciou.
CREATE TABLE Denuncias (
  id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  avaliacao_id INTEGER UNSIGNED,
  estudante_id INTEGER UNSIGNED,
  motivo TEXT,
  FOREIGN KEY (avaliacao_id) REFERENCES Avaliacoes(id),
  FOREIGN KEY (estudante_id) REFERENCES Estudantes(id)
);