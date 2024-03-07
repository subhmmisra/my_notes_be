#Notes

##Create Note
```
POST /api/v1/note/add
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Content-Type**  | application/json


__Request__
```json
{
    "title": "sampple",
    "description": "note description",
}
```

__Response__
```json
Status: 201 Created
{
    "created_at": "2024-03-07T12:05:19.652852Z",
    "updated_at": "2024-03-07T12:05:19.652989Z",
    "id": "63eb4ea7-e0f9-4625-b573-6f36c28a2094",
    "title": "sample note",
    "description": "asasdasnd"
}
```

##Update notes
```
PUT /api/v1/note/{{NOTE_ID}}
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Content-Type**  | application/json

__Request__
```json
{
    "title": "sampple",
    "description": "note description",
}
```

__Response__
```json
Status: 200 - Ok
{
    "created_at": "2024-03-07T12:05:19.652852Z",
    "updated_at": "2024-03-07T12:05:19.652989Z",
    "id": "63eb4ea7-e0f9-4625-b573-6f36c28a2094",
    "title": "sample note",
    "description": "asasdasnd"
}
```

## List Notes

```
GET /api/v1/note
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Content-Type**  | application/json


__Response__
```json
Status: 200 - Ok
{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "created_at": "2024-03-07T05:17:36.640434Z",
            "updated_at": "2024-03-07T05:17:36.640482Z",
            "id": "fa7e63d7-c9b6-4780-a50d-7105cc3b90de",
            "title": "aaa bbb ccc",
            "description": "asasdasnd"
        },
        {
            "created_at": "2024-03-07T05:15:49.217626Z",
            "updated_at": "2024-03-07T05:46:20.094936Z",
            "id": "9fe97502-734f-4b1d-a6be-b880e911793a",
            "title": "alpha beta",
            "description": "asasdasnd"
        },
        {
            "created_at": "2024-03-07T12:05:19.652852Z",
            "updated_at": "2024-03-07T12:05:19.652989Z",
            "id": "63eb4ea7-e0f9-4625-b573-6f36c28a2094",
            "title": "sample note",
            "description": "asasdasnd"
        }
    ]
}
```


## Fetch Notes

```
GET /api/v1/note/{{NOTE_ID}}
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Content-Type**  | application/json


__Response__
```json
Status: 200 - Ok
{
    "created_at": "2024-03-07T12:05:19.652852Z",
    "updated_at": "2024-03-07T12:05:19.652989Z",
    "id": "63eb4ea7-e0f9-4625-b573-6f36c28a2094",
    "title": "sample note",
    "description": "asasdasnd"
}
```

## Delete Notes

```
DELETE /api/v1/note/{{NOTE_ID}}
```

__HEADERS__

Key               | Value
------------------|---------------------------
**Content-Type**  | application/json


__Response__
```json
Status: 204 - No-Content
```