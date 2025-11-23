import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Set random seed for reproducibility
np.random.seed(42)

# 1. Generate Synthetic Data
n_samples = 100
# Features: Area (m2), Rooms, Age (years)
area = np.random.normal(100, 30, n_samples).clip(40, 250)
rooms = np.random.randint(1, 6, n_samples)
age = np.random.randint(0, 50, n_samples)

X = np.column_stack((area, rooms, age))

# True coefficients
# Price = 2000 * Area + 15000 * Rooms - 500 * Age + Base
true_coef = np.array([2000, 15000, -500])
base_price = 50000
noise = np.random.normal(0, 15000, n_samples)

y = X.dot(true_coef) + base_price + noise

# 2. Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)

print(f"Model R² Score: {r2:.4f}")
print(f"Coefficients: Area={model.coef_[0]:.2f}, Rooms={model.coef_[1]:.2f}, Age={model.coef_[2]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")

# 3. Visualization
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Actual vs Predicted
ax1.scatter(y_test, y_pred, color='#00ff88', alpha=0.7)
ax1.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
ax1.set_xlabel('Actual Price (€)')
ax1.set_ylabel('Predicted Price (€)')
ax1.set_title('Actual vs Predicted Prices')
ax1.grid(True, alpha=0.2)

# Plot 2: Feature vs Price (Area) - Partial dependence sort of view
# We plot Area vs Price and color by Rooms
scatter = ax2.scatter(area, y, c=rooms, cmap='viridis', alpha=0.8)
ax2.set_xlabel('Area (m²)')
ax2.set_ylabel('Price (€)')
ax2.set_title('House Price Distribution (Color: Rooms)')
plt.colorbar(scatter, ax=ax2, label='Number of Rooms')
ax2.grid(True, alpha=0.2)

plt.tight_layout()
plt.savefig('images/projects/linear_regression_demo.png', dpi=100, bbox_inches='tight')
print("Plot saved to images/projects/linear_regression_demo.png")
