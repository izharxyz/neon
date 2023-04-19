import { fail, redirect } from "@sveltejs/kit";
import { prisma } from "$lib/server/prisma";
import type { Actions, PageServerLoad } from "./$types";

export const load: PageServerLoad = async () => {
    return {
        posts: await prisma.post.findMany()
    }
};

export const actions: Actions = {
    default : async ({ request }) => {
        const { title, excerpt, category, thumbnail, content } = Object.fromEntries(await request.formData()) as {
            title: string 
            excerpt: string
            category: string
            thumbnail: string
            content: string
        }
        
        console.log({title, excerpt, category,thumbnail, content}) 

        try {
            await prisma.post.create({
                data: {
                    title,
                    excerpt,
                    content
                }
            })
        } catch (err) {
            console.log(err)
            return fail(500, { message: 'fff'})
        }
        throw redirect(302, '/')
    },
};