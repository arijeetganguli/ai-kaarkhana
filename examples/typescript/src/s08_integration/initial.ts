/**
 * S8 initial implementation: fetch a price in cents from a pricing service.
 *
 * PROBLEMS: no timeout; `res.ok` is never checked, so the body of a 404 or a 500 is parsed
 * as a price; failures surface as NaN or as a generic error instead of a domain error. A unit
 * test with a stubbed `fetch` cannot see any of this.
 */
export type FetchLike = typeof fetch;

export class PriceClient {
  constructor(
    private readonly baseUrl: string,
    private readonly fetchImpl: FetchLike = fetch,
  ) {}

  async fetchPriceCents(sku: string): Promise<number> {
    const res = await this.fetchImpl(`${this.baseUrl}/prices/${sku}`);
    const body = await res.text();
    return Number(body.trim());
  }
}
