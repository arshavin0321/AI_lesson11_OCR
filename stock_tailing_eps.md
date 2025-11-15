stock_tailing_eps

Source: https://ycharts.com/companies/${symbol}/eps_ttm
Description: Provides financial metrics such as Trailing earnings per share (TTM EPS).

## Data Overview

- **Total Rows**: 266,181
- **Date Range**: 2006-01-31 to 2025-09-30
- **Unique Symbols**: 5,355
- **Unique Report Dates**: 237
- **Last Update**: 2025-11-08
- **Update Frequency**: Weekly (as of 2025)

## Columns

| Column Name | Column Type | Description | Missing Values |
|------------|-------------|-------------|----------------|
| symbol | VARCHAR | Stock ticker symbol | 0 (0.00%) |
| report_date | VARCHAR | Reporting date (YYYY-MM-DD format) | 0 (0.00%) |
| tailing_eps | DECIMAL(38,2) | Trailing EPS (TTM) | 34,652 (13.02%) |
| eps | DECIMAL(38,2) | EPS (not TTM) | 11,788 (4.43%) |
| update_time | VARCHAR | Last update time (YYYY-MM-DD format) | 0 (0.00%) |

## Data Statistics

### Trailing EPS (tailing_eps)
- **Count**: 231,529 non-null values
- **Mean**: 15,992.38
- **Median**: 0.74
- **Min**: -4,000,000,000.00
- **Max**: 2,000,000,000.00
- **25th Percentile**: -0.47
- **75th Percentile**: 2.38
- **Std Dev**: 14,436,750.00

### EPS (eps)
- **Count**: 254,393 non-null values
- **Mean**: -4,415.43
- **Median**: 0.16
- **Min**: -1,000,000,000.00
- **Max**: 1,000,000,000.00
- **25th Percentile**: -0.13
- **75th Percentile**: 0.60
- **Std Dev**: 9,520,805.00

## Data Quality Notes

- Most rows (231,529) have both `tailing_eps` and `eps` values
- 22,864 rows have only `eps` values (missing `tailing_eps`)
- 11,788 rows are missing both `tailing_eps` and `eps`
- No rows have only `tailing_eps` (all `tailing_eps` values also have corresponding `eps`)

## Most Common Symbols

Top symbols by record count:
- KRMD: 87 records
- TENX: 86 records
- SBLX: 85 records
- SKY: 84 records
- MS: 84 records
- BBY: 83 records
- ALCO: 83 records
- ASUR: 83 records
- MCS: 83 records
- GPN: 83 records

## Analysis Method

Analysis performed using DuckDB on the parquet file to extract statistical insights and data quality metrics.