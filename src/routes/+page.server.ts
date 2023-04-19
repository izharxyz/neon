import { redirect } from "@sveltejs/kit";
import { prisma } from "$lib/server/prisma";
import type { Actions, PageServerLoad } from "./$types";

export const load: PageServerLoad = async () => {

    const posts = await prisma.post.findMany()
    console.log({posts})

    return {
        posts
    }
};

export const actions: Actions = {
    setTheme: async ({url, cookies}) => {
        const theme = url.searchParams.get('theme');
        const redirectTo = url.searchParams.get('redirectTo');
        
        if (theme) {
            cookies.set("colortheme", theme, {
                path: '/',
                maxAge: 60 * 60 * 24 * 365
            })
        }

        throw redirect(303, redirectTo ?? '/')
    }
};