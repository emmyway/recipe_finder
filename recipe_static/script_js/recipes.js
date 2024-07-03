$(document).ready(function() {
    fetch('/api/recipes')
        .then(response => response.json())
        .then(data => {
            const recipeGallery = $('.recipe-gallery');
            data.forEach(recipe => {
                const recipeItem = `
                    <div class="recipe-item">
                        <h3>${recipe.title}</h3>
                        <p>${recipe.description}</p>
                    </div>
                `;
                recipeGallery.append(recipeItem);
            });
        })
        .catch(error => console.error('Error fetching recipes:', error));
});
