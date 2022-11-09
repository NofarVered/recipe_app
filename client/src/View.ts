class View{
    static renderAll (data:DataModule):void{
        $("#recipes-container").empty()
        let source = $("#recipe-card-template").html()
        let template = Handlebars.compile(source)
        $("#recipes-container").append(template({recipes: data.recipes}))
    }
}