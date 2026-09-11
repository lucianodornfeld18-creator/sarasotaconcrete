// Keeps preview hosts out of the index.
//
// A Pages deployment is reachable at <project>.pages.dev before the real domain is attached. If a
// crawler finds that host first, the preview competes with sarasotaconcrete.com for its own content
// and the canonical tags (which point at the apex) will not stop the preview being crawled.
//
// So: every response served from a *.pages.dev host gets X-Robots-Tag: noindex, nofollow. Responses
// on the real domain are untouched. _headers cannot do this, because its matcher is a path, not a host.
export async function onRequest(context) {
  const response = await context.next();
  let host = "";
  try {
    host = new URL(context.request.url).hostname;
  } catch {
    return response;
  }
  if (host.endsWith(".pages.dev")) {
    const headers = new Headers(response.headers);
    headers.set("X-Robots-Tag", "noindex, nofollow");
    return new Response(response.body, { status: response.status, statusText: response.statusText, headers });
  }
  return response;
}
