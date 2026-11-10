"""Row-group profiling helpers."""

import pyarrow.parquet as pq


def profile_table(path):
    """Return per-column statistics for every row group in ``path``."""
    metadata = pq.ParquetFile(path).metadata
    columns = {}
    for rg in range(metadata.num_row_groups):
        group = metadata.row_group(rg)
        for col in range(group.num_columns):
            column = group.column(col)
            stats = column.statistics
            columns.setdefault(column.path_in_schema, []).append(
                {
                    "row_group": rg,
                    "compression": column.compression,
                    "min": stats.min if stats and stats.has_min_max else None,
                    "max": stats.max if stats and stats.has_min_max else None,
                }
            )
    return columns
