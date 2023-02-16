from ypy_websocket.ystore import SQLiteYStore

class TmpYStore(SQLiteYStore):
    db_path = "/tmp/ystore.db"
