Modular E-commerce Engine – Perfume Store
A robust, full-stack e-commerce solution built with Python (Flask), HTML5, and Bootstrap. This application features a modular architecture for managing product catalogs, persistent shopping carts, and automated order processing.

Key Features
Dynamic Product Catalog
Displays available inventory in a fully responsive, high-performance grid layout.

Individual product modules featuring pricing logic, visual assets, and integrated "Add to Cart" functionality.

Persistent Shopping Cart System
Advanced session-based cart management that persists throughout the user journey.

Real-time cart updates: individual item removal and dynamic subtotal/total calculations.

Dedicated /cart interface for comprehensive order review.

Order Processing & Checkout Pipeline
Streamlined checkout flow accessible via the /checkout route.

Secure data collection for customer logistics:

Full Name, Email, and Phone contact validation.

Geographical address mapping.

Multiple payment gateway support (Credit Card, Bank Transfer, Cash on Delivery).

Data Persistence: Automated order serialization into structured JSON format, stored securely in the data/orders directory.

Infrastructure & Containerization
Fully dockerized environment for consistent deployment across development and production stages.

Deployment Commands:

docker build -t ecommerce-engine .
docker run -p 5000:5000 -it ecommerce-engine