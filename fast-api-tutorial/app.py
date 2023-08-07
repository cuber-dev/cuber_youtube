# hi sir just explored fastapi and its very easy to learn and use
# below i made a simple api to do CRUD opearitons about products data
# BaseModel is equal to scheme in mongodb and
# Optional is equal to null in mongodb


from fastapi import FastAPI , Path
from pydantic import BaseModel
from typing import Optional



app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

products = {
    1: {
        "name": "bottle",
        "price": 50
    },
    2: {
        "name": "pen",
        "price": 10
    },
    3: {
        "name": "notebook",
        "price": 20
    },
    4: {
        "name": "eraser",
        "price": 5
    },
    5: {
        "name": "pencil",
        "price": 2
    },
    6: {
        "name": "backpack",
        "price": 100
    },
    7: {
        "name": "desk",
        "price": 250
    },
    8: {
        "name": "chair",
        "price": 80
    },
    9: {
        "name": "whiteboard",
        "price": 150
    },
    10: {
        "name": "bookshelf",
        "price": 180
    }
}


@app.get("/all-products")
def get_all_products():
    return products

@app.get("/product-name")
def get_products_name(n : str,p : int = None):
    for id, info in products.items():
        # for checking name 
        if type(info['name']) == str:
            if info['name'] == n:
                return info
        
        # for checking price
        if type(info['price']) == int:
            if info['price'] == p:
                return info
            
    return 'not found'


@app.get("/product-id/{id}")
def get_product_name(id: int):
    return products[id] if id in products else 'not found'


class Product(BaseModel):
    name : str
    price :  int

@app.post("/product/{id}")
def create_product(id: int, new_product: Product):
    if id in products:
        return 'already exists'
    
    products[id] = new_product
    return {
        "success": "added new product",
        "new_product": products[id]
    }



class Update(BaseModel):
    name : Optional[str] = None
    price :  Optional[int] = None

@app.put("/product/{id}")
def update_product(id: int, update_product: Update):
    if id not in products:
        return 'not found'
    for key , value in products.items():
        if key == id:
            if update_product.name != None:
                value['name'] = update_product.name
            if update_product.price != None:
                value['price'] = update_product.price
            products[id] = value
    

    return {
        "success": "updated product",
        "updated_product": products[id]
    }



@app.delete("/product/{id}")
def delete_product(id: int):
    if id not in products:
        return 'not found'
    deleted_product = products.pop(id)

    return {
        "success": "deleted product",
        "deleted-product": deleted_product
    }