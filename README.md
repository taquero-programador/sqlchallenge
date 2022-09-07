Dinner project
- [x] Use sqlalchemy for db
- [x] Test connect Python to DB
- [ ] Simple FastAPI
- [x] Test container connect to DB
- ***
- [ ] Run App(fastpi) in Docker for "production"
- ***
- ### Construir la imagen de Python con el Dockerfile
- Entrar al directorio donde esta el Dockerfile
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
