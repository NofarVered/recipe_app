class View{
    static renderAll (recipes:DataModule):void{
        $("#recipes-container").empty()
        let source = $("#recipe-card-template").html()
        let template = Handlebars.compile(source)
        $("#recipes-container").append(template({recipes: recipes}))
    }
}