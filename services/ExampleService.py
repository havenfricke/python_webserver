from models.Example import Example
from repositories.ExampleRepository import example_repo

class ExampleService:

    async def create_example(self, body: dict) -> Example:
        created = await example_repo.create_example(body)
        return Example(created['id'], created['name'], created['description'], created['created_at'])

    async def get_all_examples(self) -> list[Example]:
        examples = await example_repo.get_all_examples()
        return [Example(prop['id'], prop['name'], prop['description'], prop['created_at']) for prop in examples]

    async def get_example_by_id(self, id: int) -> Example:
        example = await example_repo.get_example_by_id(id)

        if not example:
            raise ValueError("404: Example not found")
        return Example(example['id'], example['name'], example['description'], example['created_at'])

    async def edit_example(self, id: int, update: dict) -> Example:
        original = await example_repo.get_example_by_id(id)

        if not original:
            raise ValueError("404: Example not found")
        updated = {
        "name": original['name'] if update.get("name") == original['name'] else update.get("name"),
        "description": original['description'] if update.get("description") == original['description'] else update.get("description")
        # Other props here if model allows
        }

        updated = await example_repo.edit_example(original['id'], updated)
        return Example(updated['id'], updated['name'], updated['description'], updated['created_at'])

    async def delete_example(self, id: int) -> dict:
        example = await example_repo.get_example_by_id(id)

        if not example:
            raise ValueError("404: Example not found")
        message = await example_repo.delete_example(id)
        return message


example_service = ExampleService() # singleton pattern in python
