# MLOps Breast Cancer Prediction API

## Descripción
Sistema completo para el despliegue automatizado de un modelo predictivo de cáncer de mama, expuesto como API REST con Flask, contenedorizado con Docker y automatizado con CI/CD.

## Estructura del proyecto
- `app/train_model.py`: Entrenamiento y guardado del modelo.
- `app/api.py`: API REST con Flask.
- `app/test_api.py`: Pruebas automáticas de la API.
- `app/test_data_examples.md`: Ejemplos de datos para pruebas.
- `requirements.txt`: Dependencias Python.
- `Dockerfile`: Imagen reproducible para despliegue.
- `.github/workflows/ci.yml`: Workflow de CI/CD.

## Entrenamiento del modelo
El modelo se entrena automáticamente al construir la imagen Docker. Utiliza el dataset breast cancer de `sklearn` y guarda el modelo en `model.joblib`.

## Uso local
1. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```
2. Entrena el modelo:
   ```bash
   python app/train_model.py
   ```
3. Ejecuta la API:
   ```bash
   python app/api.py
   ```

## Pruebas automáticas
Ejecuta los tests:
```bash
python app/test_api.py
```

## Ejemplo de endpoints
- **GET /**: Verifica el estado del servicio.
- **POST /predict**: Recibe un JSON con el campo `input` (lista de 30 valores) y retorna la predicción.

### Ejemplo de entrada válida
```json
{
  "input": [17.99,10.38,122.8,1001,0.1184,0.2776,0.3001,0.1471,0.2419,0.07871,
    1.095,0.9053,8.589,153.4,0.006399,0.04904,0.05373,0.01587,0.03003,0.006193,
    25.38,17.33,184.6,2019,0.1622,0.6656,0.7119,0.2654,0.4601,0.1189]
}
```

## Docker
Construye y ejecuta el contenedor:
```bash
docker build -t breast-cancer-api .
docker run -d -p 5000:5000 --name breast-cancer-api breast-cancer-api
```

## CI/CD
El workflow de GitHub Actions:
- Instala dependencias
- Ejecuta pruebas
- Construye la imagen Docker
- Guarda la imagen en `package/breast-cancer-api.tar`

## Notas
- El modelo se entrena automáticamente en el build de Docker.
- Ejemplos de datos para pruebas están en `app/test_data_examples.md`.
- Para push a DockerHub, configura los secretos y descomenta las líneas en el workflow.

## Autores
- Equipo MLOps - Fintech/Salud
