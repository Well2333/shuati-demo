from datetime import datetime,timezone

def get_utc_time():
    return datetime.strftime(datetime.now(timezone.utc), '%Y-%m-%d %H:%M:%S')

def sql_checker(sql:str):
    return sql.replace("'",'"')