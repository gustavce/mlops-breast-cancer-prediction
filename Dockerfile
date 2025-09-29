# Dockerfile para API Flask y modelo
FROM python:3.10-slim
WORKDIR /app
COPY app/ /app/
RUN pip install --no-cache-dir flask scikit-learn pandas joblib
# Entrenar el modelo durante el build
RUN python train_model.py
EXPOSE 5000
CMD ["python", "api.py"]
