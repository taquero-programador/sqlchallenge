Dinner project
- [x] Use sqlalchemy for db.
- [x] Test connect Python to DB.
- [ ] Simple FastAPI.
- [x] Test container connect to DB.
- [ ] Solve "value is not a valid dict".
- [x] Add docker-compose file to create DB and build Dockerfile.
- ***
- [ ] Run App(fastpi) in Docker for "production"
- ***
Dentro del directorio app/ se debe crear un archivo .env, el cual debe de tener 3 parametos, ejem:
```.env
url_database=localhost:3306
user_db=user
pass_db=1234
```

### Construir los contenedores de Mariadb, Phpmyadmin y el Dockerfile.
Ir al directorio de trabajo.
```bash
cd sqlchallenge/dannys_dinner/
```
Construir el docker-compose.yml
```bash
docker-compose up -d --build
```
