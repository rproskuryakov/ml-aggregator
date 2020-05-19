export class Article {
  constructor(
    public name: string,
    public abstract: string,
    public url: string,
    public source: string,
    public researchAreas?: Array<string>,
    public authors?: Array<string>,
  ) {}
}
