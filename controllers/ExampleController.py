from fastapi import Request
from models.ExampleBody import ExampleBody
from utils.BaseController import BaseController
from services.ExampleService import example_service

class ExampleController(BaseController):
    def __init__(self):
        super().__init__("/examples")

        self.router.add_api_route("", self.create_example, methods=["POST"])
        self.router.add_api_route("", self.get_all_examples, methods=["GET"])
        self.router.add_api_route("/{id}", self.get_example_by_id, methods=["GET"])
        self.router.add_api_route("/{id}", self.edit_example, methods=["PUT"])
        self.router.add_api_route("/{id}", self.delete_example, methods=["DELETE"])


    async def create_example(self, body: ExampleBody):
        new_example = await example_service.create_example(body.dict())
        return { "data": new_example }
    

    async def get_all_examples(self):
        examples = await example_service.get_all_examples()
        return { "data": examples }
    

    async def get_example_by_id(self, id: int):
        example = await example_service.get_example_by_id(id)
        return { "data": example }
    

    async def edit_example(self, id: int, body: ExampleBody):
        example = await example_service.edit_example(id, body.dict())
        return { "data": example }
    

    async def delete_example(self, id: int):
        example = await example_service.delete_example(id)
        return { "data": example }
        
example_controller = ExampleController() # singleton pattern in python