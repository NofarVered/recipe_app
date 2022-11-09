"use strict";
class View {
    static renderAll(data) {
        $("#recipes-container").empty();
        let source = $("#recipe-card-template").html();
        let template = Handlebars.compile(source);
        $("#recipes-container").append(template({ recipes: data.recipes }));
    }
}
