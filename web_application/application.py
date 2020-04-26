from flask import Flask, render_template, request, jsonify

app = Flask("shreya")
food_items=[["Chicken", 20], ["Pizza", 30], ["meat", 50]]

@app.route("/a")
def getFoodItems():
    return render_template("webpage.html", food_items=food_items)

@app.route("/c")
def deleteItem():
    item_index=int(request.args.get('item_index'))
    del food_items[item_index-1]
    return "Item deleted at index :%s"  % item_index
    
app.run()
