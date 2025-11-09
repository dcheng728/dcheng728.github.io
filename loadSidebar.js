// Sidebar HTML template
const sidebarHTML = `
<div class="sidenav">
    <a href="index.html" id="nav-home">Homepage</a>
    <a href="publications+manuscripts.html" id="nav-pubs">Publications & Manuscripts</a>
    <a href="researchHighlights.html" id="nav-research">Research Highlights</a>
    <a href="personalProjects.html" id="nav-projects">Personal Projects</a>
    <a href="self-study/self-study.html" id="nav-selfstudy">Physics Self-Study</a>
</div>
`;

// Load sidebar on page load
document.addEventListener('DOMContentLoaded', function() {
    // Insert sidebar at the beginning of body
    document.body.insertAdjacentHTML('afterbegin', sidebarHTML);
    
    // Fix relative links based on current location
    const currentPath = window.location.pathname;
    const isInSubfolder = currentPath.includes('/self-study/');
    
    if (isInSubfolder) {
        // We're in self-study folder, need to adjust paths
        document.getElementById('nav-home').href = '../index.html';
        document.getElementById('nav-pubs').href = '../publications+manuscripts.html';
        document.getElementById('nav-research').href = '../researchHighlights.html';
        document.getElementById('nav-projects').href = '../personalProjects.html';
        document.getElementById('nav-selfstudy').href = 'self-study.html';
    }
});
