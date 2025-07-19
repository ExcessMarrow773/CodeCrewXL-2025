// Function to show the loading screen
function showLoader() {
    document.getElementById('loader-overlay').classList.remove('loader-hidden');
}

// Function to hide the loading screen
function hideLoader() {
    document.getElementById('loader-overlay').classList.add('loader-hidden');
}


// Example: For page load (if content is loaded after initial page render)
window.addEventListener('load', () => {
    hideLoader(); // Hide loader once the page content is loaded
});