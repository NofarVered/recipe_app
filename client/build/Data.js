"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
class DataModule {
    constructor() {
        this._recipes = [];
    }
    get recipes() {
        return this._recipes;
    }
    generateRecipes(search, dairy, gluten) {
        return __awaiter(this, void 0, void 0, function* () {
            let result = yield $.get(`/search?search=${search}&dairy=${dairy}&gluten=${gluten}`);
            let recipesList = result["recipes"];
            for (const recipe of recipesList) {
                this._recipes.push(new Recipe(recipe.title, recipe.thumbnail, recipe.href, recipe.ingredients));
            }
        });
    }
}
