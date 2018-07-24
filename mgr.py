import mysql.connector


class ManagedMySqlContext:
    """
    Simple manager for MySQL context
    """

    def __init__(self, cfg):
        self.cfg = cfg
        self.ctx = None
    
    def __enter__(self):
        self.ctx = mysql.connector.connect(**self.cfg)
        return self.ctx

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.ctx:
            self.ctx.close()


class ManageMySqlCursor:
    def __init__(self, ctx):
        self.ctx = ctx
        self.cursor = None
    
    def __enter__(self):
        self.cursor = self.ctx.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
