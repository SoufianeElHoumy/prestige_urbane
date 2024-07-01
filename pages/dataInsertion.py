from models import Post 

# Create a list of dictionaries, each representing a Post
posts_data = [
    {
        "item_id": 2,
        "item_name": "Black-Tshirt with space logo ",
        "item_size": "M",
        "item_color": "Black",  
        "item_gender": "Male", 
        "item_price": 19.99,
        "item_image_url": "https://images.pexels.com/photos/12922525/pexels-photo-12922525.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1",
        "active": True,
        "quantity": 10
    },
]

# Create Post instances from the data and save them to the database
for post_data in posts_data:
    post = Post(**post_data)
    post.save()