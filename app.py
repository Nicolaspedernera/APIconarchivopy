from flask import Flask, jsonify, request

app = Flask(__name__)
from products import products

@app.route("/products", methods=["GET"])
def getproducts():
    return jsonify({"products": products , "message": "ProductsList"})


@app.route("/products/<string:product_name>",methods=["GET"])
def getproduct(product_name):
    productfound=[product for product in products if product["name"]== product_name]
    if (len(productfound)>0):
        return jsonify({"product":productfound[0]})
   
    return jsonify({"message":"product not found"})

@app.route("/products", methods=["POST"])
def addProduct():
    new_product= {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message":"Product Added Succesfully", "products": products})

@app.route("/products/<string:product_name>",methods=["PUT"])

def editProduct(product_name):
    productFound   = [product for product in products if product["name"]==product_name]
    if(len(productFound)>0):
       productFound[0]["name"]=request.json["name"]
       productFound[0]["price"]=request.json["price"]
       productFound[0]["quantity"]=request.json["quantity"]
       return jsonify({"message":"product edited" ,"product": productFound[0]})
    
    return jsonify({"message":"product not found"})

@app.route("/products/<string:product_name>",methods=["DELETE"])
def deleteProduct(product_name):
    productDelete=[product for product in products if product["name"]==product_name]
    if (len(productDelete)>0):
        products.remove(productDelete[0])
        return jsonify({"message":"product deleted" ,"product":products})
    return jsonify({"message":"product not found"})
if __name__ == "__main__":
    app.run(debug=True, port= 4000)
