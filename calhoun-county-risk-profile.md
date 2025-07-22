% Community Weather Risk Profile: Calhoun County, Alabama
% CarlyAnnaWX
% July 2025

# Executive Summary

This Community Weather Risk Profile assesses tornado risk and community vulnerability in Calhoun County, Alabama, from 2000 to 2023. The goal is to highlight how physical hazard exposure and social vulnerability intersect, influencing public response to severe weather warnings and preparedness.

This document is part of a larger initiative to visualize local-level weather risks through data and communication analysis.

# 1. Tornado Risk Overview

## 1.1 Tornado Frequency (2000–2023)

- **Total Tornadoes:** 25
- **Peak Years:** 2011, 2019
- **Seasonal Trends:** Most tornadoes occurred between March and May.

![Figure 1: Tornadoes per Year](tornadoes_per_year.png)


## 1.2 Tornado Intensity

| EF Rating | Count |
|-----------|-------|
| EF0       | 8     |
| EF1       | 10    |
| EF2       | 5     |
| EF3       | 2     |
| EF4       | 0     |
| EF5       | 0     |

![Figure 2: Tornado Intensity](tornadoes_by_intensity.png)

## 1.3 Damages and Injuries

- **Injuries:** 15
- **Fatalities:** 1
- **Estimated Damage:** $5 million

![Figure 3](impact_by_intensity.png)


## 1.4 Geographic Patterns

Tornadoes frequently occur in the western portion of Calhoun County, with clusters near Oxford and Anniston.

[Interactive Tornado Map – Calhoun County](tornado_map.html)


# 2. Social Vulnerability Analysis

## 2.1 Demographics and Barriers

- **Population (2020):** 113,605
- **Languages Spoken at Home (non-English):** 4%
- **Households Without Internet:** 12%
- **Poverty Rate:** 17%
- **Median Household Income:** $44,000

Data sourced from the U.S. Census Bureau and CDC Social Vulnerability Index.


## 2.2 Communication Gaps

Calhoun County contains vulnerable subpopulations:
- Older adults (14%)
- Mobile home residents (10%)
- Spanish-speaking communities (4%)

These groups may face challenges in receiving or acting on tornado warnings.

# 3. Integrated Risk Profile

By combining tornado exposure with demographic vulnerability, we identify high-risk zones within the county. These areas are priority targets for improved warning systems, outreach, and preparedness campaigns.

*Insert Figure 6: Combined tornado + vulnerability risk overlay map*

# 4. Recommendations

- Enhance bilingual warning messaging
- Target outreach to mobile home communities
- Collaborate with local schools and churches for preparedness education
- Expand NOAA Weather Radio access and app-based alerts

# 5. Data Sources

- National Weather Service (NWS Storm Events Database)
- U.S. Census Bureau (2020 ACS 5-Year Estimates)
- CDC/ATSDR Social Vulnerability Index
- Local emergency management reports

# Appendix

## A. Methodology Notes

- Tornado data filtered by Calhoun County polygon
- Demographic data collected at census tract level
- Risk overlays created using Python (Pandas, Folium/Plotly)

## B. License

This document is shared under a [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/).
