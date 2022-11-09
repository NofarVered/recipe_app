const data: DataModule = new DataModule();
$("#search-btn").on("click", function(){
    let ingredient: string = <string> $("#ingredient-input").val()
    let dairy: boolean = $("#dairy-checkbox").is(":checked")
    let gluten: boolean = $("#gluten-checkbox").is(":checked")
    data.generateRecipes(ingredient, dairy, gluten).then(() => View.renderAll(data));
});
