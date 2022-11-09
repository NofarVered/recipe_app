"use strict";
(function () {
    const data = new DataModule();
    $("#search-btn").on("click", function () {
        let ingredient = $("#ingredient-input").val();
        let dairy = $("#dairy-checkbox").is(":checked");
        let gluten = $("#gluten-checkbox").is(":checked");
        data.generateRecipes(ingredient, dairy, gluten).then(() => View.renderAll(data));
    });
})();
