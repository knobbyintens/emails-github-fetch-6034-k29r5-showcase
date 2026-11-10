# Parquet Lens

**Status: Released — v1.2.0**

Column-level profiler for large Parquet lakes.

## Install

```
pip install parquet-lens
```

## What is included

- Row-group statistics and compression skew report
- Null-density and dictionary-coverage heat map
- JSON report consumable by CI jobs

## Layout

- `src/parquet_lens/profiler.py`
- `src/parquet_lens/report.py`
