import { fail } from "@sveltejs/kit";
import { prisma } from "$lib/server/prisma";
import type { Actions, PageServerLoad } from "./$types";

export const load: PageServerLoad = async () => {
    return {
        posts: await prisma.post.findMany()
    }
};

export const actions: Actions = {
    default : async ({ request }) => {
        const { content } = Object.fromEntries(await request.formData()) as { 
            content: string
        }
        
        console.log(content) 

        try {
            //
        } catch (err) {
            console.log(err)
            return fail(500, { message: 'fff'})
        }

        return {
            status: 201
        }
    },
};