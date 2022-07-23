* store

** Assumptions:
   - Promotions can be run by either brands or retailers
   - A Store is owned by a retailer and can have products from any brand
   - Promotion means discount on the product price i.e. offer
   - A product has only one offer at a time

** Possible Improvements:
   - Create a mixin for created_at and updated_at fields
   - Use decimal fields for prices (money) to avoid floating precision issue
   - Allow running promotions on categories, stores or brand level
   - Move to fully fledged DB server from sqlite3
   - Use email as username for User model
