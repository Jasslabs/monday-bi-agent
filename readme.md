# Monday.com Business Intelligence AI Agent

Production-ready AI agent that answers founder-level business intelligence questions using **live Monday.com API calls**, built with:

- FastAPI
- HuggingFaceTB/SmolLM2-360M-Instruct
- GraphQL (Monday API)
- Real-time data normalization
- Visible tool-call traces

---

## Overview

Founders often ask:

- "How is our pipeline looking for the energy sector this quarter?"
- "What is total projected revenue this month?"
- "Which sector is underperforming?"
- "How many work orders are overdue?"

This agent:

1. Interprets natural language queries
2. Makes live Monday.com API calls (no caching)
3. Cleans messy board data
4. Performs cross-board BI analysis
5. Returns conversational insights
6. Shows visible API/tool-call traces

---

## 🏗 Architecture

User → FastAPI → SmolLM2 → Tool Decision → Monday GraphQL API → Data Cleaning → BI Engine → Natural Language Answer

Key principles:

- Live API calls only
- No preloaded data
- Handles messy/inconsistent formats
- Graceful error handling
- Transparent tool execution

---

## 📂 Project Structure
