# Используем легковесный Python-образ
FROM python:3.11-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
COPY requirements.txt .

# накатываем зависимости БЕЗ КЭША!
RUN pip install --no-cache-dir -r requirements.txt && \
    rm -rf /root/.cache/pip


# Копируем код приложения
COPY ./app ./app
COPY .env .env
COPY ./migrations ./migrations
# Открываем порт
#EXPOSE 8000

# Указываем ENTRYPOINT для запуска приложения
ENTRYPOINT ["uvicorn", "app.main:app"]

# Указываем параметры запуска (параметры можно переопределить через docker run)
CMD ["--host", "0.0.0.0", "--port", "8000"]

RUN addgroup -S appgroup && adduser -S appuser -G appgroup
USER appuser



