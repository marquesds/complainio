## API Overview

Note: all requests needs an authorization header like `'Authorization: apikey=\"Someone.DmDTqQ.6z_xYvgyH5J4GZpbdiGity9WSlU\"'`

### Save Complain

**URL**: `/api/v1/complains`

**Method**: `POST`

**Body Example**:
```json
{
	"title": "Problema com app do banco",
	"description": "Tento abrir o app, mas não consigo.",
	"company": {
		"name": "Itaú"
	},
	"locale": {
		"city": "São Paulo",
		"state": "SP"
	}
}
```

**Output Example**:

```json
{
    "id": "5b7db277690f536383011e7f"
}
```

#### Success Response

**Code**: `201 CREATED`

#### Invalid Body Response

**Code**: `400 Bad Request`

**Output Example**:

```json
{
    "errors": {
        "title": [
            "Missing data for required field."
        ]
    }
}
```

### Get Complain By ID

**URL**: `/api/v1/complains/{complain_id}`

**Method**: `GET`

#### Success Response

**Code**: `200 OK`

**Output Example**:

```json
{
    "_id": "5b7db197690f535b7aea9983",
    "company": {
        "name": "Itaú"
    },
    "description": "Tento abrir o app, mas não consigo.",
    "locale": {
        "city": "São Paulo",
        "state": "SP"
    },
    "title": "Problema com app do banco"
}
```

#### Not Found Response

**Code**: `404 Not found`

### Get All Complains

**URL**: `/api/v1/complains`

**Method**: `GET`

#### Success Response

**Code**: `200 OK`

**Output Example**:

```json
[
	{
	    "_id": "5b7db197690f535b7aea9983",
	    "company": {
	        "name": "Itaú"
	    },
	    "description": "Tento abrir o app, mas não consigo.",
	    "locale": {
	        "city": "São Paulo",
	        "state": "SP"
	    },
	    "title": "Problema com app do banco"
	},
	...
]
```

### Update Complain

**URL**: `/api/v1/complains`

**Method**: `PUT`

**Body Example**:
```json
{
	"title": "Problema com app do banco",
	"description": "Tento abrir o app, mas não consigo.",
	"company": {
		"name": "Banco do Brasil"
	},
	"locale": {
		"city": "São Paulo",
		"state": "SP"
	}
}
```

#### Success Response

**Code**: `200 OK`

#### Invalid Body Response

**Code**: `400 Bad Request`

**Output Example**:

```json
{
    "errors": {
        "title": [
            "Missing data for required field."
        ]
    }
}
```

### Delete Complain

**URL**: `/api/v1/complains/{complain_id}`

**Method**: `DELETE`

#### Success Response

**Code**: `204 No content`

### Get Complain's Count Of All Cities

**URL**: `/api/v1/complains/count`

**Method**: `GET`

#### Success Response

**Code**: `200 OK`

**Output Example**:

```json
[
    {
        "São Paulo - SP": 5
    },
    {
        "Fortaleza - CE": 2
    }
]
```

### Get Complain's Count Of Specific Locale

**URL**: `/api/v1/complains/count`

**Method**: `POST`

**Body Example**:
```json
{
	"city": "São Paulo",
	"state": "SP"
}
```

#### Success Response

**Code**: `200 OK`

**Output Example**:

```json
{
        "São Paulo - SP": 3
    }
```
