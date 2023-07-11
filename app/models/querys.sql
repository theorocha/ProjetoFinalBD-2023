--Criação de um dado.
INSERT INTO Disciplinas (nome, departamento_id)
VALUES ('Nome da Disciplina', 1);

-- filtragem (todas as disciplinas de um departamento)
SELECT id, nome
FROM Disciplinas
WHERE departamento_id = 1;
