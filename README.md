# 🏗️ BuildQuant

## VERIFICATION CODE:
WTC-XQYUTEJA

## Residential Quantity Estimation & Data Engineering System

BuildQuant is a Python-based educational prototype that combines **construction quantity estimation, data engineering, database storage, REST API integration, analytics, and PDF reporting** into one Streamlit application.

The project was designed around a practical construction/quantity-surveying use case: collecting proposed residential building information, transforming that information into preliminary quantities, retrieving material rates through a REST API, calculating estimated material costs, storing project data in SQLite, analysing historical projects, and generating a PDF report.

> **Important:** BuildQuant is an educational prototype. Its simplified calculations do not replace professional quantity surveying, formal Bills of Quantities (BoQs), professional cost estimating, or construction specifications.

---

## 📌 Project Overview

### Problem

Residential construction information can involve several separate steps:

- collecting project information
- calculating floor and wall areas
- accounting for openings
- allowing for material waste
- retrieving material rates
- calculating material costs
- storing project information
- comparing historical projects
- producing reports

BuildQuant brings these steps together into one small data-driven application.

### Goal

The goal of BuildQuant is to demonstrate how a construction-related workflow can be transformed into a simple **data engineering pipeline** using Python.

---

## ✨ Features

### 📋 Project Data Collection

Users can enter:

- Project name
- Project number
- Location
- Building type
- Length
- Width
- Wall height
- Number of doors
- Number of windows

### 📐 Quantity Calculations

BuildQuant calculates:

- Floor area
- Perimeter
- Gross wall area
- Door opening area
- Window opening area
- Net wall area
- Floor tile quantity including waste
- Paint area including allowance

### 💰 Cost Estimation

Material costs are calculated using:

```text
Quantity × Material Rate = Material Cost
```

The current prototype calculates:

- Floor tile cost
- Paint cost
- Total estimated cost

### 🔌 REST API Integration

BuildQuant retrieves material prices from a Flask REST API.

Example request:

```text
GET /materials/tiles
```

Example JSON response:

```json
{
    "material": "tiles",
    "unit": "m2",
    "rate": 350
}
```

The Streamlit application consumes this JSON data and uses the returned rate in its cost calculations.

### 💾 SQLite Database

Project information and calculated cost data are stored in SQLite.

The database stores:

- Project information
- Building dimensions
- Opening information
- Quantity calculations
- Material quantities
- Material rates
- Individual material costs
- Total estimated cost

### 📊 Dashboard

The dashboard provides:

- Total projects
- Average floor area
- Average wall area
- Building type count
- Current project estimate
- Floor-area charts
- Wall-area charts
- Saved project table
- Data pipeline overview

### 📈 Analytics

Historical project data can be analysed using:

- Total project count
- Average floor area
- Average project cost
- Total estimated project cost
- Largest project
- Project cost comparisons
- Floor area comparisons
- Material cost comparisons

### 📄 PDF Reports

Users can generate and download a PDF report containing:

- Project information
- Quantity summary
- Material quantities
- Cost estimates
- Educational prototype disclaimer

### ✅ Input Validation

The application validates important inputs before performing calculations.

Examples:

- Project name cannot be empty
- Project number cannot be empty
- Location cannot be empty
- Length must be greater than zero
- Width must be greater than zero
- Wall height must be greater than zero

### 🛡️ API Error Handling

The application handles common REST API problems, including:

- API unavailable
- Connection errors
- Request timeouts
- HTTP errors

The sidebar also provides an API status indicator.

---

# 🏛️ System Architecture


### Your architecture is now clearer

The project now has a nice separation of responsibilities:

```text
                    ┌─────────────────┐
                    │    app.py       │
                    │  Streamlit UI   │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              ↓              ↓              ↓
       ┌────────────┐ ┌─────────────┐ ┌─────────────┐
       │ validation │ │ calculations│ │  database   │
       └────────────┘ └──────┬──────┘ └─────────────┘
                             │
                             ↓
                      ┌─────────────┐
                      │ REST Client │
                      │ material_api│
                      └──────┬──────┘
                             │
                             ↓
                      ┌─────────────┐
                      │ Flask API   │
                      │ api/        │
                      └─────────────┘

                             ↓
                      ┌─────────────┐
                      │   reports   │
                      │ PDF output  │
                      └─────────────┘

                      ┌─────────────┐
                      │    tests    │
                      │   Pytest    │
                      └─────────────┘
---

# 🔄 Data Engineering Pipeline

BuildQuant follows a simple data pipeline:

```text
COLLECT
   ↓
VALIDATE
   ↓
TRANSFORM
   ↓
INTEGRATE
   ↓
STORE
   ↓
ANALYSE
   ↓
VISUALISE
   ↓
