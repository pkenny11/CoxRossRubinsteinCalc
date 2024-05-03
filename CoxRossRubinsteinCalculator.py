import tkinter as tk
from tkinter import ttk
import numpy as np

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
ttk.Label(frame, text="Initial Stock Price (S0):").grid(column=0, row=0)
ttk.Entry(frame, textvariable=S0_var).grid(column=1, row=0)  # Input for stock price

ttk.Label(frame, text="Strike Price (K):").grid(column=0, row=1)
ttk.Entry(frame, textvariable=K_var).grid(column=1, row=1)  # Input for strike price

ttk.Label(frame, text="Risk-Free Rate (r):").grid(column=0, row=2)
ttk.Entry(frame, textvariable=r_var).grid(column=1, row=2)  # Input for risk-free rate

ttk.Label(frame, text="Volatility (σ):").grid(column=0, row=3)
ttk.Entry(frame, textvariable=sigma_var).grid(column=1, row=3)  # Input for volatility

ttk.Label(frame, text="Time to Maturity (T):").grid(column=0, row=4)
ttk.Entry(frame, textvariable=T_var).grid(column=1, row=4)  # Input for time to maturity

ttk.Label(frame, text="Number of Steps (N):").grid(column=0, row=5)
ttk.Entry(frame, textvariable=N_var).grid(column=1, row=5)  # Input for number of steps

ttk.Label(frame, text="Option Type:").grid(column=0, row=6)
ttk.Combobox(frame, textvariable=option_type_var, values=['call', 'put']).grid(column=1, row=6)  # Dropdown for option type

# Function to handle calculation
def on_calculate():
    S0 = S0_var.get()  # Get current stock price from input
    K = K_var.get()  # Get strike price from input
    r = r_var.get()  # Get risk-free rate from input
    sigma = sigma_var.get()  # Get volatility from input
    T = T_var.get()  # Get time to maturity from input
    N = N_var.get()  # Get number of steps from input
    option_type = option_type_var.get()  # Get option type from input
    
    price = binomial_option_pricing(S0, K, r, sigma, T, N, option_type)  # Calculate the option price
    result_label.config(text=f"Option Price: {price:.2f}")  # Display the calculated price

calculate_button = ttk.Button(frame, text="Calculate", command=on_calculate)  # Button to initiate calculation
calculate_button.grid(column=1, row=7)

result_label = ttk.Label(frame, text="Option Price: ")  # Label to display results
result_label.grid(column=0, row=8, columnspan=2)

root.mainloop()  # Start the GUI event loop
