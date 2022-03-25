## Authors
**Request URL** 
- ` https://cmput404-project-t12.herokuapp.com/service/authors/ `
  
**Request Method**
- GET 



**Return Example**

``` 
{
  "type": "authors",
  "items": [
    {
      "id": "32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a",
      "host": "https://cmput404-project-t12.herokuapp.com/",
      "displayName": "zhijian1",
      "github": "https://github.com/Zhijian-Mei",
      "profileImage": "/mysite/img/default_mSfB41u.jpeg"
    },
    {
      "id": "813c85e3-9c90-4f3e-a626-bf311cacc1a9",
      "host": "https://cmput404-project-t12.herokuapp.com/",
      "displayName": "zhijian2",
      "github": "https://github.com/Zhijian-Mei",
      "profileImage": "/mysite/img/Personnel_image_AAA_JC74bwD.jpg"
    },
    {
      "id": "bd7da150-2924-4f21-a293-028676a5c3cf",
      "host": "http://127.0.0.1:8000/",
      "displayName": "kaixuan",
      "github": "www.github.com",
      "profileImage": "/mysite/img/Personnel_image_AAA_8Yc9K7m.jpg"
    },
    {
      "id": "5e8c6055-5ed1-404d-ac26-9ca6d34714d0",
      "host": "https://cmput404-project-t12.herokuapp.com/",
      "displayName": "group13",
      "github": "group13_github",
      "profileImage": "/mysite/img/2.jpg"
    },
    {
      "id": "651d73ff-cae5-47e5-9a4f-c18e45bfc766",
      "host": "https://cmput404-project-t12.herokuapp.com/",
      "displayName": "connector",
      "github": "connector.github",
      "profileImage": "/mysite/img/fire1.gif"
    },
    {
      "id": "7d112b15-80fc-4385-a3b1-480c4f0916ac",
      "host": "http://127.0.0.1:8000/",
      "displayName": "Lildonk",
      "github": "https://github.com/Lildonk",
      "profileImage": "/mysite/img/Screenshot_from_2022-02-11_13-50-41.png"
    }
  ]
}

```




## Author
**Request URL**
- ` https://cmput404-project-t12.herokuapp.com/service/authors/32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a `

**Request Method**
- GET



**Return Example**

```
{
  "id": "32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a",
  "host": "https://cmput404-project-t12.herokuapp.com/",
  "displayName": "zhijian1",
  "github": "https://github.com/Zhijian-Mei",
  "profileImage": "/mysite/img/default_mSfB41u.jpeg"
}

```

## Followers
**Request URL**
- ` https://cmput404-project-t12.herokuapp.com/service/authors/813c85e3-9c90-4f3e-a626-bf311cacc1a9/followers `

**Request Method**
- GET



**Return Example**

```
[
  {
    "id": "bd7da150-2924-4f21-a293-028676a5c3cf",
    "host": "http://127.0.0.1:8000/",
    "displayName": "kaixuan",
    "github": "www.github.com",
    "profileImage": "/mysite/img/Personnel_image_AAA_8Yc9K7m.jpg"
  }
]

```

## Posts
**Request URL**
- ` https://cmput404-project-t12.herokuapp.com/service/authors/32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a/posts `

**Request Method**
- GET



**Return Example**

```
[
  {
    "title": "zhijian1 post",
    "id": "dc08e5e2-038b-479b-b509-2a6d7b9298ad",
    "source": "https://cmput404-project-t12.herokuapp.com/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad",
    "origin": "https://cmput404-project-t12.herokuapp.com/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad",
    "description": "zhijian1 post",
    "contentType": "text",
    "content": "zhijian1 post",
    "author": "32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a",
    "categories": "undefined",
    "like_count": 2,
    "comments": "",
    "published": "2022-03-21T06:38:58.493540Z",
    "visibility": "PUBLIC",
    "unlisted": false
  }
]

```

## Post
**Request URL**
- ` https://cmput404-project-t12.herokuapp.com/service/authors/32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad `

**Request Method**
- GET



**Return Example**

