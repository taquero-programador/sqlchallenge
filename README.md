Dinner project
- [x] Use sqlalchemy for db
- [x] Test connect Python to DB
- [ ] Simple FastAPI
- [x] Test container connect to DB
- [ ] Solve "value is not a valid dict"
- [ ] Add Docker-compose to create DB and build Dockerfile
- ***
- [ ] Run App(fastpi) in Docker for "production"
- [ ] TEST
- ***
Dentro del directorio app/ se debe crear un archivo .env, el cual debe de tener 3 parametos, ejem:
```.env
url_database=0.0.0.0:3306
user_db=user
pass_db=1234
```

### Construir la imagen de Python con el Dockerfile
Entrar al directorio donde esta el Dockerfile
```bash
cd sqlchallenge/dannys_dinner/
```
Construir el Dockerfile
```bash
docker build -t api .
```
Inicar el contenedor usando la ip del host
```bash
docker run -d --network=host --name pyapi api
```
