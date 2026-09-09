# 🏗️ BuildQuant

## Residential Quantity Estimation & Data Engineering System

BuildQuant is a beginner-friendly software project that applies **Data Engineering and Systems Integration concepts to the construction industry**.

The system is designed to assist with the **preliminary quantity estimation of a proposed residential dwelling**. Users enter basic building information and dimensions, and BuildQuant processes the data to produce estimated construction quantities.

The project combines a construction/Quantity Surveying problem with software development and data engineering.

---

# 🎯 Project Goal

The goal of BuildQuant is to create a system that can:

1. Collect proposed dwelling information.
2. Validate user input.
3. Transform building measurements into quantities.
4. Apply simple material and waste calculations.
5. Store project information and calculated quantities.
6. Display results through a graphical user interface.
7. Eventually retrieve material rates through a REST API.
8. Generate a professional preliminary quantity report.

---

# 👷 Target User

The primary target user is a:

* Quantity Surveyor
* Construction student
* Building estimator
* Construction project manager
* Property developer

The system is intended to support **preliminary estimating** and is not intended to replace professional Quantity Surveying measurements or final Bills of Quantities.

---

# 🛠️ Technologies

The project currently uses or plans to use:

* **Python** — Application logic and calculations
* **Streamlit** — Graphical user interface
* **SQLite** — Project and quantity data storage
* **SQL** — Data querying
* **Pandas** — Data processing and analysis
* **ReportLab** — PDF report generation
* **Pytest** — Automated testing
* **Git** — Version control

---

# 📁 Project Structure

```text
BuildQuant/
│
├── calculations/
│   └── quantity_calculations.py
│
├── data/
│
├── database/
│
├── reports/
│
├── tests/
│   └── test_quantity_calculations.py
│
├── validation/
│
├── app.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📅 Development Progress

## Day 1 — Project Setup

The first day focused on establishing the foundation of the BuildQuant project.

### Completed

* Created the BuildQuant project structure.
* Created the Python virtual environment.
* Installed Streamlit.
* Created the initial Streamlit application.
* Created the README documentation.
* Created `requirements.txt`.
* Added `.gitignore`.
* Initialised Git.
* Created the first Git commit.

### Initial Application

The first version of BuildQuant displayed a basic Streamlit interface containing the project name and description.

---

# 📅 Day 2 — Dwelling Input GUI

Day 2 focused on creating the **data collection layer** of BuildQuant.

The application was changed from a basic welcome screen into an input form where the user can enter information about a proposed dwelling.

### Project Information

The user can enter:

* Project name
* Project number
* Location
* Building type

### Building Dimensions

The user can enter:

* Length in metres
* Width in metres
* Wall height in metres

### Openings

The user can enter:

* Number of doors
* Number of windows

### Current Data Flow

```text
User
  ↓
BuildQuant GUI
  ↓
Dwelling Information
  ↓
Project Summary
```

This establishes the first stage of the data engineering process: **data collection**.

---

# 📅 Day 3 — Quantity Calculation Engine

Day 3 introduced a separate calculation module so that calculation logic does not have to be placed directly inside the GUI.

The calculation functions are stored in:

```text
calculations/quantity_calculations.py
```

### Calculations implemented

#### Floor Area

```text
Length × Width
```

Example:

```text
10m × 8m = 80m²
```

#### Building Perimeter

```text
2 × (Length + Width)
```

Example:

```text
2 × (10 + 8) = 36m
```

#### Gross Wall Area

```text
Perimeter × Wall Height
```

Example:

```text
36m × 2.7m = 97.2m²
```

#### Opening Area

The same function can be used to calculate door or window opening areas.

```text
Width × Height × Quantity
```

Example for six doors:

```text
0.9m × 2.1m × 6 = 11.34m²
```

Example for eight windows:

```text
1.2m × 1.2m × 8 = 11.52m²
```

#### Net Wall Area

```text
Gross Wall Area
− Door Area
− Window Area
```

Example:

```text
97.2 − 11.34 − 11.52
= 74.34m²
```

---

# 🧪 Automated Testing

Automated tests were introduced using **Pytest**.

The tests are stored in:

```text
tests/test_quantity_calculations.py
```

The tests check whether the calculation functions return the expected results.

Current tests include:

* Floor area
* Perimeter
* Gross wall area
* Door opening area
* Window opening area
* Net wall area

Tests can be run using:

```bash
pytest
```

---

# 📅 Day 4 — GUI and Calculation Integration

Day 4 connected the calculation engine to the Streamlit GUI.

The application can now take information entered by the user and pass it to the calculation functions.

### Current process

```text
User enters dwelling data
          ↓
      BuildQuant GUI
          ↓