```
{
  "title": "zhijian1 post",
  "id": "dc08e5e2-038b-479b-b509-2a6d7b9298ad",
  "source": "https://cmput404-project-t12.herokuapp.com/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad",
  "origin": "https://cmput404-project-t12.herokuapp.com/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad",
  "description": "zhijian1 post",
  "contentType": "text",
  "content": "zhijian1 post",
  "author": "32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a",
  "categories": "undefined",
  "like_count": 2,
  "comments": "",
  "published": "2022-03-21T06:38:58.493540Z",
  "visibility": "PUBLIC",
  "unlisted": false
}

```

## Likes
**Request URL**
- ` https://cmput404-project-t12.herokuapp.com/service/authors/32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad/likes `

**Request Method**
- GET


**Return Example**

```
[
  {
    "at_context": "content",
    "object": "https://cmput404-project-t12.herokuapp.com/service/authors/32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad",
    "summary": "zhijian1 likes zhijian1's post",
    "actor_id": "32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a",
    "author_id": "32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a"
  },
  {
    "at_context": "content",
    "object": "https://cmput404-project-t12.herokuapp.com/service/authors/32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad",
    "summary": "zhijian2 likes zhijian1's post",
    "actor_id": "813c85e3-9c90-4f3e-a626-bf311cacc1a9",
    "author_id": "32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a"
  },
  {
    "at_context": "content",
    "object": "https://cmput404-project-t12.herokuapp.com/service/authors/32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad",
    "summary": "kaixuan likes zhijian1's post",
    "actor_id": "bd7da150-2924-4f21-a293-028676a5c3cf",
    "author_id": "32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a"
  }
]

```

## Liked
**Request URL**
- ` https://cmput404-project-t12.herokuapp.com/service/authors/32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a/liked `

**Request Method**
- GET



**Return Example**

```
[
  {
    "at_context": "content",
    "object": "https://cmput404-project-t12.herokuapp.com/service/authors/32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad",
    "summary": "zhijian1 likes zhijian1's post",
    "actor_id": "32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a",
    "author_id": "32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a"
  }
]

```

## Post_List
**Request URL** 
- ` https://cmput404-project-t12.herokuapp.com/service/post/ `
  
**Request Method**
- GET 

**Notice**
- For contentType, we are restrict them to "text","markdown","image",and "imagesrc"
- if the contentType is text or markdown, the data will be saved into content field,
- if the contentType is image, the data will be saved into image field,
- if the contentType is imagesrc, the data will be saved into image_src field,

**Return Example**

``` 
[
  {
    "title": "zhijian1 post",
    "id": "dc08e5e2-038b-479b-b509-2a6d7b9298ad",
    "source": "https://cmput404-project-t12.herokuapp.com/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad",
    "origin": "https://cmput404-project-t12.herokuapp.com/posts/dc08e5e2-038b-479b-b509-2a6d7b9298ad",
    "description": "zhijian1 post",
    "contentType": "text",
    "content": "zhijian1 post",
    "image":null,
    "image_src":"",
    "author": "32d6cbd8-3a30-4a78-a4c4-c1d99e208f6a",
    "categories": "undefined",
    "like_count": 3,
    "comments": "",
    "published": "2022-03-21T22:44:16.876579Z",
    "visibility": "PUBLIC",
    "unlisted": false
  },
  {
    "title": "zhijian2 post",
    "id": "43ed971a-4f35-4fae-b161-a5a44f53aa2a",
    "source": "https://cmput404-project-t12.herokuapp.com/posts/43ed971a-4f35-4fae-b161-a5a44f53aa2a",
    "origin": "https://cmput404-project-t12.herokuapp.com/posts/43ed971a-4f35-4fae-b161-a5a44f53aa2a",
    "description": "zhijian2 post",
    "contentType": "text",
    "content": "zhijian2 post1",
    "image":null,
    "image_src":"",
    "author": "813c85e3-9c90-4f3e-a626-bf311cacc1a9",
    "categories": "undefined",
    "like_count": 2,
    "comments": "",
    "published": "2022-03-21T22:44:12.661304Z",
    "visibility": "PUBLIC",
    "unlisted": false
  }
]

```

