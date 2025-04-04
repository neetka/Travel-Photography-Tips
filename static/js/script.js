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
});