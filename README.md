# spotify-platform-analysis
Cross-platform listening behavior analysis using Spotify Web API

## Project Overview
An analysis of cross-platform listening patterns on Spotify to understand how users engage with music across different devices (mobile, desktop, TV, smart speakers, wearables, automotive etc.).

**Research Question:** What factors predict when a user switches from one platform to another, and how does this affect their engagement?

## Motivation
This project was created to understand user behavior patterns that inform product decisions for Spotify's Platform & Partner Experience team, which optimises consumer experiences across different devices.

## Privacy & Ethics
- All user data is **completely anonymised** in this repository
- User IDs are replaced with pseudonyms (User_A, User_B, etc.)
- Raw data is excluded from version control
- Only aggregated, anonymised insights are shared
- All participants provided informed consent

## Project Structure
```
spotify-platform-analysis/
├── data/
│   ├── raw/              # Raw API responses (not in git)
│   ├── interim/          # Intermediate processing (not in git)
│   └── processed/        # Anonymised, analysis-ready data
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_statistical_modeling.ipynb
│   └── 04_insights_summary.ipynb
├── src/
│   ├── data_collection.py
│   ├── data_processing.py
│   ├── analysis.py
│   └── visualisation.py
├── reports/
│   └── figures/
├── config/
│   └── config.yaml
├── requirements.txt
└── README.md
```

## Tech Stack
- **Python 3.9+**
- **Spotipy** (Spotify API wrapper)
- **pandas** (data manipulation)
- **scikit-learn** (statistical modeling)
- **lifelines** (survival analysis)
- **plotly/seaborn** (visualisation)

## Setup Instructions
[Coming soon]

## Key Findings
[Will be updated as analysis progresses]

## Next Steps
[Future work and extensions]

---
**Note:** This is a personal learning project created for educational purposes.
```
