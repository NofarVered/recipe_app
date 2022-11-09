"use strict";
class Recipe {
    constructor(_title, _thumbnail, _href, _ingredients) {
        this._title = _title;
        this._thumbnail = _thumbnail;
        this._href = _href;
        this._ingredients = _ingredients;
    }
    get title() {
        return this._title;
    }
    get thumbnail() {
        return this._thumbnail;
    }
    get href() {
        return this._href;
    }
    get ingredients() {
        return this._ingredients;
    }
}