Quantity calculation functions
          ↓
     Calculated quantities
          ↓
      GUI displays results
```

The application now displays:

* Floor area
* Building perimeter
* Gross wall area
* Door opening area
* Window opening area
* Net wall area

### Example Output

For a dwelling with:

```text
Length: 10m
Width: 8m
Wall Height: 2.7m
Doors: 6
Windows: 8
```

BuildQuant produces approximately:

```text
Floor Area:          80.00m²
Perimeter:           36.00m
Gross Wall Area:     97.20m²
Door Opening Area:   11.34m²
Window Opening Area: 11.52m²
Net Wall Area:       74.34m²
```

---

# 📅 Day 5 — Material Quantities and Waste

Day 5 expanded BuildQuant beyond basic building measurements.

The system now supports simplified material quantity calculations with waste allowances.

## Floor Tiles

A 10% waste allowance is applied to the calculated floor area.

```text
Floor Area × 1.10
```

Example:

```text
80m² × 1.10 = 88m²
```

Therefore:

```text
Estimated Floor Tile Quantity = 88m²
```

## Paint Area

The net wall area is used as the preliminary paint area.

A 5% allowance is currently applied.

```text
Net Wall Area × 1.05
```

Example:

```text
74.34m² × 1.05
= 78.06m²
```

Therefore:

```text
Estimated Paint Area = 78.06m²
```

---

# 📊 Current BuildQuant Data Pipeline

At the end of Day 5, the project has the beginning of a basic data transformation pipeline:

```text
                 RAW DATA
                    │
                    ▼
            ┌──────────────┐
            │  User Input  │
            │              │
            │ Length       │
            │ Width        │
            │ Height       │
            │ Doors        │
            │ Windows      │
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │ Validation   │
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │Transformation│
            │              │
            │ Areas        │
            │ Perimeter    │
            │ Openings     │
            │ Waste        │
            └──────┬───────┘
                   │
                   ▼
            ┌──────────────┐
            │   Quantity   │
            │    Output    │
            └──────────────┘
```

The database and more advanced data storage components will be implemented in later development stages.

---

# 🏠 Current Example Project

The current development example is:

**Project:** Smith Residence

**Project Number:** PRJ-2026-001

**Location:** Cape Town

**Building Type:** Single-storey dwelling

### Dimensions

```text
Length:       10m
Width:         8m
Wall Height:  2.7m
```

### Openings

```text
Doors:    6
Windows:  8
```

### Preliminary Quantities

| Quantity                  | Result | Unit |
| ------------------------- | -----: | ---- |
| Floor Area                |  80.00 | m²   |
| Perimeter                 |  36.00 | m    |
| Gross Wall Area           |  97.20 | m²   |
| Door Opening Area         |  11.34 | m²   |
| Window Opening Area       |  11.52 | m²   |
| Net Wall Area             |  74.34 | m²   |
| Floor Tiles + 10% Waste   |  88.00 | m²   |
| Paint Area + 5% Allowance |  78.06 | m²   |

---

# 🔗 Planned Systems Integration

A simple **Material Price REST API** will be added in a later stage of development.# BuildQuant

## Residential Quantity Estimation & Data Engineering System

BuildQuant is a beginner-friendly data engineering project designed
to assist with preliminary quantity estimation for proposed residential
dwellings.

The system collects building information, validates the data,
calculates construction quantities, stores the results, and generates
a quantity estimation report.

## Project Goal

The goal of BuildQuant is to demonstrate how data engineering can be
applied to a construction and quantity surveying problem.

## Planned Technologies

- Python
- Streamlit
- SQLite
- Pandas# BuildQuant

## Residential Quantity Estimation & Data Engineering System

BuildQuant is a beginner-friendly data engineering project designed
to assist with preliminary quantity estimation for proposed residential
dwellings.

The system collects building information, validates the data,
calculates construction quantities, stores the results, and generates
a quantity estimation report.

## Project Goal

The goal of BuildQuant is to demonstrate how data engineering can be
applied to a construction and quantity surveying problem.

## Planned Technologies

- Python
- Streamlit
- SQLite
- Pandas
- SQL
- ReportLab
- Pytest
- Git

## Project Status

Day 1 - Project setup and initial GUI.
- SQL
- ReportLab
- Pytest
- Git

## Project Status

Day 1 - Project setup and initial GUI.

BuildQuant will request material rates from a separate service.

```text
BuildQuant
    │
    │ HTTP Request# BuildQuant

