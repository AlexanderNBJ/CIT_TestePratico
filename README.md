# CIT_TestePratico
Teste prático para aplicação para a vaga de Estágio em Desenvolvimento/TI na CIT. O teste consiste no desenvolvimento de um sistema CRUD associado a m banco da dados postgresql para organizar e catalogar pontos de escavação.

## Configuração Básica
### Instalação do PostgreSQL (Linux)
No terminal do Linux (Ubuntu), execute os seguintes comandos:
```
sudo apt install curl ca-certificates

sudo install -d /usr/share/postgresql-common/pgdg

sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc

sudo sh -c 'echo "deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt noble-pgdg main" > /etc/apt/sources.list.d/pgdg.list'

sudo apt update

sudo apt install postgresql
```
Para testar a instalação do PostgreSQL, execute o seguinte comando no terminal:
```
sudo systemctl status postgresql
```
Caso o campo ```Active``` esteja com ```inactive (dead)```, execute o seguinte comando no terminal:
```
sudo systemctl start postgresql
```
Aperte ```q``` para sair dessa tela. Em seguida, alteraremos a senha do supersusuário do banco de dados:
```
sudo su - postgres

psql

alter user postgres with password 'admin123';
```
### Instalação do PgAdmin
No terminal do Linux, execute os seguintes comandos:
```
curl -fsS https://www.pgadmin.org/static/packages_pgadmin_org.pub | sudo gpg --dearmor -o /usr/share/keyrings/packages-pgadmin-org.gpg

sudo sh -c 'echo "deb [signed-by=/usr/share/keyrings/packages-pgadmin-org.gpg] https://ftp.postgresql.org/pub/pgadmin/pgadmin4/apt/noble pgadmin4 main" > /etc/apt/sources.list.d/pgadmin4.list && apt update'

sudo apt install pgadmin4
```

### Configuração no PgAdmin4
Por se tratar de um banco de dados local, configuraremos o banco de dados em conformidade à configuração feita na instalação do PostgreSQL. Assim, ao acessar o PgAdmin4:
1. Clique com o botão direito em ```Servers```
2. A partir de ```Register```, clique em ```Server```
3. Em ```General```, o campo ```Name``` pode ser customizado. Por conveniência, escolhi **CIT - Alexander**
4. Em ```Connection```: coloque em ```Host name/adress``` o valor **localhost**; em ```Port```, o valor **5432**; em ```Username```, o valor **postgres**; e em ```Password```, o valor **admin123**
5. Clique em ```Save```
