# Options Pricing Calculator (Cox, Ross, Rubinstein)

## Introduction
For my Project, I've decided to create a "Options Pricing Calculator", which is based on the Binomial Options Pricing Model. It includes a convenient graphical interface for calculating the price of European options using the Cox-Ross-Rubinstein binomial tree model.

#### Options Background
In the contex of how they're used for this project, Options are a financial derivative that gives the "holder" the right to buy or sell an underlying asset (stock) at a predetermined price, by a specific predetermined date. For example, you can purchase a call option that would allow to buy a stock (currently priced at $100) for $105 (strike price) by a certain date. However, if that specified date arrives and the stock is not at or above the "strike" price, the options expires worthless and you dont' get any value in return.

#### Binomial Options Pricing Model
The Binomial Options Pricing Model important tool in the field of quantitative finance for valuing options. It provides flexiblity and an intuitive system for pricing a variety of options.

#### Why is it useful:
Being able to understand and accurately price options is critical for investors, traders and other financial professionals. This type of calculator can serve as a useful tool. By leveraging the power and flexibility of python with a powerful financial algorithm, people can use a tool like this to make more informed and accurate decisions.

## Data Struture
The calculator utilizes a binomial tree as its primary data structure. In the Cox-Ross-Rubinstein model, this tree represents different possible paths that the stock price might take over the option's "life". Each node on the tree represents a potential future price of the stock, derived from up and down movements calculated using the stock's volatility and the fixed time intervals to maturity. The tree is implemented as a two-dimensional array where each row represents a time step and each column represents a possible price at that time step. The final price of the option is determined by aggregating these possible outcomes, weighted by their probability of occuring.

## Input Instructions
#### Initial Stock Price (S0)
- **Description**: This is the current price of the stock.
- **Example Value**: If the stock is currently priced at $100, enter "100".

#### Strike Price (K)
- **Description**: This is the price at which the holder of the option can buy (call) or sell (put) the stock when the option expires.
- **Example Value**: If the option allows you to buy the stock at $100, enter "100".

#### Risk-Free Rate (r)
- **Description**: This is the annualized risk-free interest rate, compounded continuously. It represents the time value of money and is usually close to the yield of Treasury bonds.
- **Example Value**: If the current risk-free rate is 5%, enter "0.05".

#### Volatility (Sigma)
- **Description**: This is the annual volatility of the stock's returns, a measure of how drastically the stock price is expected to change. It is usually expressed as a decimal.
- **Example Value**: If the stock has a volatility of 20%, enter "0.20".

#### Time to Maturity (T)
- **Description**: This is the time from the current date to the expiration date of the option, expressed in years.
- **Example Value**: If the option expires in 6 months, enter "0.5", if the option expires in 2 years, enter "2". 

#### Number of Steps (N)
- **Description**: This is the number of steps in the binomial tree. More steps provide a more accurate but computationally intensive calculation.
- **Example Value**: To simulate the option price through 50 time steps, enter "50".

#### Option Type
- **Description**: This specifies whether the option is a call or a put. A call option gives the holder the right to buy the stock at the strike price, whereas a put option gives the holder the right to sell the stock at the strike price.
- **Example Values**: Enter "call" for a call option or `put` for a put option.

## Project Motivation and Challenges
I chose to implement the Cox-Ross-Rubinstein model because it aligns with my professional and educational background, as well as my interest in financial algorithms and their real-world applications. This project allowed me to deepen my understanding of binomial trees and their use in computational finance. One of the technical challenges was managing the computational complexity of the model as the number of steps increased. Optimizing the numpy array operations was a critical part of the program and a tremendous learning opportunity for me.

## Application step through (link to PowerPoint)

https://acrobat.adobe.com/id/urn:aaid:sc:VA6C2:65a345af-0d02-4e90-8430-74afc8b42854

## Instructions to Run the Program

#### Before Running
Ensure you have Python 3.8 or higher installed, as well as pip for managing Python packages. This application has been tested on Windows 10. Also, ensure that numpy is installed.

#### Installation
1. **Clone the Repository**: git clone https://github.com/pkenny11/CoxRossRubinsteinCalc.git

3. **Navigate to the Project Directory**: cd CoxRossRubinsteinCalc

4. **Launch the Program**: python CoxRossRubinsteinCalc.py
