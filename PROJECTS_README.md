# Machine Learning Micro-Projects Page

This document provides instructions for managing the Machine Learning Micro-Projects page (`ml-projects.html`).

## 1. How to Add New Projects

To add a new project, open `ml-projects.html` and locate the appropriate `<section>` for the category (e.g., `Supervised Learning`).

Add a new `div` with the class `project-card`.

**Template for a "Coming Soon" project:**
```html
<div class="project-card coming-soon" data-status="coming-soon">
    <div class="card-content">
        <h3>Project Title</h3>
        <span class="category-label">Category Name</span>
        <div class="status-badge">
            <i class="fas fa-clock"></i> Coming Soon
        </div>
    </div>
</div>
```

**Template for a "Completed" project:**
```html
<!-- Wrap in an <a> tag if you want it to link to a specific page -->
<a href="path/to/project.html" class="project-card-link">
    <div class="project-card completed" data-status="completed">
        <div class="card-content">
            <h3>Project Title</h3>
            <span class="category-label">Category Name</span>
            <div class="status-badge">
                <i class="fas fa-check"></i> Done
            </div>
        </div>
    </div>
</a>
```

## 2. How to Toggle "Coming Soon" → "Complete"

To mark a project as complete:

1.  **Remove** the `coming-soon` class from the `project-card` div.
2.  **Add** the `completed` class to the `project-card` div.
3.  **Update** the `data-status` attribute to `completed`.
4.  **Change** the icon in the `.status-badge` from `fa-clock` to `fa-check`.
5.  **Change** the text in the `.status-badge` from "Coming Soon" to "Done".
6.  (Optional) Wrap the card in an `<a>` tag to make it link to the project implementation.

**Example Change:**

*From:*
```html
<div class="project-card coming-soon" data-status="coming-soon">
    <div class="card-content">
        <h3>Linear Regression</h3>
        ...
        <div class="status-badge"><i class="fas fa-clock"></i> Coming Soon</div>
    </div>
</div>
```

*To:*
```html
<a href="linear-regression.html" class="project-card-link">
    <div class="project-card completed" data-status="completed">
        <div class="card-content">
            <h3>Linear Regression</h3>
            ...
            <div class="status-badge"><i class="fas fa-check"></i> Done</div>
        </div>
    </div>
</a>
```

The **Progress Tracker** will automatically update based on the number of cards without the `coming-soon` class.

## 3. How to Deploy/Update via GitHub Pages

Since this page is part of your existing GitHub repository, deployment is straightforward:

1.  **Commit and Push** your changes to the main branch (usually `main` or `master`).
    ```bash
    git add ml-projects.html ml-projects.css ml-projects.js PROJECTS_README.md
    git commit -m "Add ML Projects page"
    git push origin main
    ```

2.  **GitHub Pages** should automatically rebuild the site.
3.  Access the new page at: `https://rubengonv.github.io/RubenGonV/ml-projects.html` (adjust the URL based on your actual GitHub Pages URL structure).

## 4. Customization

*   **Colors**: Edit the CSS variables in `ml-projects.css` under `:root` (for light mode) and `.dark-mode` (for dark mode).
*   **Categories**: You can add new category sections in `ml-projects.html` by copying an existing `<section class="category-section">`.
