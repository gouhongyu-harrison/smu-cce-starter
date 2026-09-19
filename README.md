## Installation Instructions

If you are new to Python, follow these steps in order.

1. Open the project in GitHub Codespaces or in your local VS Code terminal.
2. Go to the project folder:

   ```bash
   cd /workspaces/smu-cce-starter
   ```

3. Create a virtual environment so your packages stay organized:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Upgrade pip and install the required packages:

   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements.txt
   ```

5. Start Jupyter and open a notebook:

   ```bash
   jupyter notebook
   ```

6. In the browser, open one of the files in the `notebooks/` folder and run the cells. For example, the notebooks fetch stock data from Yahoo Finance and print the results in the terminal.

## Code Walkthrough

This repo is a beginner-friendly finance data project built around Jupyter notebooks.

- `notebooks/` contains the main examples:
  - `filings.ipynb` gets a company's latest financial statements using `yfinance.Ticker(...)`.
  - `news.ipynb` pulls recent headlines and summaries for a stock ticker.
  - `stock_price_ratings.ipynb` gets the current stock price and analyst recommendation history.

- `lessons/` contains the course instructions and guided exercises.
- `requirements.txt` lists the Python packages the project needs, such as `yfinance`, `pandas`, and `streamlit`.

The app works like this: you pick a stock ticker such as `MU` or `GOOG`, open a notebook, and run the code cell. The notebook uses Yahoo Finance to request live market data, then prints the results in a readable format. Each notebook focuses on a different type of financial information, so the project becomes a simple data pipeline for stock analysis.

 # Cloud Computing for Economics: Starter Repo 

  This repository contains the starter code and lesson materials for building a Python financial-data application and deploying it to AWS.

  Students will use GitHub Codespaces, Python, Jupyter notebooks, Streamlit, Git, and AWS CloudFormation.

  ## Learning outcomes

  By the end of the course, you will be able to:

   1.  Build and deploy an analytics application with a simple Front End / back-end (using AI)
   2.  Host and share the application on a cloud platform (e.g., AWS EC2 or similar) so that others can access it securely over the web
   3.  Integrate data sources and APIs into the app to enable interactive, real-time analytics
   4.  Apply cloud architecture best practices, ensuring the app demonstrates scalability, performance efficiency, and basic security
   5.  Showcase your work on GitHub as part of a personal portfolio, demonstrating practical cloud and analytics skills through a shareable, explorable repository

  
  ## Repository structure

  ```text
  .
  ├── lessons/          # Step-by-step course instructions
  ├── notebooks/        # Starter financial-data notebooks
  ├── requirements.txt  # Python dependencies
  └── README.md         # Course overview