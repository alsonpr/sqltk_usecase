# SQL Report

- **name::**  Alson
- **serial_no::**  1098
- **task::**  print first column from student table
### Submitted Query

```sql
SELECT name, phone_number FROM employee;
```

## Syntax Validation

### Formatted Query

```sql
SELECT name,
       phone_number
FROM employee;
```

- **Test Results:**

   &ndash;   Fantastic news! No issues were found in your query. 

## Context Validation

### Formatted Query

```sql
SELECT name,
       phone_number
FROM employee;
```

- **Test Results:**

   &ndash;   Fantastic news! No issues were found in your query. 

## Semantic Validation

### Formatted Query

```sql
SELECT name,
       phone_number
FROM employee;
```

- **Test Results:**

  - **Test Name:** execute_sql
  - **Test Name:** performance_metrics
       - Your SQL query ran like a charm. The total cost to run the query was 0.45
       - Your actual running time was 0.012
  - **Test Name:** check_analysis
       - Great work! The columns returned by your query are ['name', 'phone_number']
