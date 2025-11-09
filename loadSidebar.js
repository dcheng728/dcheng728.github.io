// Sidebar HTML template
const sidebarHTML = `
<div class="sidenav">
    <a href="index.html" id="nav-home">Homepage</a>
    <a href="researchHighlights.html" id="nav-research">Research Highlights</a>
    <a href="personalProjects.html" id="nav-projects">AI/ML Personal Projects</a>
    <a href="self-study/self-study.html" id="nav-selfstudy">Physics Self-Study</a>
</div>
`;

// Load sidebar on page load
function loadSidebar() {
    // Insert sidebar at the beginning of body
    document.body.insertAdjacentHTML('afterbegin', sidebarHTML);
    
    // Fix relative links based on current location
    // Check both pathname and full href for robustness
    const currentPath = window.location.pathname;
    const currentHref = window.location.href;
    
    // Check if we're in a subfolder (case-insensitive for robustness)
    const isInSubfolder = currentPath.toLowerCase().includes('/self-study/') || 
                          currentHref.toLowerCase().includes('/self-study/');
    
    if (isInSubfolder) {
        // We're in self-study folder, need to adjust paths
        document.getElementById('nav-home').href = '../index.html';
        // document.getElementById('nav-pubs').href = '../publications+manuscripts.html';
        document.getElementById('nav-research').href = '../researchHighlights.html';
        document.getElementById('nav-projects').href = '../personalProjects.html';
        document.getElementById('nav-selfstudy').href = 'self-study.html';
    }
}

// Try to load as early as possible
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadSidebar);
} else {
    // Document already loaded
    loadSidebar();
}
