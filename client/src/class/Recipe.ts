class Recipe{
    constructor(protected _title: string, protected _thumbnail: string, protected _href: string, protected _ingredients: string[]
    ) {}

    get title(): string{
        return this._title;
    }

    get thumbnail(): string{
        return this._thumbnail;
    }

    get href(): string{
        return this._href;
    }

    get ingredients(): string[]{
        return this._ingredients;
    }
}


