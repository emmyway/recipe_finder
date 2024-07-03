$(document).ready(function() {
    const recipeId = 1; // Replace with dynamic value as needed

    fetch(`/api/recipe/${recipeId}`)
        .then(response => response.json())
        .then(data => {
            const recipeDetail = $('.recipe-detail');
            const recipeContent = `
                <h2>${data.title}</h2>
                <p>${data.description}</p>
                <img src="${data.image}" alt="${data.title}">
                <h3>Ingredients</h3>
                <ul>
                    ${data.ingredients.map(ingredient => `<li>${ingredient}</li>`).join('')}
                </ul>
                <h3>Instructions</h3>
                <p>${data.instructions}</p>
            `;
            recipeDetail.append(recipeContent);
        })
        .catch(error => console.error('Error fetching recipe details:', error));
});