REPORT
```

### 1. Collect

The user enters residential project information through Streamlit.

### 2. Validate

The application checks that required fields and dimensions contain valid values.

### 3. Transform

Raw project dimensions are transformed into useful quantities such as floor area and net wall area.

### 4. Integrate

Material rates are retrieved from an external Flask REST API.

### 5. Store

Project and cost information is stored in SQLite.

### 6. Analyse

Pandas is used to load and analyse historical project data.

### 7. Visualise

Streamlit charts and dashboard components display the results.

### 8. Report

ReportLab generates a downloadable PDF report.

---

# 🧮 Example Calculation

For a simple 10 m × 8 m dwelling:

```text
Length       = 10 m
Width        = 8 m
Wall Height  = 2.7 m
Doors        = 6
Windows      = 8
```

BuildQuant calculates approximately:

```text
Floor Area          = 80.00 m²
Perimeter           = 36.00 m
Gross Wall Area     = 97.20 m²
Door Opening Area   = 11.34 m²
Window Opening Area = 11.52 m²
Net Wall Area       = 74.34 m²
```

With the prototype allowances:

```text
Floor Tiles = 88.00 m²
Paint Area  = 78.06 m²
```

Using the prototype API rates:

```text
Floor Tiles = R30,800.00
Paint       = R9,367.20

Total       = R40,167.20
```

These figures are examples produced by the prototype's simplified calculation rules and are not professional QS measurements.

---

# 🔌 REST API

The material service is implemented with Flask.

### Endpoint

```text
GET /materials/<material>
```

Supported prototype materials include:

```text
concrete
tiles
paint
```

Example:

```text
GET /materials/paint
```

Response:

```json
{
    "material": "paint",
    "unit": "m2",
    "rate": 120
}
```

BuildQuant uses the returned `rate` rather than keeping the material rate directly inside the Streamlit calculation logic.

This demonstrates a simple **service integration pattern** between two applications.

---

# 🗄️ Database

BuildQuant uses SQLite for local project storage.

The `projects` table stores information including:

```text
Project details
Building dimensions
Doors
Windows
Floor area
Perimeter
Gross wall area
Door area
Window area
Net wall area
Tile quantity
Paint area
Tile rate
Paint rate
Tile cost
Paint cost
Total cost
```

Historical records can then be loaded into Pandas for analytics.

---

# 🖥️ Application Pages

## 🏠 Dashboard

Provides an overview of saved projects and current estimates.

## 📋 New Project

Collects project information and performs the calculation workflow.

## 📐 Quantities

Displays detailed quantity calculations for the current project.

## 💰 Cost Estimate

Displays material rates, material costs and total estimated cost.

## 📊 Analytics

Analyses historical project information stored in SQLite.

## 📄 Reports

Generates downloadable PDF reports.

---

# 🧪 Testing

Pytest is used to test the calculation functions.

Example tests cover:

- Floor area
- Perimeter
- Gross wall area
- Door area
- Window area
- Net wall area
- Waste/allowance calculations

Run the tests with:

```bash
pytest
```

---

# 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Web application interface |
| Pandas | Data analysis and transformation |
| SQLite | Local project database |
| SQL | Database querying |
| Flask | Material Price REST API |
| Requests | HTTP communication with API |
| ReportLab | PDF report generation |
| Pytest | Automated testing |
| Git | Version control |
| GitLab | Repository and collaboration |

---

# 📁 Project Structure

```text
BuildQuant/
│
├── api/
│   └── material_api.py
│       └── Flask REST API for material prices
│
├── calculations/
│   ├── quantity_calculations.py
│   │   └── Residential quantity calculation functions
│   ├── cost_calculations.py
│   │   └── Material cost calculation functions
│   └── material_api.py
│       └── Client used to communicate with the REST API
│
├── database/
│   └── database.py
│       └── SQLite database creation, storage and retrieval
│
├── data/
│   └── buildquant.db
│       └── Local SQLite project database
│
├── reports/
│   └── generate_report.py
│       └── PDF report generation
│
├── tests/
│   ├── README.md
│   │   └── Testing documentation
│   ├── test_input_validation.py
│   │   └── Input validation tests
│   └── test_quantity_calculations.py
│       └── Quantity calculation tests
│
├── validation/
│   └── input_validation.py
│       └── Project input validation logic
│
├── app.py
│   └── Main Streamlit application
│
├── requirements.txt
│   └── Python project dependencies
│
└── .gitignore
    └── Files and folders excluded from Git

> The SQLite database and generated reports are ignored by Git according to `.gitignore`.

---

# 🚀 Installation

## 1. Clone the repository

```bash
git clone <your-gitlab-repository-url>
```

Then enter the project directory:

```bash
cd BuildQuant
```

## 2. Create a virtual environment

Windows:

