# -*- coding: utf-8 -*-
# try something like

#this is where you view all products in store
@auth.requires_login()
def view():
    userdict = {}
    users = db(db.auth_user).select()
    for x in users:
        userdict[x.id] = x.first_name + " " + x.last_name
    rows = db(db.products.product_availability=='Available').select(orderby=~db.products.id)
    return locals()

#post products to pizza store
@auth.requires_login()
def post():
    form = SQLFORM(db.products).process()
    return locals()

##this where i see all products posted by managemnt and update product details #if you did not upload a product yu will see nothing
@auth.requires_login()
def mypost():
    rows = db(db.products.created_by==session.auth.user.id).select(orderby=db.products.product_availability | ~db.products.id)
    return locals()

#this is where you update posted products #you find the update link in mypost view
def update():
    isValid = False
    row = db(db.products.id==request.args(0)).select()
    for x in row:
        if x.created_by==session.auth.user.id:
            isValid =True
    if isValid:
        record = db.products(request.args(0)) or redirect(URL('view'))
        form = SQLFORM(db.products, record)
        if form.process().accepted:
            response.flash = 'Record Updated'
        else:
            response.flash = 'Please Complete the form.'
    return locals()

'''''
def buy():
    myDict={}
    row = db(db.products.id==request.args(0)).select()
    for x in row:
        x.product_name = x.product_name
    zita_re_product = x.product_name
    qty = request.vars.qty
    zuva = str(request.now.year) + "-" + str(request.now.month) + "-" + str(request.now.day)
    productId =request.args(0)   #selects current product_id
    customer = session.auth.user.id   #goes to cust_id
    online_order = db.online_orders.insert(cust_id=customer, prod_id=productId, order_date=zuva, quantity=qty, description = zita_re_product )
    rows = db(db.online_orders.cust_id == session.auth.user.id).select(orderby=~db.online_orders.id)
    return locals()
'''
def cart():
    return dict(cart=session.cart)
''''
def buy():
    form =SQLFORM.factory(Field('transaction_id'))
    db.sale.insert(customer=auth.user.id,
                          product = db.product.product_name,
                          quantity = value,
                          price = db.product(key).current_price,
                          transaction_id=form.vars.transaction_id)
    session.cart.clear()
    session.flash = 'Thank you for your Order'
    redirect(URL('view'))
    return (cart=session.cart, form=form)
'''

def delete():
    db.online_orders.id==request.args(0)
    remove = db(db.online_orders.id).delete() or redirect(URL('view'))
    if remove:
        response.flash = 'Item deleted'
    else:
        reponse.flash ='Cart is Empty'
    return locals()

#this downloads the product picture to the user
def download():
    return response.download(request, db)
