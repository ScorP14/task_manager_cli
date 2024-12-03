from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_DIR = BASE_DIR / "database"
FILE_NAME_JSON_DB = "tasks_db.json"
PATH_JSON_DB = DB_DIR / FILE_NAME_JSON_DB

FORMAT_DATA = "%Y-%m-%d"
