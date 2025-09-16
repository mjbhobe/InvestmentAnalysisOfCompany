# InvestmentAnalysisOfCompany
Automating the analysis of a company's performance using [Agno](https://docs.agno.com/introduction) based Agentic AI application. Agno is a high-performance runtime for multi-agent systems. It can be used to build, run and manage secure multi-agent systems in your cloud. Agno is similar to CrewAI (but not a drop-in replacement!)

**NOTE:** this is a _lite_ version of the investment analysis of a company, where the application makes a recommendation purely based on the financial performance of a company stock for the past 5 financial years. 

Normally the analysis is much more thorough and involves analysis such as peer-comparison, sentiment analysis, financial commentary analysis etc. Financial analysts spends hours to days manually analyzing data from various data sources and then preparing a formatted report for the decision makers to take a decision (or make a recommendation) on the long term investment potential of a company.

Such an application can be recommended to Investment Banks, Wealth Managers and Pension funds, where ISDA certified financial analysts run such kind of thorough analysis for internal consumption or based on a customer inquiry.

## Technology Stack
1. Python (>= 3.12) 
2. Agno (Agentic AI Framework)
3. Gemini Flash 2.0/2.5 LLM
4. yfinance (to download stock data from Yahoo Finance!)

## Technical Architecture

## Setting up the code

## Running the application

## Unresolved issues
1. Financial ratios tables sometimes display duplicate titles

## Potential enhancements
For a more thorough analysis, following enhancements are recommended:
1. **Adding sentiment analysis**: analyse overall market sentiment for this stock/company from news feeds, social media comments etc.
2. **Adding peer-comparison**: compare performance of this company with top 3-4 peers in the same business category (such as IT Services, Defence, Manufacturing etc.)
3. Analysis of Financial Statements & management commentary

