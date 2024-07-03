$(document).ready(function() {
    fetch('/api/mealplan')
        .then(response => response.json())
        .then(data => {
            const mealPlanSection = $('.recipe-details');
            data.forEach(meal => {
                const mealItem = `
                    <div class="meal-item">
                        <h3>${meal.title}</h3>
                        <p>${meal.description}</p>
                    </div>
                `;
                mealPlanSection.append(mealItem);
            });
        })
        .catch(error => console.error('Error fetching meal plan:', error));
});
