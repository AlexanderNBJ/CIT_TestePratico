CREATE DATABASE sistema_escavacao_alexander;

\c sistema_escavacao_alexander;

CREATE TABLE TIPO_DE_PONTO(
	ID SERIAL PRIMARY KEY,
	DESCRICAO VARCHAR(100) NOT NULL
);

CREATE TABLE PESQUISADOR(
	ID SERIAL PRIMARY KEY,
	NOME_COMPLETO VARCHAR(100) NOT NULL,
	TELEFONE VARCHAR(11),
	EMAIL VARCHAR(50),
	ESPECIALIDADE VARCHAR(50)
);

CREATE TABLE PONTO_DE_ESCAVACAO(
    ID SERIAL PRIMARY KEY,
    TIPO_DE_PONTO_ID SERIAL REFERENCES TIPO_DE_PONTO(ID) ON DELETE CASCADE,
    PESQUISADOR_RESPONSAVEL_ID SERIAL REFERENCES PESQUISADOR(ID) ON DELETE CASCADE,
    SRID INTEGER NOT NULL DEFAULT 4326,
    LATITUDE DOUBLE PRECISION NOT NULL CHECK (LATITUDE BETWEEN -90 AND 90),
    LONGITUDE DOUBLE PRECISION NOT NULL CHECK (LONGITUDE BETWEEN -180 AND 180),
    ALTITUDE DOUBLE PRECISION NOT NULL,
    DATA_CATALOGACAO DATE NOT NULL DEFAULT CURRENT_DATE CHECK (DATA_CATALOGACAO <= CURRENT_DATE),
    DATA_DE_DESCOBERTA DATE,
    DESCRICAO VARCHAR(200)
    CHECK (
        DATA_DE_DESCOBERTA <= DATA_CATALOGACAO
        OR DATA_DE_DESCOBERTA IS NULL
    )
);

INSERT INTO TIPO_DE_PONTO (DESCRICAO) VALUES 
    ('Antiga cabana indígena'),
    ('Utensílio indígena'), 
    ('Artefato indígena'),
    ('Restos mortais'),
    ('Armas de caça'),
    ('Possível vestimenta');

INSERT INTO PESQUISADOR (NOME_COMPLETO, TELEFONE, EMAIL, ESPECIALIDADE) VALUES 
    ('Ana Carolina Santos', '11987654321', 'ana.santos@inteligenciaterritorial.org', 'Arqueologia indígena da Amazônia'),
    ('Bruno Oliveira Nogueira', '21912345678', 'bruno.oliveira@inteligenciaterritorial.org', 'Preservação de sítios arqueológicos amazônicos'),
    ('Carla Mendes da Silva', '31911223344', NULL, 'Catalogação de artefatos indígenas'),
    ('Diego Rocha Lima', NULL, 'diego.rocha@inteligenciaterritorial.org', 'Estudo de comunidades indígenas pré-coloniais'),
    ('Eduarda Lima Conceição', '41999887766', 'eduarda.lima@inteligenciaterritorial.org', NULL);

INSERT INTO PONTO_DE_ESCAVACAO (
    TIPO_DE_PONTO_ID, 
    PESQUISADOR_RESPONSAVEL_ID, 
    LATITUDE, 
    LONGITUDE, 
    ALTITUDE, 
    DATA_DE_DESCOBERTA, 
    DESCRICAO
)
VALUES
    (
        1,
        1,
        -3.4653,
        -62.2159,
        50.0,
        '2023-09-15',
        'Sítio arqueológico com cerâmicas indígenas. Localização próxima ao Rio Amazonas, com vestígios de habitações antigas.'
    ),
    (
        2,
        2,
        -4.2635,
        -69.9382,
        120.0,
        '2023-08-10',
        'Gruta com fósseis de animais pré-históricos. Área de difícil acesso, com potencial para novas descobertas.'
    ),
    (
        1,
        3,
        -2.6286,
        -60.2093,
        80.0,
        '2023-07-25',
        'Sítio com pinturas rupestres e artefatos de caça. Localização próxima a Manaus, em área de preservação ambiental.'
    ),
    (
        3,
        1,
        -3.1190,
        -60.0217,
        30.0,
        '2023-06-12',
        'Área urbana com vestígios de habitações indígenas. Descoberta durante obras de infraestrutura, com cerâmicas e ferramentas.'
    ),
    (
        2,
        4,
        -5.8119,
        -61.2978,
        200.0,
        '2023-05-05',
        'Gruta com ossadas humanas e artefatos de rituais. Localização em área de preservação ambiental, com pinturas simbólicas nas paredes.'
    ),
    (
        1,
        2,
        -2.4425,
        -66.0833,
        60.0,
        '2023-04-20',
        'Sítio com cerâmicas e ferramentas de pedra. Localização próxima a comunidades ribeirinhas, com indícios de atividades agrícolas antigas.'
    );