# store

## Local Setup

- Create virtual environment and install requirements:
```bash
python3 -m venv venv
pip install -r requirements.txt
```
- Migrate database changes and start the local server:
```bash
python3 manage.py migrate
python3 manage.py runserver
```
- You can try out using [this][0] postman collection, to try on local
  env, change collection variable `hostname` to `localhost:8000`
- CMS link: http://localhost:8000/admin (Test superuser: a@b.com:C94A4PkFmUZqSGE)

## Requirements
- [x] The API to run a promotion should be protected i.e. only a
  logged-in user should be allowed to access that API. Rest, all other
  APIs are public endpoints
- [x] All the code should be well-styled with proper namings. We pay a
  lot of attention to code-styling.
- [ ] Include unit tests
- [x] Use Git for version control, and host the project in a public
  Github repository. Share the Github link with us.
- [ ] Use Dependency Injection
- [x] Implement CICD using Jenkins/Azure DevOps/CircleCI or any other CICD service
- [x] Host the service in a Public Cloud (Eg AWS or Azure or similar).
- [x] Write the instructions on how to build and run the application
  in the readme file in the repository.

## Assumptions
   - Promotion means discount on the product price i.e. offer
   - Promotions are run by a store for any of the products it might have
   - A store can have multiple offers for the same product
   - A store belongs to a retailer and can have products from any brand
   - A user can have only one store, i.e. one to one mapping
   - Offer is create by the owner of the store

## Possible Improvements
   - Create a mixin for created_at and updated_at fields
   - Use decimal fields for prices (money) to avoid floating precision issue
   - Allow running promotions on categories, stores or brand level
   - Move to fully fledged DB server from sqlite3
   - Use email as username for User model schema
   - Use reable slug to filter product listing by retailer and store instead of ids
   - Use django-filter package for standard filtering on queryset
   - Allow offers to be run by brands or retailers as well
   - Move secret in settings to env, can be done using decouple package
   - Move staticfiles to CDN
   - Setup SSL certificate on custome domain (requires paid account on heroku)

## APIs
   - Path prefix: `/api/v1`
   - List all products: `GET /inventory/products?retailer=1&store=2&brand=1`
   - List stores for a product: `GET /inventory/products/<product_id>`
   - Add a promotion / offer: `POST /inventory/offers`
   - Singup: `POST /inventory/signup`
   - Login: `POST /auth/token`


[0]: ./store.postman_collection.json
