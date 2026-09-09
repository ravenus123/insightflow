# InsightFlow wireframes — V0.1

These wireframes are intentionally neutral. The design sheet should replace visual tokens and component styling without changing the page hierarchy.

## 1. Overview

```text
+----------------------+-------------------------------------------+
| InsightFlow          | Demo Workspace               V0.1        |
|                      +-------------------------------------------+
| Overview             | InsightFlow                                |
| Datasets             | Turn raw sales data into decisions.       |
| Dashboard            |                                           |
| Reports      Soon    | +----------------+ +-------------------+   |
| Settings     Soon    | | Import dataset | | View dashboard    |   |
|                      | +----------------+ +-------------------+   |
+----------------------+-------------------------------------------+
```

## 2. Upload

```text
+----------------------+-------------------------------------------+
| InsightFlow          | Import dataset                            |
|                      | Bring a sales CSV into InsightFlow.       |
| Datasets             |                                           |
|                      | +---------------------------------------+ |
|                      | |                                       | |
|                      | |       Drop your dataset here          | |
|                      | |          [ Choose file ]              | |
|                      | |                                       | |
|                      | +---------------------------------------+ |
+----------------------+-------------------------------------------+
```

## 3. Preview / semantic mapping

```text
+----------------------+-------------------------------------------+
| InsightFlow          | Retail Sales Q1                           |
|                      | 84,291 rows · 9 columns                   |
|                      |                                           |
|                      | Detected fields       Dataset metadata    |
|                      | Date       [order_date] High              |
|                      | Revenue    [total_price] High              |
|                      | Product    [product_name] High             |
|                      | Order ID   [order_id] High                 |
|                      |                                           |
|                      | Data preview table                         |
|                      |                         [Generate dashboard]|
+----------------------+-------------------------------------------+
```

## 4. Analytics dashboard

```text
+----------------------+-------------------------------------------+
| InsightFlow          | Retail Sales                              |
|                      | Jan 1 - Mar 31, 2026                      |
|                      |                                           |
|                      | +Revenue+ +Orders+ +Average Order+        |
|                      |                                           |
|                      | +---------------------------------------+ |
|                      | | Revenue over time                     | |
|                      | |            line chart                 | |
|                      | +---------------------------------------+ |
|                      |                                           |
|                      | + Top products table -------------------+ |
+----------------------+-------------------------------------------+
```

## Design-sheet handoff checklist

When the design sheet arrives, map it onto:

- typography scale
- color tokens
- spacing scale
- radii
- borders / shadows
- sidebar and topbar treatment
- button variants
- card treatment
- table density
- chart presentation
- empty/loading/error states
- responsive behavior
