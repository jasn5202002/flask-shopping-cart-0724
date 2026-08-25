from flask import Flask,request,render_template,session,redirect,url_for
app=Flask(__name__)

#session 一定要有secrect key
app.secret_key='abc123'

products =[
    {'id':1,
     'name':'巧克力',
     'price':100,
     'image':'c1.JPG'            
        },
    
    {'id':2,
     'name':'餅乾',
     'price':80,
     'image':'c2.JPG'            
        },
    
    {'id':3,
     'name':'糖果',
     'price':60,
     'image':'c3.JPG'            
        }       
            
    ]

@app.route("/")  
def home():
    
# 有人貼上這個網址 就執行下面的函數        
    return render_template(        
        'index4.html',products=products       
                
        )
@app.route("/add_cart/<int:product_id>")  
def add_cart(product_id):
    
    #如果購物車還沒存在，建立空的list
    if 'cart' not in session:
        session['cart']=[]
        
    cart=session['cart']  
    #加入產品的id
    cart.append(product_id)
    #更新購物車
    session['cart']=cart
    #更新網頁
    return redirect(url_for('home'))
    
@app.route("/cart")  
def cart():
    
    cart_ids=session.get('cart',[])
    #先設定購物車網頁為空
    cart_products=[]
    total=0 ####
    
    for product_id in cart_ids:
        for product in products:
            if product['id']==product_id:    #如果有賣這個物品再加
                cart_products.append((product))
                total=total+product['price']####
    
        
 
# 有人貼上這個網址 就執行下面的函數        
    return render_template(        
        'cart.html',cart_products=cart_products       
                
        )



#偵錯模式先不開
if __name__ == '__main__':
    app.run(debug=True)
