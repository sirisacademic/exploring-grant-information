# Exploring Grant Information 🤿💎🔬
Hi Carolina! 👋  
Welcome to our shared repo for diving into the world of grant information extraction and normalisation.

## 🎯 Project Context & Goals

This exploratory work is part of Carolina's **Torres Quevedo** grant — with the broader aim of understanding how research funding is acknowledged and referenced in scientific publications.

We're starting by analyzing **acknowledgment sections** to uncover patterns, funder mentions, grant IDs, and other signals that might help build new knowledge bases and repositories of research funding data.

Ultimately, the goal is to better capture, structure, and reuse grant-related information across publications and institutions.

## 🧱 Repository Structure

This repo follows the [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/) structure, which is designed to keep projects tidy and reproducible.

Here's a quick overview:

```
exploring-grant-information/
├── data/                # Raw, interim, and processed data files
├── docs/                # Any project documentation
├── models/              # Trained models or outputs (optional)
├── notebooks/           # Jupyter notebooks go here
│   └── 1-lets start by exploring acknoledgment sections.ipynb
├── src/                 # Python scripts for data loading, processing, etc.
├── environment.yml      # Conda environment for reproducibility
├── .gitignore
└── README.md
```

---

## 📂 Shared Google Drive & Project Tracker (Collaborative Notes)

All supplementary documents, papers, and project coordination notes are stored in our shared Google Drive folder:

👉 [Google Drive - Project Folder](https://drive.google.com/drive/folders/1hLOuAWe5LVxzj_TvNeAy1pgk1QA5ya2e)

>Please make sure to keep it organized and upload relevant resources (e.g., papers, PDFs, datasets) there.

### 

We’re using a shared 📒 Google Docs to track our progress, take notes during literature review, and jot down insights:

📝 [Project Tracker & Notes](https://docs.google.com/document/d/1Bssmc4guzhIvL8jdvqZaHFpbbG4cIQIqVw2QtXk_yNo/edit?tab=t.0#heading=h.54gk095ywfd6)

>Use this file to:
>- Log explored datasets
>- Note PubMed queries
>- Track ideas for extraction/normalization
>- Document any challenges or decisions

This helps us stay synced and makes it easier to look back on the reasoning behind choices later on.


---

## 🧪 Setting Up the Environment

To make sure everything works smoothly on both our machines, we’re using a **conda environment** that contains all the required libraries.

### Step-by-step setup:

1. Open your terminal or Anaconda Prompt.
2. Navigate to the folder where you cloned this repo.
3. Create the environment from the `environment.yml` file:

```bash
conda env create -f environment.yml
```

4. Activate the environment:

```bash
conda activate grant-explore
```

5. You can now open Jupyter Notebooks inside this environment:

```bash
jupyter notebook
```

---

## 🔄 Updating the Environment

If you (or I) install new packages, we should re-export the environment so it stays in sync:

```bash
conda env export --from-history > environment.yml
```

Then commit and push the updated `environment.yml`.

To update your local environment with changes, just re-run:

```bash
conda env update -f environment.yml
```

---

## 📓 First Notebook

We're starting with this notebook:

📘 `notebooks/1-lets start by exploring acknoledgment sections.ipynb`

In it, we’ll:
- Load acknowledgment sections from PubMed and our SciLake dataset.
- Explore how funders and grants are mentioned.
- Identify patterns and start thinking about how we might extract structured info from this messy text.

---

## 🤝 Collaborating

When working together, it’s best to use **branches** to keep things clean:

- To start working on something:
  ```bash
  git checkout -b feature/my-topic
  ```

- After making changes:
  ```bash
  git add .
  git commit -m "Brief description of changes"
  git push origin feature/my-topic
  ```

- Then open a **Pull Request** on GitHub so we can review and merge.

---

## 🧱 Next Steps

Let’s explore and build something cool together! 🚀  
Any questions, just ping me — I’m happy to walk through anything step by step.

