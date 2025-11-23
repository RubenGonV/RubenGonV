document.addEventListener('DOMContentLoaded', () => {
    // --- Dark Mode Toggle ---
    const themeToggle = document.getElementById('theme-toggle');
    const body = document.body;
    const icon = themeToggle.querySelector('i');

    // Check for saved user preference, if any, on load of the website
    const savedTheme = localStorage.getItem('theme');
    if (savedTheme === 'dark') {
        body.classList.add('dark-mode');
        icon.classList.remove('fa-moon');
        icon.classList.add('fa-sun');
    }

    themeToggle.addEventListener('click', () => {
        body.classList.toggle('dark-mode');

        if (body.classList.contains('dark-mode')) {
            localStorage.setItem('theme', 'dark');
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            localStorage.setItem('theme', 'light');
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    });

    // --- Progress Tracker ---
    function updateProgress() {
        const totalProjects = document.querySelectorAll('.project-card').length;
        // Count projects that do NOT have the 'coming-soon' class
        const completedProjects = document.querySelectorAll('.project-card:not(.coming-soon)').length;

        const progressCount = document.getElementById('progress-count');
        const progressBar = document.getElementById('progress-bar');

        progressCount.textContent = `${completedProjects}/${totalProjects}`;

        if (totalProjects > 0) {
            const percentage = (completedProjects / totalProjects) * 100;
            progressBar.style.width = `${percentage}%`;
        } else {
            progressBar.style.width = '0%';
        }
    }

    // Initial call
    updateProgress();

    // --- Footer Year ---
    document.getElementById('year').textContent = new Date().getFullYear();

    // --- Click Handler for Completed Projects ---
    // (Optional: Add specific behavior for completed projects if needed, 
    // though the <a> tag or onclick logic would typically handle navigation)
    const completedCards = document.querySelectorAll('.project-card.completed');
    completedCards.forEach(card => {
        card.addEventListener('click', () => {
            // Logic to navigate to the project page
            // For now, we just log it or alert if no link is present
            // In a real scenario, these would be <a> tags or have data-href
            console.log('Clicked completed project:', card.querySelector('h3').textContent);
            // window.location.href = card.dataset.link; // Example
        });
    });
});
