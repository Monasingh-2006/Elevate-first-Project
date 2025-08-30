📊 Stock Analysis Dashboard

A web-based interactive dashboard built using Streamlit, yFinance, and Plotly to visualize and analyze historical stock data with moving averages and volume insights.

📌 Project Objective

The goal of this project is to create a user-friendly tool where users can:

Enter a stock symbol (like AAPL, TSLA, etc.)

Select a custom date range

View interactive stock price charts with short-term and long-term moving averages

Analyze trading volume trends

Gain insights into stock trends over time

🧰 Technologies Used
Tool	Description
Python	Core programming language
Streamlit	Web framework to build UI and host app
yFinance	To fetch real-time and historical stock data
Plotly	To create interactive visualizations
Pandas	Data manipulation and moving average calculation

⚙️ How It Works

User Input:

Stock ticker (e.g., AAPL)

Start and end dates

Short and long moving average durations

Processing:

Downloads historical stock data using yFinance

Calculates moving averages using Pandas

Plots interactive line charts with Plotly

Output:

📈 Price chart with moving averages

📊 Volume chart

Tooltips and zoom/pan support via Plotly

🛠️ 2. Install Required Libraries

Make sure you have Python installed (preferably 3.8+), then run:

pip install streamlit yfinance plotly pandas

▶️ 3. Run the Streamlit App
streamlit run "stock dashboard.py"


The app will open in your browser at:
http://localhost:8501

🧠 Features

✅ Clean and responsive layout
✅ User-controlled date range and moving averages
✅ Interactive Plotly charts
✅ Real-time data via yFinance
✅ Sidebar for easy parameter tweaking

💡 Real-Life Use Case

Just like a shopkeeper tracks sales over days and draws trends, this dashboard lets investors and traders:

Spot trends with moving averages

Detect momentum shifts

Analyze volume patterns during events (like earnings, news)

📁 Project Structure
stock-dashboard/
│
├── stock dashboard.py       # Main Streamlit app
├── README.md                # Project documentation
└── requirements.txt         # (Optional) for dependencies

 Li

This project is for academic and educational purposes only.
