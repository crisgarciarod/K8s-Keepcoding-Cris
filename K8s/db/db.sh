mysql --password=keepcoding2022 -u root <<EOS
CREATE DATABASE IF NOT EXISTS contadordb;
GRANT ALL ON contadordb.* TO 'mycontador';
FLUSH PRIVILEGES;
    
USE contadordb;

CREATE TABLE tabla_contador (
    contador int NOT NULL
);

INSERT INTO tabla_contador VALUES (0);
EOS