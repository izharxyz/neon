import type { Handle } from "@sveltejs/kit";
import { auth } from "$lib/server/lucia";

export const handle = (async ({ event, resolve }) => {
    event.locals.auth = auth.handleRequest(event);
    let theme: string | null = null;

    const newTheme = event.url.searchParams.get("theme");
    const cookieTheme = event.cookies.get("colortheme");

    if (newTheme) {
        theme = newTheme;
    } else if (cookieTheme) {
        theme = cookieTheme;
    }

    if (theme) {
        return await resolve(event, {
            transformPageChunk: ({ html }) => html.replace('data-theme=""', `data-theme=${theme}`),
        })
    }

    return await resolve(event);
}) satisfies Handle;