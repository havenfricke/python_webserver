class Example:
    def __init__(self, id: int, name: str, desc: str, created_at: str):
        self.id = id
        # self.creator_id = creator_id Add this when auth is integrated
        self.name = name
        self.desc = desc
        self.created_at = created_at