import os
import psycopg2

# Настройка базы данных
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db:5432/app_db")

# Папка с миграциями
MIGRATIONS_DIR = "./migrations"

def apply_migrations():
    # Подключаемся к базе данных
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Создаем таблицу для отслеживания выполненных миграций
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS migrations (
            id SERIAL PRIMARY KEY,
            filename VARCHAR(255) NOT NULL UNIQUE
        );
    """)
    conn.commit()

    # Получаем список уже выполненных миграций
    cursor.execute("SELECT filename FROM migrations;")
    applied_migrations = {row[0] for row in cursor.fetchall()}

    # Применяем миграции из папки
    for migration in sorted(os.listdir(MIGRATIONS_DIR)):
        if migration.endswith(".sql") and migration not in applied_migrations:
            print(f"Applying migration: {migration}")
            with open(os.path.join(MIGRATIONS_DIR, migration), "r") as file:
                sql = file.read()
                cursor.execute(sql)
                cursor.execute("INSERT INTO migrations (filename) VALUES (%s);", (migration,))
                conn.commit()

    # Закрываем соединение
    cursor.close()
    conn.close()
    print("Migrations applied successfully.")
