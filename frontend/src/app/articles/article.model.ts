export class Article {
  constructor(
    public name: string,
    public abstract: string,
    public url: string,
    public source: string,
    public researchAreas?: List[string],
    public authors?: List[string],
  ) {}
}
