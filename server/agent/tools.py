from db.connection import execute_sql, engine

def get_schema():
    inspector = inspect(engine)
    schema = {}

    for table in inspector.get_table_names():
        columns = inspector.get_columns(table)
        schema[table] = {
            col["name"]: str(col["type"]) for col in columns
        }
    return schema


def run_query(query: str):
    return execute_sql(query)
