document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const searchBtn = document.getElementById('search-btn');
    const resultsContainer = document.getElementById('results');
    const defaultMessage = document.getElementById('default-message');

    searchBtn.addEventListener('click', searchPhotos);
    searchInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') searchPhotos();
    });

    
    async function searchPhotos() {
        const query = document.getElementById("search-input").value.trim();
        if (!query) return;
    
        const resultsContainer = document.getElementById("results");
        resultsContainer.innerHTML = '<div class="col-span-3 text-center py-8"><p>Loading...</p></div>';
    
        try {
            const response = await fetch('/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: `query=${encodeURIComponent(query)}`
            });
    
            if (!response.ok) {
                const error = await response.json();
                throw new Error(error.error || 'Request failed');
            }
    
            const data = await response.json();
            // Display results...
        } catch (error) {
            resultsContainer.innerHTML = `
                <div class="col-span-3 text-center py-8 text-red-500">
                    <p>Error: ${error.message}</p>
                    <p class="text-sm mt-2">API may be unavailable or your search was too generic</p>
                </div>`;
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
        // Animate form elements on scroll
        const form = document.querySelector('.photography-form');
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('animate__animated', 'animate__fadeInUp');
                }
            });
        });
        
        observer.observe(form);
    
        // Form validation and enhancement
        const locationInput = document.getElementById('location');
        if (locationInput) {
            locationInput.addEventListener('focus', function() {
                this.parentElement.classList.add('focused');
            });
    
            locationInput.addEventListener('blur', function() {
                this.parentElement.classList.remove('focused');
            });
        }
    
        // Smooth scroll behavior
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                document.querySelector(this.getAttribute('href')).scrollIntoView({
                    behavior: 'smooth'
                });
            });
        });
    });
});