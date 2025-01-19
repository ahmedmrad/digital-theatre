# verify_db.py
from sqlalchemy import inspect
from src.database import engine

def verify_database():
    inspector = inspect(engine)
    
    # Get all table names
    tables = inspector.get_table_names()
    print("\nTables in database:")
    print("------------------")
    for table in tables:
        print(f"\nTable: {table}")
        
        # Get columns for each table
        columns = inspector.get_columns(table)
        print("Columns:")
        for column in columns:
            print(f"  - {column['name']}: {column['type']}")
            
        # Get foreign keys
        foreign_keys = inspector.get_foreign_keys(table)
        if foreign_keys:
            print("Foreign Keys:")
            for fk in foreign_keys:
                print(f"  - {fk['constrained_columns']} -> {fk['referred_table']}.{fk['referred_columns']}")

if __name__ == "__main__":
    verify_database()