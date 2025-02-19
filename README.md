# Text_Sum_DataBricks

Project Overview

This project implements an end-to-end AI and data solution for Rival Insurance Technology. The goal is to ingest unstructured text data, apply structured processing using Databricks, and generate AI-powered summaries using Azure OpenAI. Finally, an API is built to serve the summarized data.

Architecture Overview

This project follows Medallion Architecture (Bronze → Silver → Gold) to ensure structured and scalable data transformation.

Bronze Layer → Stores raw, unstructured text data as-is.
Silver Layer → Cleans and preprocesses the data (removes duplicates, standardizes format).
Gold Layer → Finalizes data for AI summarization and analytics.


AI-Powered Summarization:
Use Azure OpenAI to generate concise, structured summaries. Summarization logic optimizes token usage for cost efficiency.

API for Retrieving Summaries:
Serve summarized data via an API using Azure Functions and deploy API using Azure Functions

following command cna be used for testing 
curl -X POST "http://localhost:7071/api/summarize" \
     -H "Content-Type: application/json" \
     -d '{"text": "Customer had an accident and filed a claim."}

Design Decisions & Justifications

Batch Processing for Large Datasets
Processing all text in one request is costly and slow. Batch processing can optimize performance when implemented.
Also, considering that I used student subscription, I had to use put some limit on LLM tokens, etc



Potential Future Improvements & Optimizations

Improve AI Summarization Quality
Fine-tune GPT prompts for better insurance-specific summaries.
Use GPT-4-Turbo to reduce cost per token.
Optimize Costs & Token Usage
Implement shorter prompt engineering to reduce OpenAI API costs.
Use semantic similarity filtering to avoid redundant API calls.
Implement Caching for Faster API Responses
Store summaries in Redis or Azure Cache to reduce duplicate API calls.
Automate Pipeline with Azure Data Factory
Use Azure Data Factory (ADF) to schedule and orchestrate pipeline tasks.
Implement Sentiment Analysis
Enhance insights by analyzing positive vs. negative sentiment in claims.
Deploy to Kubernetes for Scaling
Use Azure Kubernetes Service (AKS) to dynamically scale API traffic.
