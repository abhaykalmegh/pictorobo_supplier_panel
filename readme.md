# Django Product Management Project

This is a simple Django project for managing product data. It allows you to create, list, and upload products using Django Rest Framework (DRF).

## Project Structure

The project consists of the following components:

- **Models**: 
  - `Product` model in the `models.py` file represents a product with fields such as `title`, `img` (an image of the product), `description`, and `created_at` (automatically generated timestamp).

- **Serializers**:
  - `ProductSerializer` in the `serializers.py` file is used for serializing `Product` objects into JSON format and deserializing JSON data into Python objects.

- **Views**:
  - `create_product` and `list_products` views in the `views.py` file are responsible for creating and listing products using DRF.
  - `product_upload` view renders an HTML form for uploading products.

- **URLs**:
  - URL patterns in the `urls.py` file define the routing for different views, allowing you to access the following endpoints:
    - `/products/create/` for creating a new product
    - `/products/` for listing all products
    - `/products/upload/` for uploading products using an HTML form