```bash
python -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Running BuildQuant

BuildQuant uses two processes:

### Terminal 1 — Start the Material API

```bash
python api/material_api.py
```

The API runs on:

```text
http://localhost:5000
```

### Terminal 2 — Start Streamlit

```bash
streamlit run app.py
```

The Streamlit application will open in your browser.

---

# 🔗 Systems Integration

The project intentionally uses a simple REST integration rather than adding unnecessary infrastructure.

```text
BuildQuant
    │
    │ GET /materials/tiles
    ▼
Material Price API
    │
    │ JSON
    ▼
{
    "material": "tiles",
    "unit": "m2",
    "rate": 350
}
    │
    ▼
BuildQuant
    │
    ▼
Quantity × Rate
    │
    ▼
Material Cost
```

This demonstrates:

- HTTP requests
- REST endpoints
- JSON
- API consumption
- Service integration
- Error handling

---

# 🐛 Bugs Encountered and Solutions

## 1. Dashboard Column Mismatch Crash

### Bug Description

The application crashed with a `ValueError` indicating that a specific number of columns were passed, for example:

```text
16 columns passed, passed data had 23 columns
```

when rendering the project DataFrame on the Dashboard or Analytics pages.

### Root Cause

The database schema and calculation engine were updated to include additional fields such as:

- Material rates
- Tile quantities
- Paint quantities
- Individual material costs
- Total cost

This increased the returned project data to **23 columns**.

However, the hardcoded:

```python
columns = [...]
```

lists inside the Streamlit Dashboard and Analytics views still expected the old 16-column database layout.

### Solution

Updated the explicit column-name lists in both pages so they match the exact 23-column schema returned by:

```python
get_projects()
```

This restored correct DataFrame construction and prevented the mismatch crash.

---

## 2. Button Control Flow & Indentation Bug in New Project Handler

### Bug Description

Clicking the:

```text
🧮 Calculate Quantities
```

button sometimes bypassed the core calculation logic or failed to trigger input validation correctly.

### Root Cause

The input-validation blocks were incorrectly indented underneath the Streamlit button handler.

This caused scoping/control-flow problems and premature exits.

### Solution

The New Project handler was restructured so that the operations execute sequentially:

```text
Button pressed
      ↓
Input validation
      ↓
Quantity calculations
      ↓
REST API calls
      ↓
Cost calculations
      ↓
SQLite persistence
      ↓
Session state update
      ↓
Success message
```

This ensured the complete workflow runs only when the Calculate button is pressed.

---

## 3. Missing UI Disclaimers on Quantities & Cost Estimate Pages

### Bug Description

The professional educational disclaimer was already included in the PDF export and Reports page, but it was missing from the interactive:

- `📐 Quantities`
- `💰 Cost Estimate`

pages.

### Root Cause

The warning UI components had not been added to those page layouts.

### Solution

Added prominent `st.warning()` callouts to both pages explaining that:

> BuildQuant is an educational prototype and does not replace professional quantity surveying or formal Bills of Quantities.

This makes the limitation visible throughout the application rather than only inside generated reports.

---

# ⚠️ Limitations

BuildQuant is deliberately a simplified educational prototype.

Current limitations include:

- Simplified quantity calculation rules
- Fixed door dimensions
- Fixed window dimensions
- Simplified waste percentages
- Limited material catalogue
- Prototype material rates
- Local SQLite storage
- No user authentication
- No multi-user deployment
- No professional QS measurement rules
- No formal BoQ generation
- No live commercial material-price service
- No project-level permissions

---

# 🔮 Future Improvements

Possible future development includes:

- More construction material categories
- Configurable door/window dimensions
- More detailed quantity take-offs
- Professional BoQ structure
- User authentication
- Cloud database
- Live material pricing
- Supplier integration
- Advanced project filtering
- Export to Excel
- More advanced data visualisation
- Automated testing for the API
- Deployment to a cloud platform
- Role-based access
- Construction project forecasting

---

# 🎓 Educational Purpose

BuildQuant was developed as a practical way to connect software development and data engineering concepts with a construction-related domain.

It demonstrates how knowledge from:

- Construction
- Quantity surveying concepts
- Python
- Databases
- REST APIs
- Data analysis
- Software engineering
- Testing
- Reporting

can be combined into a single application.

---

# 📌 Project Status

**Status: Functional educational prototype**

The current version includes:

- Streamlit interface
- Multi-page navigation
- Quantity calculations
- Input validation
- SQLite persistence
- Historical cost storage
- Flask REST API
- JSON data exchange
- API error handling
- Dashboard
- Analytics
- Cost estimation
- PDF reporting
- Automated calculation tests

---

# 👩🏽‍💻 Author

**Joélle November**

WeThinkCode_ student interested in:

- Software Development
- Data Engineering
- Systems Integration
- Construction Technology
- Data-driven solutions

---

## 📄 Disclaimer

BuildQuant is an educational software prototype created for learning and demonstration purposes. It is not a professional quantity-surveying, engineering, estimating, or construction-management system. Calculations and rates should not be used as the basis for actual construction procurement, tendering, contracts, or professional Bills of Quantities.