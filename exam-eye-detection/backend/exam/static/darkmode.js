// Dark Mode Toggle Script
(function() {
    const DARK_MODE_KEY = 'examguard_dark_mode';
    
    function isDarkMode() {
        return localStorage.getItem(DARK_MODE_KEY) === 'true';
    }
    
    function setDarkMode(enabled) {
        localStorage.setItem(DARK_MODE_KEY, enabled);
        document.documentElement.setAttribute('data-theme', enabled ? 'dark' : 'light');
    }
    
    function createToggleButton() {
        const btn = document.createElement('button');
        btn.id = 'darkModeToggle';
        btn.innerHTML = isDarkMode() ? '☀️' : '🌙';
        btn.title = isDarkMode() ? 'Switch to Light Mode' : 'Switch to Dark Mode';
        btn.onclick = function() {
            const newMode = !isDarkMode();
            setDarkMode(newMode);
            btn.innerHTML = newMode ? '☀️' : '🌙';
            btn.title = newMode ? 'Switch to Light Mode' : 'Switch to Dark Mode';
        };
        document.body.appendChild(btn);
    }
    
    // Initialize on page load
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            setDarkMode(isDarkMode());
            createToggleButton();
        });
    } else {
        setDarkMode(isDarkMode());
        createToggleButton();
    }
})();