## Residential Quantity Estimation & Data Engineering System

BuildQuant is a beginner-friendly data engineering project designed
to assist with preliminary quantity estimation for proposed residential
dwellings.

The system collects building information, validates the data,
calculates construction quantities, stores the results, and generates
a quantity estimation report.

## Project Goal

The goal of BuildQuant is to demonstrate how data engineering can be
applied to a construction and quantity surveying problem.

## Planned Technologies

- Python
- Streamlit
- SQLite
- Pandas# BuildQuant

## Residential Quantity Estimation & Data Engineering System

BuildQuant is a beginner-friendly data engineering project designed
to assist with preliminary quantity estimation for proposed residential
dwellings.

The system collects building information, validates the data,
calculates construction quantities, stores the results, and generates
a quantity estimation report.

## Project Goal

The goal of BuildQuant is to demonstrate how data engineering can be
applied to a construction and quantity surveying problem.

## Planned Technologies

- Python
- Streamlit
- SQLite
- Pandas
- SQL
- ReportLab
- Pytest
- Git

## Project Status

Day 1 - Project setup and initial GUI.
- SQL
- ReportLab
- Pytest
- Git

## Project Status

Day 1 - Project setup and initial GUI.
    ▼
Material Price API
    │
    │ JSON Response
    ▼
BuildQuant
    │
    ▼
Quantity × Material Rate
    │
    ▼
Estimated Cost
```

This will demonstrate a basic **Systems Integration** concept using:

* REST
* HTTP
* JSON
* API communication

The integration will intentionally remain simple so that the main focus stays on the Data Engineering project.

---

# 🚧 Current Limitations

BuildQuant currently uses simplified assumptions.

For example:

* The dwelling is assumed to have a rectangular footprint.
* Standard door dimensions are currently used.
* Standard window dimensions are currently used.
* The current wall calculation is simplified.
* Roof, foundation and structural quantities are not yet included.
* Material rates are not yet integrated.
* The current calculations are not intended to replace professional Quantity Surveying measurement.

These limitations will be documented and addressed where appropriate in future versions.

---

# 🔮 Future Improvements

Potential future features include:

* SQLite database
* Multiple project management
* Material rate database
* REST API integration
* Cost estimation
* Quantity dashboard
* Charts and analytics
* PDF report generation
* Bill of Quantities export
* More detailed construction measurements
* Floor-plan upload
* Automated measurement extraction

---

# 📌 Project Status

**Current stage:** Day 5 — Quantity calculation and material estimation

### Completed

* [x] Project setup
* [x] Streamlit GUI
* [x] Dwelling input form
* [x] Quantity calculation engine
* [x] Automated calculation tests
* [x] GUI/calculation integration
* [x] Basic material quantities
* [x] Waste allowances

### Upcoming

* [ ] Input validation
* [ ] SQLite database
* [ ] SQL queries
* [ ] Data processing with Pandas
* [ ] Dashboard
* [ ] Cost estimation
* [ ] Material Price REST API
* [ ] Systems Integration
* [ ] PDF report
* [ ] Final testing
* [ ] Final documentation

---

# 👩‍💻 Development Approach

BuildQuant is being developed incrementally.

Each development stage focuses on a small feature that is tested before moving to the next stage.

The project uses Git version control to maintain a history of development and demonstrate continuous progress.

```
