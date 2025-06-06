# OPTIONAL Wave 4: Enhancements

These really are **optional** - if you've gotten here and you have time left, that means you're moving speedy fast!

## More Inventory Management

### `GET /rentals/overdue`
List all customers with overdue videos

Fields to return:
- `video_id`
- `title`
- `customer_id`
- `name`
- `postal_code`
- `checkout_date`
- `due_date`

### `GET /customers/<id>/history`
List the videos a customer has checked out _in the past_. Current rentals should not be included.                                                                                  

URI parameters:
- `id`: Customer ID

Fields to return:
- `title`
- `checkout_date`
- `due_date`

###  `GET /videos/<id>/history`
List customers that have checked out a copy of the video _in the past_

URI parameters:
- `id`: Video identifier

Fields to return:
- `customer_id`
- `name`
- `postal_code`
- `checkout_date`
- `due_date`

## Enhancements

### More Query Parameters
The following 3 _optional_ query parameters:

| Name          | Value   | Description
|---------------|---------|------------
| `sort`        | string  | Sort objects by this field, in ascending order
| `count`       | integer | Number of responses to return per page
| `page_num`    | integer | Page of responses to return

should additionally be accepted by the following endpoints:
- `GET /video`
- `GET /customers/<id>/rentals`
- `GET /videos/<id>/rentals`
- `GET /customers/<id>/history`
- `GET /videos/<id>/history`

So, for an API endpoint like `GET /videos`, the following requests should be valid:
- `GET /videos`: All videos, sorted by ID
- `GET /videos?sort=name`: All videos, sorted by name
- `GET /videos?count=10&page_num=2`: Videos 11-20, sorted by ID
- `GET /videos?sort=name&count=10&page_num=2`: Videos 11-20, sorted by name

Add your own Wave 04 tests to verify functionality.

## CLI

Create a Command Line Interface (CLI) program as a client for the Retro Video Store API.
