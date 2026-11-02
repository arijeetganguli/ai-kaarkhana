import { createServer, type Server } from "node:http";
import type { AddressInfo } from "node:net";
import { afterAll, beforeAll, describe, expect, it, vi } from "vitest";
import * as improved from "../src/s08_integration/improved";
import * as initial from "../src/s08_integration/initial";

let server: Server;
let baseUrl: string;

beforeAll(async () => {
  server = createServer((req, res) => {
    const url = req.url ?? "";
    if (url === "/prices/ok") {
      res.writeHead(200).end("1250");
    } else if (url === "/prices/missing") {
      res.writeHead(404).end("not found");
    } else if (url === "/prices/boom") {
      res.writeHead(500).end("internal error");
    } else if (url === "/prices/garbage") {
      res.writeHead(200).end("twelve fifty");
    } else if (url === "/prices/slow") {
      setTimeout(() => res.writeHead(200).end("1250"), 1_500).unref();
    } else {
      res.writeHead(400).end();
    }
  });
  await new Promise<void>((resolve) => server.listen(0, "127.0.0.1", resolve));
  baseUrl = `http://127.0.0.1:${(server.address() as AddressInfo).port}`;
});

afterAll(async () => {
  server.closeAllConnections();
  await new Promise<void>((resolve) => server.close(() => resolve()));
});

describe("S8 why the stubbed unit test is not enough", () => {
  it("passes for the initial implementation with a stubbed fetch", async () => {
    const fakeFetch = vi.fn().mockResolvedValue({ text: async () => "1250" });
    const client = new initial.PriceClient("http://unused.invalid", fakeFetch as unknown as typeof fetch);
    await expect(client.fetchPriceCents("ok")).resolves.toBe(1250);
  });

  it("initial defect: a 404 body becomes NaN, not an error", async () => {
    await expect(new initial.PriceClient(baseUrl).fetchPriceCents("missing")).resolves.toBeNaN();
  });

  it("initial defect: a 500 body becomes NaN, not an error", async () => {
    await expect(new initial.PriceClient(baseUrl).fetchPriceCents("boom")).resolves.toBeNaN();
  });
});

describe("S8 integration tests of the improved client", () => {
  const client = () => new improved.PriceClient(baseUrl, 2_000);

  it("returns the price from a real response", async () => {
    await expect(client().fetchPriceCents("ok")).resolves.toBe(1250);
  });

  it("maps 404 to PriceNotFoundError", async () => {
    await expect(client().fetchPriceCents("missing")).rejects.toThrow(improved.PriceNotFoundError);
    await expect(client().fetchPriceCents("missing")).rejects.toThrow("no price for sku: missing");
  });

  it("maps 500 to PriceServiceError", async () => {
    await expect(client().fetchPriceCents("boom")).rejects.toThrow("pricing service answered HTTP 500");
  });

  it("maps a malformed body to PriceServiceError", async () => {
    await expect(client().fetchPriceCents("garbage")).rejects.toThrow("malformed price in response");
  });

  it("times out within the configured limit", async () => {
    const started = Date.now();
    const impatient = new improved.PriceClient(baseUrl, 300);
    await expect(impatient.fetchPriceCents("slow")).rejects.toThrow("timed out after 300 ms");
    expect(Date.now() - started).toBeLessThan(1_200);
  });

  it("maps a refused connection to PriceServiceError", async () => {
    const unreachable = new improved.PriceClient("http://127.0.0.1:1", 300);
    await expect(unreachable.fetchPriceCents("ok")).rejects.toThrow(improved.PriceServiceError);
  });
});
