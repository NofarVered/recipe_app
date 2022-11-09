# recipe_app

## Technologies

<img align="left" alt="Pyton" width="70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />

<img align="left" alt="Mysql" width="70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/mysql/mysql.png" />
<br />
<br />

## Screenshot

![Screenshot](homepage_pic.png)

## Endpoints

Request:

```
GET http://localhost:8000/search?search=cheese&dairy=false&gluten=true
```

Response:

```
{
"recipes":[
        {
        "title":"Crock Pot Chicken Baked Tacos",
        "thumbnail":"https://www.themealdb.com/images/media/meals/ypxvwv1505333929.jpg",
        "href":"https://www.youtube.com/watch?v=oqL0mLDBzS4",
        "ingredients":[
        "Chicken Breasts",
        "Vinaigrette Dressing",
        "Cumin",
        "Smoked Paprika",
        "Garlic",
        "Refried Beans",
        "Hard Taco Shells",
        "Shredded Mexican Cheese",
        "Grape Tomatoes",
        "Jalapeno",
        "Avocado",
        "Green Salsa",
        "Sour Cream",
        "Milk"
        ]
        },
        {
        "title":"Chicken Enchilada Casserole",
        "thumbnail":"https://www.themealdb.com/images/media/meals/qtuwxu1468233098.jpg",
        "href":"https://www.youtube.com/watch?v=EtVkwVKLc_M",
        "ingredients":[
        "Enchilada sauce",
        "shredded Monterey Jack cheese",
        "corn tortillas",
        "chicken breasts"
        ]
        }, ...
}

```

Request:

```
GET http://localhost:8000/search?search=eggs&dairy=true&gluten=false
```

Response:

```
{"recipes":
        [{"title":"Bread and Butter Pudding",
                "thumbnail":"https://www.themealdb.com/images/media/meals/xqwwpy1483908697.jpg",
                "href":"https://www.youtube.com/watch?v=Vz5W1-BmOE4",
                "ingredients":[
                        "butter",
                        "bread",
                        "sultanas",
                        "cinnamon",
                        "milk",
                        "double cream",
                        "eggs",
                        "sugar",
                        "nutmeg"]
        }]
}

```
