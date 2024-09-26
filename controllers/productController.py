from flask import request, jsonify
from models.schemas.productSchema import product_schema, products_schema
from services import productService
from marshmallow import ValidationError
from utils.util import token_required

@token_required
def save():
    try:
        product_data = product_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    
    product_save = productService.save(product_data)
    return product_schema.jsonify(product_save), 201

@token_required
def getAll():
    try:
        products = productService.getAll()
        return products_schema.jsonify(products), 201
    except ValidationError as err:
        return jsonify(err.messages), 400    
    
@token_required
def find_all_pagination():
    page = request.args.get('page', 1 ,type=int)
    per_page = request.args.get('per_page', 10 ,type=int)
    return products_schema.jsonify(productService.find_all_pagination(page=page, per_page=per_page)), 200

@token_required
def getOne():
    try:
        product_data = productService.getOne(request.json)
        if product_data:
            return product_schema.jsonify(product_data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@token_required
def updateProduct():
    try:
        product_data = productService.updateProduct(request.json)
        if product_data:
            return product_schema.jsonify(product_data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400

@token_required
def deleteProduct():
    try:
        product_data = productService.deleteProduct(request.json)
        return product_schema.jsonify(product_data), 201
    except ValidationError as err:
        return jsonify(err.messages), 400