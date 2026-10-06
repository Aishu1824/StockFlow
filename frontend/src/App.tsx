import { useState } from "react";
import "./App.css";
import { getProducts, type Product } from "./api/products";

function App() {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(false);

  const handleViewProducts = async () => {
    try {
      setLoading(true);

      const data = await getProducts();

      setProducts(data);
    } catch (error) {
      console.error("Failed to fetch products:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="navbar">
        <h1>StockFlow</h1>

        <nav>
          <a href="#">Products</a>
          <a href="#">Orders</a>
          <a href="#">Inventory</a>
        </nav>
      </header>

      <main className="hero">
        <h2>StockFlow</h2>

        <p>
          Intelligent Order & Inventory Management Platform
        </p>

        <button onClick={handleViewProducts}>
          {loading ? "Loading..." : "View Products"}
        </button>

        <div className="products">
          {products.map((product) => (
            <div className="product-card" key={product.id}>
              <h3>{product.name}</h3>

              <p>{product.description}</p>

              <p>₹{product.price}</p>

              <small>SKU: {product.sku}</small>
            </div>
          ))}
        </div>
      </main>
    </div>
  );
}

export default App;