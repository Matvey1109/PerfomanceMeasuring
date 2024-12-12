# Benchmark Statistics

## Results from Benchmark Tests

| Test Name | Min Time (us) | Max Time (us) | Mean Time (us) | StdDev (us) | Median Time (us) | IQR | OPS | Rounds |
|-----------|---------------|---------------|----------------|-------------|-----------------|-----|-----|-------|
| test_concatenate_with_join[10-10] | 1.4707 | (1.0) | 46.2260 | (1.0) | 1.5859 | (1.0) | (1.0) | 187266 |
| test_concatenate_with_plus_equals[10-10] | 1.6990 | (1.16) | 49.9070 | (1.08) | 1.8201 | (1.15) | (0.87) | 134753 |
| test_concatenate_with_join[100-20] | 10.5200 | (7.15) | 14,573.9510 | (315.28) | 15.0788 | (9.51) | (0.11) | 33666 |
| test_concatenate_with_plus_equals[100-20] | 17.3540 | (11.80) | 208.0220 | (4.50) | 19.2066 | (12.11) | (0.08) | 33756 |
| test_concatenate_with_join[1000-5] | 106.9020 | (72.69) | 60,712.2360 | (>1000.0) | 208.5073 | (131.48) | (0.01) | 6616 |
| test_concatenate_with_plus_equals[1000-5] | 162.4530 | (110.46) | 458.8090 | (9.93) | 178.4101 | (112.50) | (0.01) | 5828 |