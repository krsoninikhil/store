* store

** Assumptions:
   - Promotions are run by a store for any of the products it might have
   - A store can have multiple offers for the same product
   - A Store is owned by a retailer and can have products from any brand
   - Promotion means discount on the product price i.e. offer
   - Offer can be run

** Possible Improvements:
   - Create a mixin for created_at and updated_at fields
   - Use decimal fields for prices (money) to avoid floating precision issue
   - Allow running promotions on categories, stores or brand level
   - Move to fully fledged DB server from sqlite3
   - Use email as username for User model
   - Use slug to filter product listing by retailer and store
   - Use django-filter package for standard filtering on queryset
   - Allow offers to be run by brands or retailers as well

** APIs
   - Path prefix: /api/v1
   - List all products: /products?retailer=1&store=2&brand=1
   - List stores for a product: /products/<product_id>
