class DataModule{
    private _recipes: Recipe[];

    constructor(){
        this._recipes = [];
    }

    get recipes(){
        return this._recipes;
    }

    async generateRecipes(search: string, dairy: boolean, gluten: boolean){
        let result = await $.get(`/search?search=${search}&dairy=${dairy}&gluten=${gluten}`);
        let recipesList = result["recipes"];
        for(const recipe of recipesList){
            this._recipes.push(new Recipe(recipe.title, recipe.thumbnail, recipe.href, recipe.ingredients));
        }
    }
}
