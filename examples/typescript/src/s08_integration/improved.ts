/** S8 improved implementation: explicit timeout, status handling and domain errors. */
import type { FetchLike } from "./initial";

export class PriceNotFoundError extends Error {
  constructor(sku: string) {
    super(`no price for sku: ${sku}`);
    this.name = "PriceNotFoundError";
  }
}

export class PriceServiceError extends Error {
  constructor(message: string, options?: { cause?: unknown }) {
    super(message, options);
    this.name = "PriceServiceError";
  }
}

export class PriceClient {
  constructor(
    private readonly baseUrl: string,
    private readonly timeoutMs: number,
    private readonly fetchImpl: FetchLike = fetch,
  ) {}

  async fetchPriceCents(sku: string): Promise<number> {
    let res: Response;
    try {
      res = await this.fetchImpl(`${this.baseUrl}/prices/${encodeURIComponent(sku)}`, {
        signal: AbortSignal.timeout(this.timeoutMs),
      });
    } catch (cause) {
      if (cause instanceof Error && (cause.name === "TimeoutError" || cause.name === "AbortError")) {
        throw new PriceServiceError(`pricing service timed out after ${this.timeoutMs} ms`, { cause });
      }
      throw new PriceServiceError("pricing service unreachable", { cause });
    }

    if (res.status === 404) {
      throw new PriceNotFoundError(sku);
    }
    if (res.status !== 200) {
      throw new PriceServiceError(`pricing service answered HTTP ${res.status}`);
    }
    const body = (await res.text()).trim();
    if (!/^\d+$/.test(body)) {
      throw new PriceServiceError(`malformed price in response: ${JSON.stringify(body)}`);
    }
    return Number(body);
  }
}
