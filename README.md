# InvestmentAnalysisOfCompany

Financial analysts in pension funds, asset management firms, and investment advisory businesses spend a disproportionate amount of time on labor-intensive tasks such as gathering, reading, and summarizing annual reports, earnings calls, investor presentations, and industry data—often leading to inefficiencies, inconsistencies, and slower turnaround in investment decision-making. This manual-heavy workflow diverts valuable analyst capacity from strategic evaluation to repetitive & mundane data handling. Generative AI interventions can easily streamline these extraction, analysis and summarization activities. Such automation is especially valuable in research-driven businesses managing large investment universes, where speed, accuracy, and depth of analysis are critical to delivering superior returns and minimizing oversight risk.

Financial analysts perform comprehensive evaluations across the following dimensions to support investment decisions aligned with long-term growth, risk mitigation and portfolio stability.
1. **Business Fundamentals** – analyzing products, customers, revenue models, market position, and competitive moats.
2. **Financial Analysis** – assessing profitability, liquidity, leverage, efficiency, and valuation metrics using annual reports and filings.
3. **Peer Benchmarking** – comparing key performance indicators with industry peers to gauge relative standing.
4. **Sentiment & ESG Analysis** – evaluating market sentiment, reputational risk, and sustainability practices using news, social media, and ESG disclosures.

This application is a _lite_ version of the above process, focusing on some aspects of the Financial Analysis step. For a complete & thorough Financial analysis, data is normally sourced from multiple **trusted and publicly available data sources**, such as:
1. **SEC EDGAR Filings (USA Companies)**: 10-K and 10-Q reports are to review audited financial statements, management discussion, risk disclosures.
2. **Annual Reports & Financial Statements**: to review Balance sheet, P&L, cash flow, notes
3. **Yahoo Finance/Google Finance data**: Historical price data, key ratios, analyst estimates
4. **Third-Party Financial Data Aggregators**: such as Alpha Vantage, Financial Modeling Prep, Tiingo, and Finnhub for Cleaned financial ratios, earnings, income statements, balance sheets

In our application, we focus on analyzing historical financial ratios using data from Yahoo Finance only. This roughly covers step # 3 from the above list. We are taking this approach only because data is freely available and fairly reliable.

The Financial analysis will be powered by a single Agent, which will leverage several tools to calculate financial ratios (Financial ratios such as liquidity ratios, profitability ratios, efficiency ratios, valuation ratios, leverage ratios and performance and growth metrics) across a 5 year period. These ratios will then be analyzed by an LLM (Google Gemini Flash in our case, but you can use any LLM of your choice [with code modifications, of course!]). The LLM will combine it's observations for each set of financial ratios and then give an overall recommendation on the long-term investment potential of the stock.

## Technology Stack
1. Python (>= 3.12) 
2. Agno (Agentic AI Framework)
3. Gemini Flash 2.0/2.5 LLM 
4. yfinance library (to download stock data from Yahoo Finance!)
5. Streamlit for GUI front-end

## Technical Architecture

## Setting up the Python environment
1. Download the code to your local machine - let's assume you downloaded it to a folder `c:\InvestmentAnalysisOfCompany` (on Windows) or `~/InvestmentAnalysisOfCompany` (on a Mac/Linux machine). Let's refer to this folder as `$CODE_ROOT`.
2. Install `uv` on your machine - `uv` has been used to manage Python environments. See [this link](https://docs.astral.sh/uv/getting-started/installation/) for installation instructions.
3. Run the following commands from a shell in `$CODE_ROOT` [NOTE: `$CODE_ROOT>` in the code listing is the command prompt - don't type it!]
```bash
$CODE_ROOT> uv init --python 3.12  # initialize local environment 

$CODE_ROOT> uv venv   # create the folder for local env

$CODE_ROOT> source .venv/bin/activate # on Mac/Linux
OR 
$CODE_ROOT> .venv\bin\activate # on Mac/Linux

$CODE_ROOT> uv sync   # ins
```
**NOTE:** if `.venv/bin/activate` is not found, use `.venv/Scripts/activate`

## Running the application


## Unresolved issues
1. Financial ratios tables sometimes display duplicate titles

## Potential enhancements
For a more thorough analysis, following enhancements are recommended:
1. **Adding sentiment analysis**: analyse overall market sentiment for this stock/company from news feeds, social media comments etc.
2. **Adding peer-comparison**: compare performance of this company with top 3-4 peers in the same business category (such as IT Services, Defence, Manufacturing etc.)
3. Analysis of Financial Statements & management commentary

