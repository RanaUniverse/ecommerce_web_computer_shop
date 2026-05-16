
# 📦 Product System Design & Implementation Plan

This document describes how the product module should work in the ecommerce system and how it will evolve step by step.

---

## 🧠 Core Idea

The Product system is responsible for:
- Storing product information
- Managing product images
- Linking products with categories
- Allowing admin control (create/update/delete)
- Displaying products to users

---

# 🚀 1. Create New Product:- `/product/add`


### Flow:
- Only accessible to users with `admin / manager` role
- Display a form with:
  - Product name
  - Description
  - Category (datalist or select)
  - Price (MRP, sell price, purchase price)
  - Quantity
  - Images upload

### After Submission:
- Validate category exists
- Normalize product data
- Save product in `product_data`
- Save images in `product_image_data`
- Store image files in: `static/uploads/products/<product_id>/`

### Result:
- Redirect to product info page:


# 🚀 2. Editing Existing Product:- `/product/edit/<product_id>`

# 🍌 3. Deleting Existing Product:- `/product/delete/<product_id>1`

# 🍌 4. Show Product to Customers:- `/product/<product_id>`
