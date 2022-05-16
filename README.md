### Setup database

```sh
docker compose up --build
```

### Clean

```sh
docker compose down
```

### Run optimization with Optuna PR 3327

```sh
docker compose run --rm optuna-300b bash
```

### Run optimization with Optuna PR 3564

```sh
docker compose run --rm optuna-300c bash
```

---

### Migration

```sh
# Create study
docker compose run --rm optuna-300b python src/init.py

# Run migration on RDB
docker compose run --rm optuna-300c bash src/upgrade.sh

# Resume study
docker compose run --rm optuna-300b python src/load.py
```
