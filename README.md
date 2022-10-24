## Dinner project
- [x] Use sqlalchemy for db.
- [x] Test connect Python to DB.
- [x] Simple FastAPI.
- [x] Test container connect to DB.
- [x] Add docker-compose file to create DB and build Dockerfile.
- [x] Testing CI/CD.
- [x] Run App(fastpi) in Docker for "production"
- [ ] Check error `value is not a dict`.
- [ ] Edit sales.
***
Dentro del directorio app/ se debe crear un archivo .env, el cual debe de tener 3 parametos, ejem:
```.env
URL_DATABASE=db:3306
USER_DB=user
PASS_DB=1234
```

### Construir el Dockerfile solo para FastAPI. se reduce el archivo compose
Ir al directorio de trabajo.
```bash
cd sqlchallenge/dannys_dinner/
```
Construir el docker-compose.yml
```bash
docker-compose up -d --build
```

### Last change
Elimine la opción de `network_mode: host`. Ahora ya sea que esten conectados a la misma red o compose creé una, se pueden ver y acceder por el nombre de servicio o container_name.

Elimine la opción `CMD` de Dockerfile para colocarlo en compose, tambien añadí `volumes` para que el flujo sea biderecciónal (no creá nuevo directorio en el host, utiliza el ya existente).
