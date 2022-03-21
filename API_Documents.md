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
