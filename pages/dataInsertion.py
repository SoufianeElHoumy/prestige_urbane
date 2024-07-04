from models import Post 

# Create a list of dictionaries, each representing a Post
posts_data = [
    {
        "item_name": "Jacket Korean Streetwear ",
        "item_size": "M",
        "item_color": "green",
        "item_gender": "Male", 
        "item_price": 19.99,
        "item_image_url": "https://i.pinimg.com/564x/b6/96/f6/b696f630c6559be4dc0c380c2e423bfe.jpg",
        "active": True,
        "quantity": 20
    },
    {
        "item_name": "Jacket Korean Streetwear Yellow",
        "item_size": "XL",
        "item_color": "Yellow",  
        "item_gender": "Male", 
        "item_price": 19.99,
        "item_image_url": "https://i.pinimg.com/564x/3e/19/10/3e19102a13e774b156ebdd84b6ae5d2a.jpg",
        "active": True,
        "quantity": 15
    },
    {
        "item_name": "Jacket Bomber Varsity",
        "item_size": "M",
        "item_color": "Black",  
        "item_gender": "Male", 
        "item_price": 14.99,
        "item_image_url": "https://i.pinimg.com/564x/09/1d/96/091d96e9481b0f1bde47f79c1fbe7a64.jpg",
        "active": True,
        "quantity": 10
    },
    {
        "item_name": "Jacket Thick Fleece",
        "item_size": "M",
        "item_color": "Black",  
        "item_gender": "Male", 
        "item_price": 16.99,
        "item_image_url": "https://i.pinimg.com/564x/9b/41/77/9b417750ac6829d98cd5231bd995887d.jpg",
        "active": True,
        "quantity": 18
    },
    {
        "item_name": "Jacket Warm Grain Fleece ",
        "item_size": "M",
        "item_color": "Blue",  
        "item_gender": "Male", 
        "item_price": 15.99,
        "item_image_url": "https://i.pinimg.com/564x/19/c3/71/19c37172c5ca497218a9d6f4db96f944.jpg",
        "active": True,
        "quantity": 10
    },
    {
        "item_name": "Jacket Drawstring Hooded",
        "item_size": "M",
        "item_color": "Black",  
        "item_gender": "Male", 
        "item_price": 20.99,
        "item_image_url": "https://i.pinimg.com/564x/38/e6/97/38e697d68407d430844b66ff58bebce4.jpg",
        "active": True,
        "quantity": 5
    },
    {
        "item_name": "Jacket Windbreaker ",
        "item_size": "S",
        "item_color": "Black",  
        "item_gender": "Male", 
        "item_price": 21.99,
        "item_image_url": "https://i.pinimg.com/564x/ec/67/0b/ec670b7262726d27d09ef70fd0b299a1.jpg",
        "active": True,
        "quantity": 25
    },
    
    
]

# Create Post instances from the data and save them to the database
for post_data in posts_data:
    post = Post(**post_data)
    post.save()