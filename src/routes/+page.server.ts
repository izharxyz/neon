import { fail } from "@sveltejs/kit";
import { prisma } from "$lib/server/prisma";
import type { Actions ,PageServerLoad } from "./$types";

export const load: PageServerLoad = async () => {
    return {
        posts: await prisma.post.findMany()
    }
};

export const actions: Actions = {
    createPost: async ({ request }) => {
        const { title, content } = Object.fromEntries(await request.formData()) as { 
            title: string, 
            content: string
        }

        try {
            await prisma.post.create({
                data: {
                    title,
                    content
                }
            })
        } catch (err) {
            return fail(500, { message: 'fff'})
        }

        console.log("post created?")
        return {
            status: 201
        }
    },
};