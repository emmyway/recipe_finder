$(document).ready(function() {
    fetch('/api/favorites')
        .then(response => response.json())
        .then(data => {
            const favoritesSection = $('.recipe-details');
            data.forEach(favorite => {
                const favoriteItem = `
                    <div class="favorite-item">
                        <h3>${favorite.title}</h3>
                        <p>${favorite.description}</p>
                    </div>
                `;
                favoritesSection.append(favoriteItem);
            });
        })
        .catch(error => console.error('Error fetching favorite recipes:', error));
});
