from DB.connection import query

class ExampleRepository:
    def __init__(self):
        pass

    async def create_example(self, body: dict):
        create = "INSERT INTO examples (name, description) VALUES (:name, :description)"
        res = await query(create, body)
        created_id = res["inserted_id"]
        select = "SELECT * FROM examples WHERE id = :id"
        created = await query(select, {"id": created_id})
        return created
    

    async def get_all_examples(self):
        get_all = "SELECT * FROM examples"
        res = await query(get_all)
        return res
    
    
    async def get_example_by_id(self, id: int):
        get_by_id = "SELECT * FROM examples WHERE id = :id"
        res = await query(get_by_id)
        return res
    

    async def edit_example(self, id: int, body: dict):
        edit = "UPDATE examples SET name = :name, description = :description WHERE id = :id"
        new_body = {
            "id": id,
            **body   # unpack the body into params w id
        }
        res = await query(edit, new_body)
        return res


    async def delete_example(self, id: int):
        delete = "DELETE FROM examples WHERE id = :id"
        res = await query(delete, { "id": id })
        return "Succussful deletion" if res else "ID not found"


example_repo = ExampleRepository() # singleton pattern in python