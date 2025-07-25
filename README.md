# ⚡ Global Electric Vehicle (EV) Adoption Dashboard (2010–2024)

This interactive dashboard visualizes global Electric Vehicle (EV) adoption trends using data from 2010 to 2024. Built with **Dash**, **Plotly**, and **Pandas**, the project explores EV vs non-EV sales, Battery Electric Vehicles (BEV) vs (Plug Hybrid Electric Vehicle )PHEV breakdowns, and market share comparisons by country and year.

---

## 🚘 Project Purpose

This dashboard answers key questions such as:

- How are electric vehicles being adopted globally?
- Which countries lead in EV market share?
- How do battery-electric vehicles (BEVs) compare to plug-in hybrids (PHEVs)?
- How has EV adoption evolved over time?

---

## 🧱 Tech Stack

| Tool | Description |
|------|-------------|
| `Dash` | Python framework for interactive web apps |
| `dash-bootstrap-components` | Pre-built UI components and responsive layout |
| `dash_ag_grid` | Fast, feature-rich data tables |
| `pandas` | Data manipulation and analysis |
| `plotly` | High-quality, interactive visualizations |

---

## 📁 Project Structure

```
ev-dashboard/
├── assets/
│   └── style.css                      # Custom styling (Bootstrap theme or overrides)
├── environment/
│   └── requirements.txt              # All dependencies listed here
├── src/
│   ├── components/                   # Dash components and layouts
│   │   ├── area_graph.py
│   │   ├── bar_chart.py
│   │   ├── country_checklist.py
│   │   ├── data_grid.py
│   │   ├── ids.py
│   │   ├── layout.py
│   │   ├── line_chart.py
│   │   ├── year_dropdown.py
│   │   └── __init__.py
│   ├── data/                         # Data loading and utilities
│   │   ├── loader.py
│   │   └── __init__.py
│   └── __init__.py
├── main.py                           # Entry point for the Dash app
├── .gitignore
└── README.md
```

---

## 🚀 How to Run the App

### 1. Clone the Repository
```bash
git clone https://github.com/kpedidogodonou/ev-dashboard.git
cd ev-dashboard
```

### 2. Set Up Environment
```bash
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r environment/requirements.txt
```

### 3. Run the App
```bash
python main.py
```

Then visit: [http://localhost:8050](http://localhost:8050)

---

## 📈 Dashboard Features

- 📊 **EV vs Non-EV Sales** (stacked bar chart)
- 🔌 **BEV vs PHEV Adoption** by country and year
- 🌍 **Country-specific dropdown filters**
- 📅 **Year range selectors**
- 📋 **AG Grid data table** with sorting and filtering
- 📱 Responsive layout using Dash Bootstrap Components

---

## 📚 Data Sources

- **International Energy Agency – Global EV Outlook 2025**
- **Our World in Data** – [EV Dataset](https://ourworldindata.org/energy)

---

## 📦 Requirements

```
dash
dash-bootstrap-components
dash-ag-grid
pandas
plotly
```

(Already listed in `environment/requirements.txt`)

---

## 💡 Sample Insights

- Norway leads with ~90% of new car sales being electric.
- Global EV sales have grown exponentially since 2020.
- Plug-in hybrids are more common in countries with weaker charging infrastructure.
- EV market share is rising but ICE cars still dominate globally.

---

## 👤 Author

**Kpêdido Godonou**  
[🌐 kpedido.com](https://kpedido.com) | [📧 Contact](mailto:kpedido.godonou@gmail.com)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).