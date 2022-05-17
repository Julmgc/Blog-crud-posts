## <font size="7">_Blog-crud-posts_</font>

​​### <font color="gree"> API, CRUD for movies, using MongoDB, factory pattern and MVC architecture </font> Saves a movie

## <font size="6">Base URL /api </font>

## <font size="6">Routes</font>

​
​

### <font color="gree"> POST </font> Saves the post

​

```json
/posts
```

<font color="caramel"> _Request_ </font>
​

```json
{
  "title": "Hello",
  "author": "Julia",
  "tags": [{ "name": "travel" }],
  "content": "First travel post"
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "author": "Julia",
  "content": "First travel post",
  "created_at": "Mon, 01 Nov 2021 21:16:33 GMT",
  "id": 18,
  "tags": [
    {
      "name": "travel"
    }
  ],
  "title": "Hello"
}
```

​

### <font color="green"> GET </font> Shows all posts

​

```json
/posts
```

​
<font color="yellow"> _Response_ </font>
​

```json
[
  {
    "author": "Lu",
    "content": "oi",
    "created_at": "Wed, 01 Sep 2021 23:39:44 GMT",
    "id": 10,
    "tags": ["oi", "olá"],
    "title": "Olá"
  },
  {
    "author": "Lu",
    "content": "CONTENT",
    "created_at": "Thu, 02 Sep 2021 07:32:35 GMT",
    "id": 11,
    "tags": ["oi", "olá"],
    "title": "Olá",
    "updated_at": "2021-09-02 07:49:46.000792"
  }
]
```

### <font color="purple"> GET </font> Returns a specific post

​

```json
/posts/<int:id>
```

<font color="yellow"> _Response_ </font>
​

```json
{
  "author": "Julia",
  "content": "Olá",
  "created_at": "Wed, 01 Sep 2021 19:15:32 GMT",
  "id": 8,
  "tags": ["oi", "olá"],
  "title": "Hallo",
  "updated_at": "2021-09-05 18:44:02.577900"
}
```

​

### <font color="orange"> PATCH </font> Updates a spefic post

​

```json
/posts/<int:id>
```

​
<font color="caramel"> Request </font>
​

```json
{
  "title": "travel post"
}
```

​
<font color="yellow"> _Response_ </font>
​

```json
{
  "author": "Julia",
  "content": "Olá",
  "created_at": "Wed, 01 Sep 2021 19:15:32 GMT",
  "id": 8,
  "tags": ["oi", "olá"],
  "title": "travel post",
  "updated_at": "2021-11-01 22:02:23.963695"
}
```

### <font color="red"> DELETE </font> Delete a specific post

​

```json
/posts/<int:id>
```

<font color="yellow"> _Response_ </font>
​

```json
NO CONTENT, 204
```

​
