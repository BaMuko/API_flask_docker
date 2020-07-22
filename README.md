# Device Registrz Service

## Usage

All responses will have the form

```json
{
	"data": "Mixed ty holding the content of the response",
	"messege": "Description of what happened"
}
```

Subsequent response definitions will onlz detail the expected value of the `data field`



## List all devices 

**Definition**

`GET /devices`

**Response**

- `200 OK` on succcess

``` json
[
	{
		"identifier": "floor-lamp",
		"name": "Floor-lamp",
		"device-type": "switch",
		"controller-gateway": "12.1.68.0.2"
	}
]
```


## Registering a new device

**Definition**

`POST /devices`

**Arguments**

- `"identifier": string` a globally unique identifier for this device
- `"name": string` a friendly name for this device
- `"device-type": string` the type of the device as understood by the client
- `"controller-gateway": string` the IP address of the devices's controller

**Response**

- `201 Created` on success

```json
	{
		"identifier": "floor-lamp",
		"name": "Floor-lamp",
		"device-type": "switch",
		"controller-gateway": "12.1.68.0.2"
	}
```


## Lookup device

`GET /device/<identifier>`

**Response**

- `404 Not Found` if the device does not exist
- `200 OK` on success

``` json
[
	{
		"identifier": "floor-lamp",
		"name": "Floor-lamp",
		"device-type": "switch",
		"controller-gateway": "12.1.68.0.2"
	}
]
```


## Delete a device

**Definition**

`DELETE /devices/ <identifier>`

**Response**

- `404 Not Found` if the device does not exits
- `204 Not Content`