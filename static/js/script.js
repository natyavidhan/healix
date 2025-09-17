// Healix - Custom JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Dark Mode Toggle Functionality
    const darkModeToggle = document.getElementById('darkModeToggle');
    const body = document.body;
    
    // Check for saved theme preference or respect OS preference
    const savedTheme = localStorage.getItem('theme');
    const prefersDarkScheme = window.matchMedia('(prefers-color-scheme: dark)');
    
    // If the user has explicitly chosen a theme, use it
    if (savedTheme === 'dark') {
        body.setAttribute('data-theme', 'dark');
        darkModeToggle.checked = true;
    } else if (savedTheme === 'light') {
        body.setAttribute('data-theme', 'light');
        darkModeToggle.checked = false;
    } else {
        // If no saved preference, use the OS preference
        if (prefersDarkScheme.matches) {
            body.setAttribute('data-theme', 'dark');
            darkModeToggle.checked = true;
        }
    }
    
    // Listen for toggle changes
    darkModeToggle.addEventListener('change', function() {
        if (this.checked) {
            body.setAttribute('data-theme', 'dark');
            localStorage.setItem('theme', 'dark');
        } else {
            body.setAttribute('data-theme', 'light');
            localStorage.setItem('theme', 'light');
        }
    });
    
    // Navbar scroll behavior
    const navbar = document.querySelector('.navbar');
    
    function updateNavbarClass() {
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    }
    
    // Initial call to set the class correctly on page load
    updateNavbarClass();
    
    // Update on scroll
    window.addEventListener('scroll', updateNavbarClass);
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            
            if (targetId === '#') return; // Ignore empty anchors
            
            const targetElement = document.querySelector(targetId);
            
            if (targetElement) {
                window.scrollTo({
                    top: targetElement.offsetTop - 80, // Adjust for fixed navbar
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Initialize Bootstrap tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    // Handle form submissions - placeholder for future functionality
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            // For future form handling
            // e.preventDefault();
            // console.log('Form submitted');
        });
    });
});

// Additional animations and interactions could be added here
