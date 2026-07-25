# Tableau Desktop & Tableau Public Integration Guide

**Author:** KADALI GEETHA SRAVYA  
**Project:** Cosmetic Insights: Navigating Cosmetics Trends and Consumer Behavior with Tableau  
**Dataset:** `data/cosmetics_clean.csv` (1,472 Rows, 10 Fields + Calculated Fields)

---

## Step 1: Connect to Dataset
1. Open **Tableau Desktop** or **Tableau Public**.
2. Click **Connect to Data** -> **Text File** -> Select `data/cosmetics_clean.csv`.
3. Verify all columns: `Label`, `Brand`, `Name`, `Price`, `Rank`, `Ingredients`, `Combination`, `Dry`, `Normal`, `Oily`, `Sensitive`.

---

## Step 2: Create Calculated Field (`ALL SKIN TYPES COUNT`)
1. In the Data pane, click the drop-down arrow next to Search and select **Create Calculated Field...**
2. Name the field: `ALL SKIN TYPES COUNT`
3. Enter formula:
   ```tableau
   [Combination] + [Dry] + [Normal] + [Oily] + [Sensitive]
   ```
4. Click **OK**.

---

## Step 3: Build Worksheets
1. **Sheet 1: Category Distribution (Tree Map / Bubble Chart)**
   - Drag `Label` to Colors & Detail.
   - Drag `CNT(Name)` to Size & Labels.
2. **Sheet 2: Brand Price Scatter Plot**
   - Drag `Price` to Columns (AVG).
   - Drag `Rank` to Rows (AVG).
   - Drag `Brand` to Detail & Color.
3. **Sheet 3: Skin Type Suitability Bar Chart**
   - Drag `Label` to Rows.
   - Drag `ALL SKIN TYPES COUNT` to Columns (SUM/AVG).

---

## Step 4: Assemble Dashboard & Story
1. Create a **New Dashboard** titled `Cosmetics Insights Dashboard`.
2. Add interactive filters for `Label`, `Brand`, and `Skin Type`.
3. Create a **New Story** titled `Cosmetics Trends & Consumer Story` with 4 scenes.

---

## Step 5: Publish & Web Integration
1. Go to **File** -> **Save to Tableau Public...**
2. Copy the embed code/URL and place it inside `templates/index.html` in your Flask application.
