import tkinter as tk
from tkinter import ttk
import numpy as np

# Function to calculate option price
def binomial_option_pricing(S0, K, r, sigma, T, N, option_type):
    dt = T / N  # Time delta per step
    u = np.exp(sigma * np.sqrt(dt))  # Upward movement factor
    d = 1 / u  # Downward movement factor
    p = (np.exp(r * dt) - d) / (u - d)  # Risk-neutral probability

    stock_prices = np.zeros((N+1, N+1))  # Initialize the stock price tree
    for i in range(N+1):
        for j in range(i+1):
            stock_prices[j, i] = S0 * (u ** (i - j)) * (d ** j)  # Calculate stock prices for each node

    option_values = np.zeros((N+1, N+1))  # Initialize the option values at expiration
    if option_type == 'call':
        option_values[:, N] = np.maximum(stock_prices[:, N] - K, 0)  # Call option payoff
    else:
        option_values[:, N] = np.maximum(K - stock_prices[:, N], 0)  # Put option payoff

    # Calculate option price at earlier nodes
    for i in range(N-1, -1, -1):
        for j in range(i+1):
            option_values[j, i] = (p * option_values[j, i+1] + (1 - p) * option_values[j+1, i+1]) * np.exp(-r * dt)

    return option_values[0, 0]

# Create the main window
root = tk.Tk()
root.title("Binomial Option Pricing Calculator")  # Set window title

# Add a frame for input fields
frame = ttk.Frame(root, padding=10)
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Variables for inputs
S0_var = tk.DoubleVar()
K_var = tk.DoubleVar()
r_var = tk.DoubleVar()
sigma_var = tk.DoubleVar()
T_var = tk.DoubleVar()
N_var = tk.IntVar()
option_type_var = tk.StringVar(value='call')

# Setup input fields
labels = ["Initial Stock Price (S0):", "Strike Price (K):", "Risk-Free Rate (r):", "Volatility (σ):", "Time to Maturity (T):", "Number of Steps (N):", "Option Type:"]
variables = [S0_var, K_var, r_var, sigma_var, T_var, N_var]

for i, label_text in enumerate(labels):
    ttk.Label(frame, text=label_text).grid(column=0, row=i)
    if i == len(labels) - 1:
        ttk.Combobox(frame, textvariable=option_type_var, values=['call', 'put']).grid(column=1, row=i)  # Dropdown for option type
    else:
        ttk.Entry(frame, textvariable=variables[i]).grid(column=1, row=i)  # Input fields

# Function to handle calculation
def on_calculate():
    params = [var.get() for var in variables]  # Get input values
    option_type = option_type_var.get()  # Get option type from input
    
    price = binomial_option_pricing(*params, option_type)  # Calculate the option price
    result_label.config(text=f"Option Price: {price:.2f}")  # Display the calculated price

calculate_button = ttk.Button(frame, text="Calculate", command=on_calculate)  # Button to initiate calculation
calculate_button.grid(column=1, row=len(labels))

result_label = ttk.Label(frame, text="Option Price: ")  # Label to display results
result_label.grid(column=0, row=len(labels)+1, columnspan=2)

root.mainloop()  # Start the GUI event loop
