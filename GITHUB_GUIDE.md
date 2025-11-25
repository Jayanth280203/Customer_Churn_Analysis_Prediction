# How to Publish Your Project to GitHub

This guide will help you upload your Churn Analysis project to GitHub.

## Prerequisites
- **Git** installed on your computer.
- A **GitHub Account**.

## Step 1: Initialize Git (Local)

1.  Open your terminal (Command Prompt or PowerShell) in the project folder:
    `c:\Users\GALLIS\Desktop\Churn_analysis_predicton`
2.  Initialize a new git repository:
    ```bash
    git init
    ```
3.  Add your files to the staging area:
    ```bash
    git add .
    ```
4.  Commit your changes (save them to history):
    ```bash
    git commit -m "Initial commit: Churn analysis scripts and data"
    ```

## Step 2: Create a Repository on GitHub

1.  Log in to [GitHub.com](https://github.com).
2.  Click the **+** icon in the top-right corner and select **New repository**.
3.  **Repository name**: `churn-analysis-prediction` (or any name you like).
4.  **Description**: "Customer churn prediction using Random Forest and Tableau dashboard."
5.  **Public/Private**: Choose Public (visible to everyone) or Private.
6.  **Do NOT** check "Add a README", ".gitignore", or "license" (we already have them).
7.  Click **Create repository**.

## Step 3: Connect and Push

1.  Copy the URL of your new repository. It will look like:
    `https://github.com/YOUR_USERNAME/churn-analysis-prediction.git`
2.  Back in your terminal, link your local repo to GitHub:
    ```bash
    git remote add origin https://github.com/YOUR_USERNAME/churn-analysis-prediction.git
    ```
    *(Replace `YOUR_USERNAME` with your actual GitHub username)*
3.  Push your files to GitHub:
    ```bash
    git branch -M main
    git push -u origin main
    ```

## Step 4: Verify
Refresh your GitHub repository page. You should see all your files (`churn_analysis.py`, `README.md`, `TABLEAU_GUIDE.md`, etc.) listed there.
