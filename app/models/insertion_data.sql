--estudantes:
INSERT INTO estudantes (nome, matricula, email, curso, senha, foto)
VALUES ('Theo Rocha', '190038489','theomarquesrx@gmail.com, 'Engenharia de computação', 'Theotheo2003@', null);

INSERT INTO estudantes (nome, matricula, email, curso, senha, foto)
VALUES ('Gabriel Rocha', '21000000', 'gabrielrx@gmail.com, 'Engenharia de computação', 'Biel2003@', null);
INSERT INTO estudantes (nome, matricula, email, curso, senha, foto)
VALUES ('admin', '00' ,'admin@admin', 'admin', 'admin00', null);


--departamentos:
INSERT INTO departamentos (nome)
VALUES ('Ciência da Computação');
INSERT INTO departamentos (nome)
VALUES ('Engenharia Elétrica');
INSERT INTO departamentos (nome)
VALUES ('Matemática');
INSERT INTO departamentos (nome)
VALUES ('Física');


--professores
INSERT INTO professores(nome, email, departamento_id, matricula)
VALUES ('Vinicius Ruela','vini@gmail.com' , 1 , '1600');
INSERT INTO professores(nome, email, departamento_id, matricula)
VALUES ('Pedro Garcia','pedro@gmail.com' , 1 , '1500');
INSERT INTO professores(nome, email, departamento_id, matricula)
VALUES ('Teófilo','teo@gmail.com' , 1 , '1700');

INSERT INTO professores(nome, email, departamento_id, matricula)
VALUES ('Humberto Abdalla','abdalla@gmail.com' , 2 , '200');
INSERT INTO professores(nome, email, departamento_id, matricula)
VALUES ('Daniel Café','cafe@gmail.com' , 3 , '201');

INSERT INTO professores(nome, email, departamento_id, matricula)
VALUES ('Paulo Cruz','cruz@gmail.com' , 3 , '300');
INSERT INTO professores(nome, email, departamento_id, matricula)
VALUES ('Andrea silva','silva@gmail.com' , 3 , '301');


INSERT INTO professores(nome, email, departamento_id, matricula)
VALUES ('André Machado','machado@gmail.com' , 4 , '400');
INSERT INTO professores(nome, email, departamento_id, matricula)
VALUES ('Helena Santos','santos@gmail.com' , 4 , '401');


-- disciplinas
INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Algoritmos e Programação de computadores', 1 );
INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Estrutura de Dados', 1 );
INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Banco de dados', 1 );
INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Programação competitiva', 1 );


INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Sinais e Sistemas', 2 );
INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Sistemas Microprocessados', 2 );  
INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Circuitos Elétricos', 2 );  

INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Cálculo 1', 3 );  
INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Cálculo 2', 3 );  
INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Cálculo 3', 3 );  

INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Física 1', 4 );  
INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Física 2', 4 );  
INSERT INTO disciplinas(nome,departamento_id)
VALUES ('Física 3', 4 );  

-- turmas
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (1,2);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (1,3);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (2,2);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (2,3);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (3,2);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (3,1);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (4,2);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (4,3);

INSERT INTO turmas(disciplina_id, professor_id)
VALUES (5,4);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (5,5);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (6,4);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (6,5);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (7,4);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (7,5);


INSERT INTO turmas(disciplina_id, professor_id)
VALUES (8,6);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (8,7);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (9,6);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (9,7);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (10,6);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (10,7);

INSERT INTO turmas(disciplina_id, professor_id)
VALUES (11,8);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (11,9);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (12,8);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (12,9);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (13,8);
INSERT INTO turmas(disciplina_id, professor_id)
VALUES (13,9);




--avaliações
INSERT INTO `trabalhobd`.`avaliacoes` (`estudante_id`, `turma_id`, `nota`, `comentario`) VALUES ('2', '1', '7', 'aula aceitavel');
INSERT INTO `trabalhobd`.`avaliacoes` (`estudante_id`, `turma_id`, `nota`, `comentario`) VALUES ('1', '1', '4', 'aula muito chata');
INSERT INTO `trabalhobd`.`avaliacoes` (`estudante_id`, `turma_id`, `nota`, `comentario`) VALUES ('1', '1', '10', 'Turma e professores muito bons');

--denúncias
INSERT INTO `trabalhobd`.`denuncias` (`avaliacao_id`, `estudante_id`, `motivo`) VALUES ('7', '2', 'ok');
INSERT INTO `trabalhobd`.`denuncias` (`avaliacao_id`, `estudante_id`, `motivo`) VALUES ('9', '3', 'legal');
INSERT INTO `trabalhobd`.`denuncias` (`avaliacao_id`, `estudante_id`, `motivo`) VALUES ('10', '4', 'chato');
